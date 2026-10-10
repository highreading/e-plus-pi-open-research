> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform slope-10 determinant target and cyclic support reformulation

Date: 2026-08-28

This note deliberately separates two exact theorems from one conjectural
uniform lemma. Nothing in Sections 2--3 is presently an infinite proof of
determinant nonvanishing.

## 1. Setup

Let $m\geq1$, let $b\geq7$ be odd with $5\nmid b$, and put
$p=10m+b$.  In Sections 3--4, $p$ is assumed prime.  Retain



$$
F(y)=y^5-y,\qquad W(y)=(1-y)(1+y^2).
$$



Write $x=2m$. For the parity $\epsilon=m\bmod2$, let
$D_{b,\epsilon}(x)$ be the exact two-state determinant formed from
$W^{b-1}$ and $W^{b-2}$. This is the same determinant as in the
extended slope-10 certificate, with its polynomial variable changed from
$m$ to $x=2m$.

Define the universal product



$$
U_b(x)=
\prod_{\substack{1\leq j\leq b-2\\j\ {\rm odd}}}(x^2-j^2)
\prod_{\substack{b/2<j\leq b-4\\j\ {\rm odd}}}(x+j).               \tag{1.1}
$$



The case $b=3$ is an elementary lower-degree edge case and is not included
in the stable product (1.1).

## 2. Conjectural uniform 2-adic deflation law

Use the ray coordinate



$$
z=\frac{5x+b}{2},\qquad x=\frac{2z-b}{5},                           \tag{2.1}
$$



and put



$$
Q_{b,\epsilon}(z)=
\frac{D_{b,\epsilon}((2z-b)/5)}
     {2^{b-3}U_b((2z-b)/5)}.                                       \tag{2.2}
$$



The exact evidence supports the following uniform statement.

**Conjectural lemma.** For every admissible $b\geq7$, both quotients in
(2.2) belong to $\mathbb Z_{(2)}[z]$, and their reductions modulo 2 agree:



$$
\overline Q_{b,0}(z)=\overline Q_{b,1}(z)=
\begin{cases}
(1+z)^h,& b=4h+3,\\[2mm]
(1+z)^h+z^h,& b=4h+1.
\end{cases}                                                        \tag{2.3}
$$



In particular, the constant term in (2.3) is 1. If (2.3) is proved, then



$$
v_2\!\left(D_{b,\epsilon}(-b/5)\right)
=v_2\!\left(U_b(-b/5)\right)+b-3,                                  \tag{2.4}
$$



so every admissible formal ray constant is nonzero. Notice that
$U_b(-b/5)\ne0$ because $5\nmid b$. Thus (2.3), including only its
constant-term assertion, would prove the desired uniform determinant
nonvanishing theorem. It would not by itself prove actual mod-$p$ support
or close every ray: odd primes dividing the ray constant still require a
replay or a separate exclusion. For example, at $b=13$ and even parity,
$Q_{13,0}(0)=173/38364647023828125$, so the compatible prime $p=173$
survives this 2-adic test and must be checked separately.

### Exact finite audit

The companion script constructs every determinant over $\mathbb Q$,
performs exact polynomial division by (1.1), makes the affine substitution
(2.1), divides by $2^{b-3}$, and checks every coefficient denominator is
odd before reducing its numerator modulo 2.

It verifies (2.2)--(2.3), including exact divisibility by $U_b$, for both
parities and every admissible odd



$$
7\leq b\leq201.
$$



There are 79 intercepts and 158 parity rows. The ordered stream hash is



$$
\texttt{310283465b20fd739f867a9d186a82bcec3aa23e3bb02b7acb47924b7ba2e52b}.
$$



This is finite exact evidence, not an induction in $b$.

An independent verifier rebuilds the determinant from the residue recurrence
for both parities at $b=7,9,13,57,101$, checks the full cyclic identity and
reciprocity directly at four prime points, and reproduces the complete
$b\leq201$ output byte for byte.

## 3. Exact moment recurrence

Let



$$
\ell(P)=\operatorname {Res}_{y=1}P(y)F(y)^{-n}\,dy,
\qquad J_k(q)=\ell\!\left(y^kW(y)^q\right).
$$



Since $F=AW$, where $A=-y(y+1)$, and



$$
AW'=y-y^2+y^3+3y^4,
$$



the residue of $d(y^kW^qF^{1-n})$ gives the exact recurrence



$$
\boxed{
(k+3q+5-5n)J_{k+4}+(n-1-k)J_k
+q(J_{k+1}-J_{k+2}+J_{k+3})=0.}                                   \tag{3.1}
$$



For $q=b-2$, $n=4m+b$, and $p=10m+b$, its first coefficient is



$$
k+3q+5-5n=k-1-2p\equiv k-1\pmod p.                                \tag{3.2}
$$



The singular index is therefore $k=1$. Also



$$
J_0(q+1)=J_0(q)-J_1(q)+J_2(q)-J_3(q).
$$



Taking $k=0$ in (3.1) and using (3.2) gives



$$
\boxed{
J_0(q+1)=\frac{(q+n-1)J_0(q)-J_4(q)}q\pmod p.}                     \tag{3.3}
$$



Consequently the original adjacent pair vanishes simultaneously if and
only if



$$
J_0(q)=J_4(q)=0.                                                    \tag{3.4}
$$



Equivalently, the adjacent two-state determinant is
$q^{-1}\det(J_0,J_4)$. If (3.4) holds, the equations at $k=0,1$
also give



$$
J_1=0,\qquad J_2=J_3,                                              \tag{3.5}
$$



provided $n+q-2\not\equiv0\pmod p$. In fact this coefficient is always
nonzero here: it lies strictly between 0 and $2p$, while equality with
$p$ would require $b=6m+4$, impossible for odd $b$.

## 4. Exact cyclic coefficient product

Put $N=p-n=6m$ and



$$
\rho_j=\operatorname {Res}_{y=1}y^jF(y)^{-n}\,dy.
$$



Because the pole order of $y^kW^qF^{-n}$ is $n-q=4m+2<p$, the freshman's
dream in the local coordinate $y=1+u$ gives



$$
J_{k+p}=J_k\pmod p.                                                 \tag{4.1}
$$



In the cyclic Laurent ring
$\mathbb F_p[T,T^{-1}]/(T^p-1)$, the sparse Cartier formula implies



$$
4\sum_{j=0}^{p-1}\rho_jT^j
=T^{n-1-4N}(1-T^4)^N.                                              \tag{4.2}
$$



Indeed, the unique exponent selected by $a$ is
$j\equiv n-1-4a\pmod p$. Cyclic convolution by $W^q$, together with



$$
T^3W(T^{-1})=-W(T),
$$



then gives



$$
\boxed{
4\sum_{k=0}^{p-1}J_kT^k
=(-1)^qT^5W(T)^q(1-T^4)^N
\pmod{T^p-1}.}                                                      \tag{4.3}
$$



Here the monomial exponent reduces to 5 because



$$
n-1-4N-3q=5-2p.
$$



Since $q=b-2$ is odd, reciprocal symmetry in (4.3) yields



$$
\boxed{J_k=-J_{n+4-k}\pmod p,}                                     \tag{4.4}
$$



with indices read modulo $p$. Thus (3.4) also forces



$$
J_n=J_{n+3}=J_{n+4}=0,\qquad J_{n+1}=J_{n+2}=-J_2.                 \tag{4.5}
$$



Finally, in the local coordinate $U=T-1$, one has
$T^p-1=U^p$, and the right side of (4.3) is



$$
U^{6m+b-2}\times\text{a unit}.                                     \tag{4.6}
$$



Equations (3.4) and (4.3) give a factorization-free formulation of the
remaining support problem: prove that the $T^0$ and $T^4$ coefficients
of the explicit cyclic product (4.3) cannot both vanish.

## 5. Present boundary

The recurrence has a genuine one-dimensional boundary mode after imposing
(3.4)--(3.5), and individual coefficient zeros do occur. For example,
small exact scans find instances with $J_0=0$, instances with $J_4=0$,
and instances with $J_1=0$, though no simultaneous $J_0=J_4=0$.
Therefore neither a naive full-support claim nor multiplicity
$U^{6m+b-2}$ alone closes the argument.

The two viable uniform targets are now sharply isolated:

1. prove the 2-adic deflation congruence (2.3), likely by a confluent
   divided-difference or terminating-Pochhammer induction, and then control
   or replay the remaining odd numerator primes; or
2. prove the two-coefficient support theorem for (4.3), using the singular
   recurrence (3.1) and reciprocal boundary condition (4.4).

Until the first route is completed through its numerator-prime step, or the
second route is proved, the established infinite-ray theorem remains
the factor-and-replay result through $b=57$, and the larger computations
remain explicitly finite evidence.
