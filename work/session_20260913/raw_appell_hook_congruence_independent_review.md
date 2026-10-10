> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit: actual Appell hook normalization and congruence

Date: 2026-09-13. Reviewer: audit_results. **FULL PASS.**
Reviewed source: raw_appell_hook_normalization_congruence.md, all sections.
No mathematical correction was needed. This is an independent normalization
and proof audit; no new canonical degree, prime, or root scan was performed.

## 1. Primary theorem and the universal strength actually needed

I checked Theorem 4.1, Proposition 4.3, and the proof of Theorem 5.8 of
Bonneux, Hamaker, Stembridge and Stevens, *Wronskian Appell polynomials and
symmetric functions*. The proof explicitly uses the fact that the augmented
Schur function $H(\lambda)s_\lambda$ has integer coefficients in the
power sums. Thus the source is entitled to use universal coefficient
integrality, rather than just integrality of individual specialized Appell
polynomials. The leading $p_1^{|\lambda|}$ coefficient is one.
[Primary paper, arXiv:1812.01864v2](https://arxiv.org/pdf/1812.01864v2).

There is also a direct independent check of precisely this integer
coefficient assertion. Frobenius's formula and the hook dimension formula
give the coefficient at cycle type $\mu$ as


$$
\frac{|\mathcal C_\mu|\chi^\lambda(\mu)}{f^\lambda}.
$$


The corresponding class sum is an integral matrix in the regular
representation, so every scalar by which it acts on an irreducible
constituent is an algebraic integer. The displayed scalar is rational
because symmetric-group characters are integers; hence it is an integer.
For the identity cycle type it is one. This checks both the scale and the
leading coefficient used in the congruence.

## 2. Complete-function convention, shape, and factorial ledger

The background integer $n$ is fixed throughout the Appell sequence
$\mathcal A_k(x)=k![t^k]e^{xt}(1+t^2)^n$. These polynomials are monic
and satisfy $\mathcal A'_k=k\mathcal A_{k-1}$.

Taking the logarithm of the **complete-function** generating series gives


$$
\varphi(p_1)=x,\qquad
 \varphi(p_{2j})=2n(-1)^{j+1},\qquad
 \varphi(p_{2j+1})=0\quad(j\ge1).
$$


In particular, $\varphi(p_2)=2n$, not $-2n$.
Transposing $A_n=(a_{n+i-j})_{0\le i,j\le n}$ produces the ordinary
Jacobi--Trudi matrix $h_{n-i+j}$. Its partition is
$(n^{n+1})$; the corner partition is $(n^n)$.
No row permutation or sign occurs. An elementary-function convention
would conjugate the first partition and change the even power-sum signs.
The source keeps these two conventions separate.

Direct multiplication of the rectangular hook lengths gives


$$
H_D=\prod_{j=0}^{n}\frac{(n+j)!}{j!},\qquad
 H_B=\prod_{j=0}^{n-1}\frac{(n+j)!}{j!},\qquad
 \frac{H_D}{H_B}=\frac{(2n)!}{n!}=R.
$$


Deleting row and column zero from $A_n$, then shifting both surviving
indices by one, gives exactly the displayed $B_n$ matrix. Its cofactor
sign is positive, so the inverse corner is $v_0=B_n/D_n$.
There are no hidden factorial-scaled rows in either determinant.

## 3. Polynomial congruence and full local depth

In each nonleading power-sum monomial, some part has size at least two.
An odd part of size at least three makes the specialization zero; an even
part contributes a multiple of $2n$. Thus the universal theorem proves
the genuine polynomial statements


$$
M_D:=H_DD_n\in\mathbb Z[x],\qquad
 M_D\equiv x^{n(n+1)}\pmod{2n},
$$




$$
M_B:=H_BB_n\in\mathbb Z[x],\qquad
 M_B\equiv x^{n^2}\pmod{2n}.
$$


Both are monic. This inference would not follow merely from integrality
at a collection of background parameters, which is why Section 1 matters.

At one, both normalized values are integers congruent to one modulo
$2n$. In particular they are nonzero, and are units at every prime
$p\mid2n$. It follows exactly that


$$
v_p(D_n(1))=-v_p(H_D),\qquad
 v_p(B_n(1))=-v_p(H_B).
$$


The ratio direction is


$$
\frac{v_0}{R}=\frac{M_B(1)}{M_D(1)}.
$$


Subtracting one, with the denominator a $p$-unit, proves


$$
\frac{v_0}{R}\in1+2n\mathbb Z_{(p)},\qquad
 v_p(v_0)=v_p(R).
$$


This retains depth $v_p(2n)$, not only congruence modulo $p$. It is a
lower bound on the depth of the *difference from one*, not an assertion
that the difference has exactly this valuation.

The simultaneous localization statement is also correct: the reduced
denominators of both normalized ratios are coprime to $2n$.
For any integer $x$ coprime to $2n$, the same reasoning proves
$v_0(x)/R\equiv x^{-n}$ in that ring. Invertibility follows there as
well from the normalized determinant congruence.

## 4. Original dual-polynomial interface

I checked the source's equation against the algebraic moment and
Hankel-to-Toeplitz identities in
raw_joint_dual_hankel_and_even_root_product.md:


$$
A_n(1)\mathbf q_n=n!V_n(1)e_0,\qquad
 q_n(0)=[t^n]U_n=(2n)!V_{n,\mathrm{lead}}.
$$


Although the accretivity discussion in that earlier note is even-degree,
these two displayed identities are algebraic in every degree. The
coefficient vector $\mathbf q_n$ is not the primitive endpoint
denominator.

The inverse-corner equation is


$$
(2n)!V_{n,\mathrm{lead}}=n!V_n(1)v_0.
$$


Consequently


$$
\boxed{\frac{V_n(1)}{V_{n,\mathrm{lead}}}
 =\frac{R}{v_0}=\frac{M_D(1)}{M_B(1)}
 \in1+2n\mathbb Z_{(p)}\quad(p\mid2n).}
$$


All divisions are valid. They follow either from the previously audited
added-column nonvanishing theorem or directly here: the original
cofactor polynomial is nonzero, so invertibility of $A_n(1)$ forces
$V_n(1)\ne0$; the nonzero inverse corner then forces
$V_{n,\mathrm{lead}}\ne0$.
There is no parity restriction and no condition $3m<p$.

The already frozen $n=1$ formulas are
$M_D=x^2-2,\ M_B=x$, so at one the endpoint ratio is $-1$,
as required modulo two. The previously saved $n=2$ data have
$V_2(t)=49t^2-64t+940$, hence $V_2(1)/V_{2,\mathrm{lead}}=925/49$.
Here $H_B=12,\ H_D=144$, and $M_B(1)=49,\ M_D(1)=925$;
this checks the ratio direction and the modulus four using existing
controls only.

## 5. Scope of the passing result

The new theorem supplies an all-index exact local normalization of the
actual scalar inverse corner and the original $V$-endpoint ratio.
It also supplies an independent all-index proof that the full Toeplitz
determinant and its first corner are nonzero.

It does **not** bound the primitive endpoint denominator $q_n$, the
distinct evaluated numerator $N_n$, the integer $Z_n$, or
$\gcd(N_n,Z_n)$. In particular, no fixed-prime primitive-denominator
growth assertion is justified by this corner congruence alone.
A separate exact hook-normalized expression for the relevant evaluated
cofactors would be needed to obtain that arithmetic bridge.

