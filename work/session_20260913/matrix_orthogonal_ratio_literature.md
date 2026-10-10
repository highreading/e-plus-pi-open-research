> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Matrix orthogonal-polynomial literature and the actual scaled row recurrence

Date: 2026-09-13. Targeted primary-source check after the new
two-channel determinant and CD results. These references concern
the row recurrence; they do not prove the mixed high-cofactor bound.

## Primary results inspected

[Durán and Van Assche, Orthogonal matrix polynomials and higher
order recurrence relations](https://arxiv.org/pdf/math/9310220),
Section 2, establishes the passage from a symmetric higher-order
scalar recurrence to a matrix three-term recurrence and positive
matrix orthogonality. The proof explicitly groups the banded
matrix into blocks with invertible triangular off-diagonal blocks.
This is the relevant general framework for keeping both channels.

[Delvaux and Dette, Zeros and ratio asymptotics for matrix
orthogonal polynomials](https://arxiv.org/pdf/1108.5155), version 3,
Theorem 3.1, gives qualitative ratio asymptotics for continuously
varying limiting block coefficients, with invertible limiting
off-diagonal blocks. Its stated spectral domain excludes an
enclosing real interval and a finite exceptional set. Lemma 2.2
and the preceding definitions explicitly handle repeated algebraic
eigenvalues by their geometric multiplicities. The theorem does
not state a quantitative O(1/N) error or a bound for selected
evaluation minors. Theorem 3.2 concerns zero-counting measures.

The publisher records additionally identify Durán's 1999 ratio
paper as the earlier matrix Nevai result; no uninspected theorem
from it is used in this session.

## Independent specialization to the actual recurrence

Group the actual symmetric branch rows into

    P_j(x)=[R_(2j)(x); R_(2j+1)(x)].

The directly proved five-diagonal recurrence gives

    x P_j = Gamma_(2j+2) P_(j+1)
              +D_j P_j+Gamma_(2j)^T P_(j-1),

where D_j is the actual symmetric diagonal two-by-two block of K.
The initial matrix is G=[[1,0],[sqrt(3)/2,1]], invertible.
Right multiplication of every P_j by G^(-1) gives initial matrix
I without changing any recurrence coefficient or adjacent ratio.
The Gamma blocks are invertible; no scalar-branch positive-mass
pencil is being substituted for this two-channel recurrence.

Introduce an independent scaling parameter L and x=L^2 z. The
explicit coefficients a_k=k^2/sqrt(4k^2-1) give, as j/L -> s>0,

    Gamma_(2j+2)/L^2 -> s^2 I,
    D_j/L^2 -> -2s^2 I.

These are direct expansions of the actual entries. The limiting
off-diagonal matrix is invertible for s>0, and the limits extend
continuously to zero. The limiting quadratic symbol is

    det(s^2(w+w^(-1)-2)I-zI)
        =[s^2(w+w^(-1)-2)-z]^2.

Its double roots are semisimple away from the scalar branch points:
the whole two-dimensional channel space is the corresponding
nullspace. Thus the repeated scalar-I limit is not by itself a
failure of the multiplicity provision in the cited theorem.

At a scalar cut N=2j and a positive parameter x=cN^2, the
corresponding constant boundary Jacobi model has diagonal -1/2
and off-diagonal 1/4 after division by N^2. Solving its scalar
quadratic equation gives the candidate forward two-step factor

    lambda(c)=(sqrt(c)+sqrt(c+1))^2.

This last expression is an independent calculation for the local
constant model. Application to the actual finite matrices requires
a convergence argument. The ongoing direct resolvent calculation
aims to establish a uniform O(1/N) error on positive compact
c-intervals, stronger in this respect than the qualitative source
statement. The bounded spectral windows of the scaled finite row
compressions have already been proved in the CD note.

## What remains missing

Even a fully verified adjacent matrix ratio asymptotic would leave
the actual high-row, parity-selected multi-node remainder matrix
A_rem. Neither matrix orthogonality nor a scalar limiting ratio
proves its nonzero singular-value or maximal-cofactor estimates.
The useful next mathematical step is therefore a quantitative
transport estimate that retains both channels, followed by an
explicit analysis of the two distinct node-polynomial reductions.
No theorem about scalar total positivity, primitive denominators,
or irrationality is inferred from these primary references.
