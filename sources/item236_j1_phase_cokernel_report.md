> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 236 — an all-$h$ cokernel proof of the phase-residual identity

Date: 2026-08-31

## 1. Scope and verdict

Put



$$
r=2h,\qquad
 A=2r+4s-1,\quad B=r+1,\quad C=-(r+8s),             \tag{1.1}
$$



and retain the polynomial antidifference operator used in Items 229 and
231,



$$
\mathcal L_sU(j)=-(2s+j)U(j+1)-jU(j).               \tag{1.2}
$$



Item 229's lower polynomial and Item 231's upper polynomial are



$$
\begin{aligned}
 P^-_{h,s}(j)={}&A{r+2s+4-2j\choose r}
                +B{r+2s+3-2j\choose r}
                +C{r+2s+2-2j\choose r},             \tag{1.3}\\
 P^+_{h,s}(j)={}&C{2j-r-1\choose r}
                +B{2j-r\choose r}
                +A{2j-r+1\choose r}.                \tag{1.4}
\end{aligned}
$$



Write their unique reductions as



$$
P^-_{h,s}=c^-_h(s)+\mathcal L_sU^-_{h,s},\qquad
 P^+_{h,s}=c^+_h(s)+\mathcal L_sU^+_{h,s},
 \quad \deg_jU^\pm_{h,s}\leq r-1.                   \tag{1.5}
$$



The exact result of this item is



$$
\boxed{c^+_h(s_*)=c^-_h(s_*)\quad\hbox{for every }h\geq1,\qquad
        s_*=-{4h+3\over6}.}                         \tag{1.6}
$$



Thus the equality observed only through $h\leq20$ in Item 231 is now
**PROVED for all $h$**.  The proof is a coefficientwise cokernel
calculation; it does not evaluate, or assume convergence of, an infinite
binomial sum.

The identity synchronizes the two Gosper residuals but does not force their
common value to vanish modulo an actual row prime.  No all-$h$ relation
between that common value and Item 222's phase eliminant is proved here.
Consequently the new unconditional Route-1 rate and divisibility exponent
are both zero.

## 2. The normalized coefficientwise functional

For $n\geq0$, let ${n\brace k}$ be a Stirling number of the second kind
and let $x^{\underline k}=x(x-1)\cdots(x-k+1)$.  Define the linear
functional $\Phi_s:\mathbb Q(s)[j]\to\mathbb Q(s)$ by



$$
\boxed{\displaystyle
 \Phi_s(j^n)=\sum_{k=0}^{n}{n\brace k}
              {(-2s)^{\underline k}\over2^k}.}       \tag{2.1}
$$



In particular,



$$
\Phi_s(1)=1.                                        \tag{2.2}
$$



There is a useful finite-differential interpretation.  Put



$$
F_s(z)=\left({2\over1+z}\right)^{2s},\qquad
 \theta=z{d\over dz}.                               \tag{2.3}
$$



The right side is expanded only at $z=1$, where it has constant term one.
Then



$$
\Phi_s(P)=\left.P(\theta)F_s(z)\right|_{z=1}.       \tag{2.4}
$$



Indeed $\theta^{\underline k}=z^k d^k/dz^k$, so (2.4) gives
$(-2s)^{\underline k}/2^k$ on $j^{\underline k}$, which is exactly
(2.1).  Formula (2.4) is a finite number of formal derivatives for every
polynomial $P$; it is not an analytic summation prescription.

## 3. Exact cokernel theorem

Write



$$
m_k=\Phi_s(j^{\underline k})
     ={(-2s)^{\underline k}\over2^k}.                \tag{3.1}
$$



It is enough to test $\mathcal L_s$ on the falling-power basis.  For
$U(j)=j^{\underline d}$, direct polynomial algebra gives



$$
\begin{aligned}
 -\mathcal L_s(j^{\underline d})
  ={}&2j^{\underline{d+1}}+(3d+2s)j^{\underline d}\\
    &+d(d-1+2s)j^{\underline{d-1}},                 \tag{3.2}
\end{aligned}
$$



where the last term is absent for $d=0$.  The falling moments satisfy,
as polynomial identities in $s$,



$$
2m_{d+1}=(-2s-d)m_d,\qquad
 d(d-1+2s)m_{d-1}=-2dm_d.                           \tag{3.3}
$$



Substitution of (3.3) into (3.2) makes the three coefficients sum to zero.
By linearity,



$$
\boxed{\Phi_s(\mathcal L_sU)=0}  \tag{3.4}
$$



for every polynomial $U$.  This is a completely finite proof.

For comparison with the Abel/Gosper language, the expansion of
$(1+z)^{-2s}$ at $z=0$ has coefficients



$$
t_j=(-1)^j{2s+j-1\choose j},\qquad
 (j+1)t_{j+1}=-(2s+j)t_j,                            \tag{3.5}
$$



and coefficientwise application of (3.5) gives the formal differential
identity



$$
\sum_{j\geq0}t_j\mathcal L_sU(j)z^j
 =\left(z^{-1}-1\right)\theta
       \bigl(U(\theta)(1+z)^{-2s}\bigr).             \tag{3.6}
$$



The apparent $z^{-1}$ is harmless because the differentiated expression
has zero constant term.  The right side has a factor $1-z$ and is regular
at $z=1$, which is the usual normalized-Abel mnemonic for (3.4).  No
value of the infinite series at $z=1$ is used: the proof of (3.4) is the
finite falling-basis calculation (3.1)--(3.3), while (3.6) is only an
equivalent formal differential identity.

If $U(j)=u_dj^d+\cdots$, then



$$
\mathcal L_sU(j)=-2u_dj^{d+1}+O(j^d).               \tag{3.7}
$$



Hence $\mathcal L_s$ is injective from polynomials of degree at most
$r-1$ into polynomials of degree at most $r$, and its image has
dimension $r$.  By (2.2)--(3.3), the constant polynomial $1$ is not in
that image.  Therefore



$$
\mathbb Q(s)[j]_{\leq r}
   =\mathbb Q(s)\,1\ \oplus\
     \mathcal L_s\bigl(\mathbb Q(s)[j]_{\leq r-1}\bigr),     \tag{3.8}
$$



and the scalar in the unique decomposition $P=c+\mathcal L_sU$ is



$$
\boxed{c=\Phi_s(P).}         \tag{3.9}
$$



This proves the claimed cokernel statement over characteristic zero for
every specialization of $s$.

## 4. Positive/negative binomial reflection

For formal $q$ near one, the falling-power definition (2.1) gives



$$
\Phi_s(q^j)=\left({2\over1+q}\right)^{2s}.          \tag{4.1}
$$



Only finitely many powers of $q-1$ are needed in every coefficient below.
Using
${\alpha+2j\choose r}=[u^r](1+u)^{\alpha+2j}$, equation (4.1) yields



$$
\Phi_s{\alpha+2j\choose r}
 =[u^r](1+u)^\alpha
   \left({2\over1+(1+u)^2}\right)^{2s}.             \tag{4.2}
$$



Likewise,



$$
\begin{aligned}
 \Phi_s{\alpha-2j\choose r}
 &=[u^r](1+u)^\alpha
   \left({2\over1+(1+u)^{-2}}\right)^{2s}\\
 &=[u^r](1+u)^{\alpha+4s}
   \left({2\over1+(1+u)^2}\right)^{2s}\\
 &=\Phi_s{\alpha+4s+2j\choose r}.                  \tag{4.3}
\end{aligned}
$$



All generalized powers in (4.2)--(4.3) are formal series at $u=0$, and
only the coefficient of $u^r$ is taken.  Thus (4.3) is an exact
coefficient identity, with no convergence hypothesis.

## 5. Phase specialization and proof of (1.6)

Apply (4.3) to the three terms of (1.3).  Their reflected upper arguments
are



$$
r+6s+4+2j,\qquad r+6s+3+2j,\qquad r+6s+2+2j.       \tag{5.1}
$$



At the row phase



$$
2r+6s_*+3=0,                \tag{5.2}
$$



these become, respectively,



$$
2j-r+1,\qquad2j-r,\qquad2j-r-1.                    \tag{5.3}
$$



The coefficients remain $A,B,C$, so (4.3) and (1.3)--(1.4) give



$$
\Phi_{s_*}(P^-_{h,s_*})
                         =\Phi_{s_*}(P^+_{h,s_*}).   \tag{5.4}
$$



Combining (5.4) with (3.9) proves (1.6) for every $h\geq1$.  Although
actual Item 222 phase rows use $3\nmid h$, the characteristic-zero
identity itself also holds when $3\mid h$.

## 6. Exact consequence and remaining obstruction

The theorem identifies Item 229's lower residual with Item 231's upper
residual at the same row phase.  It therefore removes the possibility that
the two incomplete-binomial reductions carry independent residual scalars.
It does **not** show that their common scalar is zero, a unit, or controlled
by the Item 222 eliminant.

In particular, this package proves neither



$$
c_h(s_*)=\mathcal R_hE_h^*                         \tag{6.1}
$$



for an all-$h$ localized factor $\mathcal R_h$, nor a symbolic
unit-localized gcd/resultant theorem for the endpoint scalar $K_h$ and
$E_h^*$.  The finite patterns recorded in Items 229 and 231 are not used
to infer either statement.  Those questions remain **OPEN**.

Accordingly:

- **PROVED:** the coefficientwise cokernel formula (2.1)--(3.9), the
  binomial reflection (4.3), and the all-$h$ phase identity (1.6);
- **EXACT REPLAY:** the functional/reflection identity through $h\leq80$
  and independent lower/upper Gosper-system solutions through $h\leq12$;
- **OPEN:** an all-$h$ relation with $E_h^*$, an all-prime exclusion or
  weighted exceptional-prime theorem, and any positive Route-1 rate.

The new unconditional linear log-rate is $0$, and the new divisibility
exponent is $0$.

## 7. Reproducibility

The deterministic checker uses only Python 3.11+ standard-library exact
integer and `Fraction` arithmetic.  The canonical and replay JSON files are
byte-identical.  The portable manifest uses archive-relative `sources/`,
`scripts/`, `results/`, and `manifests/` paths and pins the Item 222, 229,
and corrected Item 231 dependencies.
