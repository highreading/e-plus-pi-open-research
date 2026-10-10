> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primary Hahn-weight gate and the actual finite cutoff

The coordinator checked NIST DLMF18.19 Table18.19.1, including the allowed
negative parameter range, weight and squared norm. Taking both parameters
alpha=beta=-N-1 makes the Hahn weight a common sign times binom(N,j)^2.
This is classical full-support orthogonality on0..N, not a new norm formula.

- https://dlmf.nist.gov/18.19

The coordinator also checked DLMF18.22.10--11. With these parameters the
difference coefficients are A(j)=(j-N)^2 and C(j)=j^2. The binomial-square
weight satisfies w_j A(j)=w_(j+1) C(j+1), giving classical discrete Green
machinery. The original cutoff is b<N, so its upper return cannot be erased.
No claim is made that the actual contact states are Hahn eigenfunctions or
that Hahn changes of basis preserve29-integral contents.

- https://dlmf.nist.gov/18.22

The archive already contains the complete source recurrence and three-column
reduction in October5 A2turn6; those are explicitly recovered and reused.
A focused search found no evaluated Hahn/finite-Green reduction giving the
original paid norm or its growing valuation. This does not prove exhaustive
absence of literature. Known orthogonal-polynomial machinery is background;
the open research target is its exact complete-source application with the
original finite return, paid lattice and same-index all-prime budget.
