> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The constrained Machin space is not uniformly an extended Chebyshev system

Date: 2026-08-26

## Scope

A possible shortcut for the endpoint-matched diagonal Hermite--Padé family
would be to prove that its whole constrained coefficient space is an
extended Chebyshev space on $[0,1]$.  Its dimension is $3n+2$, while the
constructed remainder has a zero of order at least $3n+1$ at the origin.
If the Chebyshev assertion held, zero counting could potentially exclude a
further zero at $1$.

That proposed assertion is false already for $n=1$.  This note gives an
exact Wronskian obstruction.  It does **not** rule out a sign or
nonvanishing theorem for the particular one-dimensional Padé remainder,
nor does it rule out a different Chebyshev subspace for large $n$.

## 1. The constrained space at $n=1$

Put



$$
G(x)=16\arctan(x/5)-4\arctan(x/239).
$$



Parametrizing the endpoint condition $C(1)=B(1)$ as



$$
B=b+(x-1)\widetilde B,\qquad
 C=b+(x-1)\widetilde C
$$



shows that the constrained function space at $n=1$ has the basis



$$
f_1=1,\quad
 f_2=x,\quad
 f_3=e^x+G(x),\quad
 f_4=(x-1)e^x,\quad
 f_5=(x-1)G(x).
\tag{1}
$$



Let



$$
W(x)=\det\bigl(f_j^{(r)}(x)\bigr)_{
  \substack{0\le r\le4\\1\le j\le5}}.
\tag{2}
$$



The zero set of this full Wronskian is independent of the chosen basis:
changing a basis multiplies $W$ by one fixed nonzero determinant.

## 2. Exact opposite endpoint signs

Direct differentiation of (1), using



$$
\frac{d}{dx}\arctan(x/a)=\frac{a}{a^2+x^2},
$$



gives the exact rational value



$$
W(0)=
 -\frac{935059672726675656}
        {2912107693477515625}<0.
\tag{3}
$$



At the other endpoint the same exact determinant simplifies to



$$
W(1)=
 \frac{72e}{
  542800770374370512771595361}
 \left(
 50807650153010910313192727\,e
 -55199386641542198623868748
 \right).
\tag{4}
$$



The bracket in (4) is positive without any numerical assumption: its
second coefficient ratio is



$$
\frac{55199386641542198623868748}
      {50807650153010910313192727}<2<e.
\tag{5}
$$



Thus $W(1)>0$.  Since $W$ is continuous on $[0,1]$, equations
(3)--(4) imply that



$$
W(\xi)=0
$$



for some $\xi\in(0,1)$.

## 3. Consequence

The five-dimensional constrained space (1) is not an extended Chebyshev
space on $[0,1]$.  In particular, a proof of endpoint nonvanishing cannot
simply assert uniform extended-Chebyshev regularity of the entire
endpoint-constrained family for every $n$.

This obstruction is deliberately narrow.  Finite high-precision probes
show further full-Wronskian sign changes for several higher degrees, but
those computations are not used here.  A theorem about the actual Padé
line, a selected residue class, or a differently ordered/sign-regular
integral representation remains possible.
