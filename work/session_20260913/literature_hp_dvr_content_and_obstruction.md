> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Hermite–Padé table identities over a DVR: applicability and the exact content loss

Date: 2026-09-13. Focused source review and original algebraic specialization by audit_sources. The source statements below are distinct from the original deductions in Sections 3–5. No prime or degree scan was used.

The reviewed literature supplies fraction-free determinant recurrences, including singular-table algorithms. It does not supply an upper bound for the isolated prime-power content of the actual exponential–arctangent extremal matrix. There is nevertheless a useful exact specialization: the excess $v_p(F_n)-v_p(D_n)$ is precisely the content gained by passing from coordinate exterior products to polynomial cross products. Section 4 proves that statement with the actual endpoint normalization. Section 5 exhibits arbitrarily deep isolated defects in another explicit Hermite–Padé input, ruling out an input-independent depth bound from the table identities alone.

## 1. Primary sources and checked hypotheses

**Beckermann–Labahn, Fraction-Free Computation of Matrix Rational Interpolants and Matrix GCDs, SIAM J. Matrix Anal. Appl. 22 (2000), 114–144.** [Author-hosted full text](https://cs.uwaterloo.ca/~glabahn/Papers/exact.pdf), [publisher DOI](https://doi.org/10.1137/S0895479897326912).

Read the setup in Section 2, the normalization in Sections 4–5, Theorem 6.1 on pp. 127–128, and Theorems 7.2–7.3 on pp. 133–136. The coefficient domain is an integral domain with a quotient field. Theorem 6.1 gives cross-multiplication recurrences followed by exact division by the preceding determinant pivot. Theorem 7.2 handles nonperfect paths; Theorem 7.3 describes their solution spaces over the quotient field. These statements apply to our finite Taylor systems over a localization of the integers, and hence to their computations over $\mathbb Z_p$. Their “normal” determinant is nonzero, not necessarily a unit. Exact divisibility of a numerator by a pivot does not imply that the quotient is primitive or that a denominator has no $p$-adic depth. The theorem therefore does not by itself transport a saturated integral kernel basis across the defective prime.

**Beckermann–Labahn, Fraction-Free Computation of Simultaneous Padé Approximants, ISSAC 2009.** [Author-hosted full text](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/bernhard_beckermann/abs/fp26-beckermannPS.pdf).

Read Section 3, equation (3.1), on PDF p. 4; Theorems 4.1–4.2 on PDF pp. 4–5; and Theorem 5.3 on PDF p. 7. The formal input has at least one nonzero constant coefficient; our first series is 1. The polynomial cofactor relation between the determinant-normalized type-I and type-II Mahler systems retains a factor $d^{m-2}$, where $d$ is the multigradient. In our three-series case this factor is $d$. The closest-normal-index descriptions in Theorems 4.1–4.2 are over the coefficient field $K$. Theorem 5.3 retains a previous pivot $d_k$ in the exact recurrence for the next type-II system. These are appropriate normalization identities; deleting the pivot factor would delete precisely the arithmetic information being investigated.

**Doliwa–Siemaszko, Hermite–Padé approximation and integrability, arXiv:2201.06829; J. Approx. Theory 292 (2023), 105910.** [Full preprint](https://arxiv.org/pdf/2201.06829), [journal DOI](https://doi.org/10.1016/j.jat.2023.105910).

Read the canonical determinants (1.10)–(1.16), the perfect-system assumption on PDF p. 5, and Section 2 on PDF pp. 5–8: equation (2.1), Proposition 2.1, and the Paszkowski/Frobenius identities (2.9)–(2.11). The displayed determinant identities have polynomial proofs, so the identities themselves remain true over a DVR even at a zero or nonunit determinant. Dividing them to fill a table requires the relevant pivots. The paper also explicitly retains new input-series coefficients when advancing levels; these formulas are not autonomous scalar recurrences for diagonal determinants. Our $F_n,D_n$ are contents of collections of minors, not individual tau-functions, so their valuations cannot simply be substituted for the valuations of a chosen determinant.

**Access limitation.** Beckermann–Carstensen, Global Identities in the Non-normal Newton–Padé Approximation Table, J. Approx. Theory 74 (1993), 199–220, was identified through its [author-hosted URL](https://www2.mathematik.hu-berlin.de/~cc/cc_homepage/download/1993-BB_CC-Global_Identities_Newton_Pade_Table.pdf). The current download returned an HTML page, and browser PDF-page retrieval failed. No theorem-level claim from that paper is used here. The nonperfect-path theorem above was read in accessible primary text.

The three successfully retrieved PDFs and text extractions are preserved in the session's literature_hp_dvr directory. The failed 1993 retrieval is recorded as HTML rather than treated as a read PDF.

For clarity, the full exponential Taylor series is not an element of $\mathbb Z_p[[z]]$. Every application over $\mathbb Z_p$ here has a stated finite cutoff $L<p$. Its coefficients through $L$ are integral, and one may extend those finitely many coefficients by zeros to apply a formal-series algorithm over that ring. Only identities and matrices using rows through $L$ are then retained. No conclusion about subsequent rows of that artificially extended input is transferred back to the exponential or arctangent.

## 2. The exact valuation obstruction in a fraction-free step

An identity of the form



$$
d\,M_{\mathrm{new}}=r_1M_1-r_2M_2
\tag{1}
$$



is meaningful over $\mathbb Z_p$ even when $d$ is not a unit. Let $\operatorname{cv}_p$ denote the minimum coefficient valuation of a nonzero polynomial vector or matrix. Then its exact content consequence is



$$
\operatorname{cv}_p(M_{\mathrm{new}})
=\operatorname{cv}_p(r_1M_1-r_2M_2)-v_p(d).
\tag{2}
$$



The ultrametric inequality gives a lower bound for the first term on the right. It gives an upper bound only if some coefficient's cancellation is separately controlled. In particular, even if the two summands have equal known valuations, their difference may have arbitrarily larger valuation. This is the unresolved quantity, not a missing field-rank assertion.

Likewise, the polynomial Hirota identity says that the minimum among the valuations of its three nonzero products must be attained at least twice. That is a valid valuation constraint on those exact scalar determinants. It is not an upper bound on one determinant when the other two products can cancel to high order.

## 3. An actual scalar-table specialization, with its limitation

For the actual formal series $f=(1,e^z,\arctan z)$, let $\tau(a,b,c)$ be the determinant of the coefficient matrix with columns



$$
1,z,\ldots,z^a;\quad e^z,ze^z,\ldots,z^be^z;
\quad \arctan z,z\arctan z,\ldots,z^c\arctan z
$$



and consecutive rows $0,\ldots,a+b+c+2$. A degree $-1$ block is empty. All statements in this section are over $\mathbb Z_p$ with the largest row index below $p$, so Taylor denominators are units.

Put $u=(n-1,n-1,n-1)$, and use subscripts $A,B,C$ to denote increasing the corresponding degree by 1. The actual determinant identity is



$$
\tau_{AB}\tau_C-\tau_B\tau_{AC}+\tau_A\tau_{BC}=0.
\tag{3}
$$



It is a specialization of the polynomial determinant identity in the source, so it requires no unproved perfectness of this three-series system.

Eliminating the identity block belonging to the first series proves the following exact identifications. The determinant $\tau(u)$ is the unscaled maximal minor of $X_n$ omitting its final row $3n$. The determinant $\tau_A$ is the unscaled maximal minor omitting its first row $n$. The determinants $\tau_B,\tau_C$ are those of $X_n$ with respectively the extra column $B_n,C_n$. Expanding along that extra column shows that each belongs to the maximal-minor ideal of $X_n$. Consequently



$$
v_p(\tau(u)),\ v_p(\tau_A),\
v_p(\tau_B),\ v_p(\tau_C)\ \ge v_p(F_n).
\tag{4}
$$



The two-shift determinants in (3) use the further actual row $3n+1$. Thus take $p>3n+1$ for the complete displayed identity. Neither (3) nor (4) identifies any of these selected minors as attaining the whole maximal-minor content. After division by $p^{v_p(F_n)}$, (3) still contains unknown primitive residues and the two-shift determinants. Replacing those residues by units would be an additional arithmetic hypothesis. This is why the scalar tau identity alone does not strengthen the reviewed contiguous gcd law.

## 4. Exact coordinate-to-polynomial content identity for the actual pair

This section is an original algebraic specialization using the already reviewed primitive-dual identity. It is also an independent explanation of the inequality $v_p(D_n)\le v_p(F_n)$.

Fix $p>3n$, let $R=\mathbb Z_p$, and set



$$
K=\begin{pmatrix}H_n\\B(1)\\C(1)\end{pmatrix},
\qquad E=\det K=\mathcal E_n\ne0.
$$



Let $U,V\in R^{2n+2}$ be the last two columns of $\operatorname{adj}K$, in this order. Then $KU=E e_{2n+1}$, $KV=E e_{2n+2}$, with one-based row numbering. In particular $U/E,V/E$ are precisely the two actual endpoint-normalized high solutions in their $B,C$ coefficient coordinates.

Jacobi's complementary-minor identity gives, for every pair of coefficient coordinates $i<j$,



$$
(U_iV_j-U_jV_i)
 =\pm E\det H_n[\text{all rows},\text{all columns except }i,j].
\tag{5}
$$



The sign depends only on the deleted columns. Every maximal minor of $H_n$ occurs. Therefore



$$
\boxed{\operatorname{cv}_p(U\wedge V)=v_p(E)+v_p(D_n).}
\tag{6}
$$



Reconstruct $A$ linearly by taking the negative Taylor truncation through degree $n$ of $Be^z+C\arctan z$. At $p>3n$ this is an $R$-linear map $J$ from coefficient vectors $(B,C)$ to coefficient vectors of $(A,B,C)$. Projection back to $B,C$ is an integral left inverse of $J$; consequently its exterior square preserves content exactly.

Let $\mu$ denote the coefficient map that takes the exterior product of two triple coefficient vectors to their polynomial cross product. The multiplication of polynomials makes $\mu$ an $R$-linear map with integer structure constants. Thus



$$
\operatorname{cv}_p\bigl(\mu(JU\wedge JV)\bigr)
\ge \operatorname{cv}_p(U\wedge V).
\tag{7}
$$



Write $T_E,T_F$ for the endpoint-normalized polynomial triples. The reviewed result in raw_extremal_dual_polynomial_and_content_identity.md gives



$$
T_E\times T_F
=\frac1{Z_n}
   \bigl(\widehat Q_n,\widehat P_{e,n},\widehat P_{\arctan,n}\bigr),
\tag{8}
$$



where $\widehat P_{e,n}$ and $\widehat P_{\arctan,n}$ are the degree-$2n$ Taylor truncations of $\widehat Q_ne^z$ and $\widehat Q_n\arctan z$. They are $p$-integral. For the standard cross-product convention, its second and third components satisfy $S_1-e^zS_0=O(z^{3n+1})$ and $S_2-(\arctan z)S_0=O(z^{3n+1})$; hence both numerator signs are positive. The first component $\widehat Q_n$ is $p$-primitive. Using the exact normalization $E=(-1)^nF_nZ_n$, we obtain



$$
\mu(JU\wedge JV)
=\frac{E^2}{Z_n}
  \bigl(\widehat Q_n,\widehat P_{e,n},\widehat P_{\arctan,n}\bigr),
$$



and hence



$$
\boxed{\operatorname{cv}_p\bigl(\mu(JU\wedge JV)\bigr)
=v_p(E)+v_p(F_n).}
\tag{9}
$$



Combining (6)–(9), put $e=v_p(D_n)$, $f=v_p(F_n)$, and divide $U\wedge V$ by a generator of its coefficient ideal. This gives an integral primitive exterior vector $\omega$, well-defined up to an $R$-unit, satisfying



$$
\boxed{\operatorname{cv}_p\bigl(\mu((\wedge^2J)\omega)\bigr)=f-e.}
\tag{10}
$$



Thus $f-e$ is exactly the cancellation depth of this explicit polynomial-multiplication map on the primitive Plücker coordinates of the actual high-solution plane. Formula (7) proves $f\ge e$ without the earlier shifted-left-annihilator argument.

This does not give an upper bound for (10). Integral linear maps can send primitive vectors arbitrarily close to their kernel. In the present setting, when $e=0$, vanishing of the polynomial cross product modulo $p$ means the two independent coefficient vectors become polynomial multiples of a common triple over $\mathbb F_p(z)$. This agrees with the extremal module profile; it must not be confused with ordinary linear dependence of their full coefficient vectors.

## 5. Arbitrarily deep isolated defects in an explicit other input

The following example is a rigorous obstruction to obtaining an input-independent isolated-depth bound from the generic table identities. It is not an example from the actual arctangent family.

Fix a prime $p>6$, an integer $h\ge1$, and $\delta=p^h$. Replace the third series by



$$
g(z)=e^z-1+\delta z^2+2\delta z^3+z^4+z^7e^{2z}.
\tag{11}
$$



Keep the first two series $1,e^z$, and define the same integer row-scaled matrices $H_r,X_r$ using this new third series. Their entries are integers: multiplication of the Taylor coefficients in (11) by row factorials gives integers. The last term has no effect on the matrices considered below.

For $r=1$, the extremal matrix is



$$
X_1=\begin{pmatrix}
1&1\\
1&1+2\delta\\
1&1+12\delta
\end{pmatrix}.
$$



Its three maximal minors are $2\delta,12\delta,10\delta$. Thus its global content is $2p^h$, and $v_p(F_1)=h$. The exponential two-column minor of $H_1$, in rows 2 and 3, is



$$
\det\begin{pmatrix}1&2\\1&3\end{pmatrix}=1,
$$



so $D_1=1$.

For $X_2$, use rows $2,3,4,5$ and columns $B_0,B_1,C_0,C_1$. Subtract the first two columns from the corresponding last two. Modulo $p$, the resulting last columns are the coefficient columns of $z^4,z^5$, since the terms $-1,-z$ lie below these rows and $\delta=0$. The chosen row-scaled determinant is



$$
1\cdot4!\cdot5!=2880\not\equiv0\pmod p.
$$



Therefore $v_p(F_2)=0$. We have proved, with no numerical search,



$$
\boxed{v_p(F_1)=h,\qquad v_p(D_1)=0,\qquad v_p(F_2)=0,}
\tag{12}
$$



for every $h\ge1$. The generic polynomial determinant identities and the nonperfect fraction-free theory apply to this input. They permit isolated defects of unrestricted depth even with a unit high content and a unit next extremal content. This does not contradict the actual contiguous inequality: its left side is zero in (12).

## 6. Ranked next step

The most concrete arithmetic target identified here is to bound (10) for the actual exponential–arctangent plane, or to evaluate one coefficient of that polynomial cross product after dividing by the coordinate content. Equivalently, one needs a unit or a controlled-depth transverse minor measuring how the two integral high solutions fail to be polynomial multiples of the same lower-degree triple.

The new accessory compatibility equations being developed independently address precisely the actual-input restriction that the universal example lacks. A successful finite-difference, differential, or resultant calculation must retain the primitive scale in (10). Replacing the plane by a field-normalized Mahler basis, or canceling its multigradient before taking valuations, would lose that scale.

The literature review closes no isolated-depth bound for the actual family. It supplies verified exact recurrences, a precise specialization, and a demonstrated reason why field normality or fraction-free computability alone cannot supply the missing bound.
