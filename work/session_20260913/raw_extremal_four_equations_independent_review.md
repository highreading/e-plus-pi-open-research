> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the four accessory equations and their prime-power depth

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed in full: raw_extremal_four_accessory_equations.md, together with the original cofactor construction in raw_extremal_no_accessory_compatibility.md and its root review. **The four-equation equivalence, including the full prime-power valuation formula, passes.** This is a smaller exact characterization of the extremal defect. It does not exclude its solutions or bound their lifting depth.

I checked the arguments algebraically rather than by a new degree or prime scan. One optional explanatory addition was sent to the author: in the necessity direction over $\mathbb Z/p^h\mathbb Z$, explicitly identify the actual polynomial $C$ as a unit multiple of the cofactor generator $C^*$, before passing its residue equations to $C^*$. Section 6 below supplies that link in detail.

Throughout, $n=d+1$, $M=3d+4$, $s=M-2=3d+2$, $D=1+z^2$, and $p>3d+3=M-1$. In particular $p=M$ is included whenever $M$ is prime.

## 1. The polynomial exponential branch and the algebraic Abel argument

For a monomial $z^m$, direct expansion of the displayed operator gives coefficient $m-d$ at degree $m+2$ in $L^{[1]}z^m$. A nonzero polynomial exponential solution therefore has degree $d$. Subtracting its leading multiple from any other solution proves that this polynomial solution space has dimension one over the residue field.

The map $L:\mathcal P_d\to\mathcal P_{d-1}$ has a kernel of dimension at least one by dimension. To rule out dimension two, the proposed determinant



$$
W=\det\begin{pmatrix}
B&C_1&C_2\\
B+B'&C_1'&C_2'\\
B+2B'+B''&C_1''&C_2''
\end{pmatrix}
$$



is indeed nonzero. Put $Q=B/C_1$, $R=C_2/C_1$, $J=Q'+Q$, and $K=R'$. Since both numerator and denominator degrees of $R$ are less than $p$, $K=0$ would imply $R$ is constant. This follows by reducing the fraction and using divisibility into its derivatives; it does not assume that all derivative constants in $K(z)$ are ordinary constants without the degree restriction.

Also $J\ne0$, since a rational logarithmic derivative is $O(z^{-1})$ at infinity and cannot equal $-1$. Dividing the three formal columns by $C_1$ reduces the determinant, up to an invertible rational factor and sign, to



$$
K(J+J')-K'J.
$$



Its vanishing would imply $(K/J)'/(K/J)=1$, again impossible for a rational function. No full exponential series or characteristic-zero analytic Wronskian criterion is used.

The degree estimate $\deg W\le3d-2$ is correct. In the term containing the last-row exponential entry, the other factor is $C_1C_2'-C_1'C_2$, of degree at most $2d-2$. Equal leading degrees cancel; otherwise their sum is at most $2d-1$. The other two terms have no larger degree.

The second-derivative coefficient of $L/(zD)$ is



$$
-1-\frac{s}{z}+2\frac{D'}D.
$$



Differentiating the determinant therefore gives



$$
W'=\left(\frac{s}{z}-2\frac{D'}D\right)W.
$$



The subtracted exponential contribution is essential and has the correct sign. For the nonzero polynomial $P=D^2W$, one gets $zP'=sP$ and $\deg P\le3d+2=s<p$. Coefficient comparison permits only $P=\kappa z^s$. This contradicts divisibility by $D^2$, since $D(0)=1$. The argument does not discard possible $z^p$ constants: the degree bound excludes them before coefficient comparison.

Thus $\dim\ker L=1$, and $L:\mathcal P_d\to\mathcal P_{d-1}$ is surjective, on the locus where the polynomial exponential branch exists.

## 2. The coefficient matrix, cofactor generator, and parameter degrees

I independently expanded $Lz^j$. The four coefficient entries in row $k$ are exactly



$$
\begin{aligned}
j=k+2:&\quad (k+2)(k+1)(k-3d-2),\\
j=k+1:&\quad (k+1)(\gamma-k),\\
j=k:&\quad k(k-1)(k-3d)+(k-d)\beta+2d^2(d-1),\\
j=k-1:&\quad -(k-d-1)(k-d).
\end{aligned}
$$



The two highest output coefficients cancel at input degrees $d,d-1$, so this is a $d$-by-$(d+1)$ matrix with no missing output row. The signed maximal cofactors satisfy $U_dv=0$ as an integer polynomial identity. Each entry has total parameter degree at most $d$. On the exponential-equation locus at least one maximal minor is a unit modulo $p$; no specified cofactor, including $v_0$, is presumed nonzero.

Reduction of the simple-pole numerator modulo the monic $D$ is valid whether $D$ splits or not. The two residues $R_0,R_1$ have degree at most $d+1$. The displayed continuant for $v_0$ also has the correct signs and indices: the matrix with columns $1,\ldots,d$ has diagonal $b_k$, upper diagonal $a_k$, and two lower diagonals $c_k,e_k$.

In the exponential downward recursion, the successive divisors are $-1,\ldots,-d$. Induction gives denominator dividing $r!$ for $b_{d-r}$ and parameter degree at most $r$. Therefore $d!B^*$ has integral coefficient polynomials and both $E_0,E_1$ have total parameter degree at most $d+1$, as claimed.

## 3. Pole compatibility and polynomial solvability for A

When $R_0=R_1=0$, the forcing $\mathcal T_L(C^*)$ is a polynomial of degree at most $d-1$. The only potentially degree-$d$ polynomial terms, $-2z(C^*)'+2dC^*$, cancel at full degree and are already smaller otherwise. The divided numerator has degree at most $d-1$. Surjectivity of $L$ therefore gives $A_0\in\mathcal P_d$, unique modulo $C^*$.

This is an actual polynomial solvability argument. It is not an assertion that removing the poles of a general rational differential equation automatically produces a polynomial solution.

The optional claim $C^*(\pm i)\ne0$ is also correct under these hypotheses. A simple zero contradicts the residue equation. For a zero of multiplicity $m\ge2$, the lowest term of $LC^*$ has coefficient $-2m^2(m-1)$, a unit because $m\le d<p$. This excludes such a zero as well.

## 4. The two low initial constraints and their nonzero scaling

Let $C_0=C^*$, $H_0=A_0+C_0F_T$. If their two initial columns were dependent, a nonzero constant linear combination would produce $A+CF_T$ with two zero initial coefficients. Its differential residual is $O(z^{M-2})$, so the unit indicial recursion forces order $M$.

If $C=0$, this is impossible for a nonzero polynomial of degree at most $d$. Otherwise



$$
S=D(A'C-AC')+C^2
$$



is a nonzero polynomial of degree at most $2d$. Its nonvanishing follows from the nonzero residues of $1/D$: a rational derivative has zero simple-pole residue, also in positive characteristic. The order-$M$ relation forces $z^{M-1}\mid S$, a contradiction since $M-1=3d+3>2d$.

The finite-jet error has the stated order. Namely $F_T'-1/D=O(z^{M-1})$, including at $p=M$, and multiplying by $DC^2$ cannot introduce a lower coefficient. Thus the two-by-two initial determinant is a unit over the residue field.

Solving that initial system gives $A=\lambda A_0+\mu C_0$, $C=\lambda C_0$. If $\lambda=0$, the corresponding high-order combination $\mu C_0+BE_T$ would force



$$
C_0(B'+B)-C_0'B
$$



to have order at least $M-1$. This polynomial is nonzero by the rational-logarithmic-derivative argument, and has degree at most $2d$, again impossible. Thus $\lambda\ne0$. This verifies both the initial normalization and the nonzero arctangent component.

## 5. Finite-jet sufficiency at the boundary p=M

The errors in replacing the exponential and arctangent derivatives by their finite jets through $M-1$ have orders at least $M-j$ for derivative order $j\le3$. The coefficient of the third derivative has a factor $z$. Hence the full differential identity yields



$$
L(A+BE_T+CF_T)=O(z^{M-2}).
$$



The coefficient of an as-yet undetermined remainder term $z^k$, in output degree $k-2$, is $k(k-1)(k-M)$. Every such factor is a unit for $2\le k\le M-1$, even when $p=M$. Starting from the two zero initial coefficients therefore gives the full order $M$. Neither $M$ nor $M!$ is divided out.

## 6. Both directions over R_h=Z/p^h Z

**From a primitive approximate extremal triple to the four equations.** Its reduction gives a nonzero actual extremal triple over the residue field. The reviewed leading numerator identity implies that $b_d$ and $\Xi_d$ are units. The universal cleared numerator has degree at most $s$, and the finite-jet order argument makes every coefficient below $s$ zero in $R_h$. Hence $N=\kappa z^s$, with $\kappa=b_d\Xi_d$ a unit.

The cofactor construction can consequently be carried out over $R_h$. The numerator coefficients are polynomial expressions; their origin factors are divided out only after the corresponding low coefficients have been shown zero. Multiplication by $D^{-1}$ is legitimate in $R_h[[z]]$, and rational coefficient identities may be taken in the localization at the monic $D$ and $z$. The only constant Wronskian divisor is the unit $\kappa$.

The infinity coefficient elimination does not require an individual leading coefficient of $C$ or $A$ to be a unit. The two leading Laurent vectors of $C$ and $A-C/z$ form a matrix with determinant $\pm\Xi_d$, a unit. The equations at degree $d+1$ force the raising coefficient $F(d)=0$; the next two equations, using that same unit matrix, force $F(d-1)=0$ and the next coefficient $G(d)=0$. Their integer degree separation is 1. Thus they determine the remaining displayed coefficients of $L$ over $R_h$ without a hidden division by a nonunit.

Normalize the unit $b_d$ to 1. The unit downward recursion then identifies the actual $B$ with $B^*$, giving $E_0=E_1=0$ in $R_h$.

To make the $C^*$ normalization explicit, reduction modulo $p$ now satisfies Lemma 1. A maximal minor of $U_d$ is therefore a unit in $R_h$. The kernel of this split surjection is free of rank one, generated by its cofactor vector $C^*$. The actual $C$ has nonzero reduction, because otherwise the unit numerator would vanish modulo $p$. Consequently $C=\lambda C^*$ for a unit $\lambda\in R_h$. The residue equations of the actual $C$ are linear in $C$; dividing by that unit gives $R_0=R_1=0$ for $C^*$.

**From a root of the four equations to a primitive approximate triple.** The constructed $B^*$ has unit leading coefficient, and its reduction satisfies the exponential equation. Lemma 1 therefore gives a unit maximal minor of $U_d$. Completing that minor performs the surjection and kernel calculation by invertible matrices over $R_h$, so this is a genuine lift of the field rank statement.

The residue equations make the forcing polynomial of the required degree over $R_h$. Solve for $A_0$ with the unit maximal minor. The initial two-by-two determinant reduces to the nonzero determinant in Section 4 and is thus a unit in $R_h$. It gives $\mu,\lambda$, with $\lambda$ a unit by its residue-field reduction. The induction from Section 5 uses only units in $R_h$, producing all actual Taylor rows modulo $p^h$. The leading coefficient of $B^*$ remains 1, so the coefficient vector is primitive.

This proves the ring equivalence. It is stronger than mere equality of residue-field zero sets, and both directions retain the lowest row imposing the degree bound on $A$.

## 7. Smith valuation and the remaining ideal

At the allowed prime, the actual $X_n$ has at most one nonunit Smith invariant. Its valuation is $f=v_p(F_n)$. After the unimodular Smith transformations, a primitive kernel modulo $p^h$ exists if and only if $h\le f$: the coordinates belonging to unit invariant factors vanish, and the remaining coordinate can be a unit precisely in that range. Combining this observation with Section 6 proves the maximum formula (17), with every exponent retained.

Full characteristic-zero column rank makes $f$ finite. The argument does not require choosing compatible roots $(\beta,\gamma)$ as $h$ varies.

Finally, the assertion about a rational constant in the four-polynomial ideal is valid: the field proof also works in characteristic zero and over its algebraic closure. A common algebraic root would reconstruct a forbidden nonzero characteristic-zero extremal triple. The Nullstellensatz, followed by rational linear descent of a finite certificate, gives a nonzero integer constant after denominators are cleared. This does not control that constant's prime factors or valuations.

The exact remaining task is therefore an integral elimination or valuation bound for this specific ideal. The four equations provide no such bound merely from their number or degree. No correction to the theorem is required.
