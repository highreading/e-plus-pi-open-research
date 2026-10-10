> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primitive minors and opposite endpoint signs do not bound companion conditioning

Status: main-agent paper lemma; independent review pending. This is an abstract counterexample to a general linear-algebra shortcut, not an example from the actual Hermite–Padé family.

Use the conditioning quantity in agent2/TWO_SCALAR_DETERMINANT_QUOTIENT.md. For a primitive antisymmetric minor matrix N, put kappa_j=e^T N f_j and

    C=min_{j:kappa_j!=0} sum_k |N_jk|/|kappa_j|.

For any integer m>=2 take the one-row high block

    R=(m,m-1,m).

It has full row rank and row content one. Its signed maximal minors have content one, and their antisymmetric matrix is

    N=[0,m,1-m; -m,0,m; m-1,-m,0].

The matrix is decomposable: its alternating form is exactly det[R;x;y]. Its column sums are (-1,0,1). Therefore kappa=(-1,0,1), and the two eligible row absolute sums both equal 2m-1. Consequently

    C=2m-1.

Thus primitive high rows, primitive maximal minors, and decomposability alone provide no upper bound depending only on dimension.

The opposite-sign endpoint condition does not repair this general implication. Choose the abstract tail rows a=f_0 and c=f_2. Then

    z0=B(e,a)=-1, z1=B(e,c)=1,
    B(a,c)=1-m.

For any fixed positive A0,A1, the endpoint combination d=A1 z1-A0 z0=A0+A1 has projective separation Delta=1. Nevertheless |B(a,c)/d|=(m-1)/(A0+A1) is unbounded.

These arbitrary tail rows are not asserted to be the factorial tails of the actual reference polynomials. The example therefore rules out only a companion estimate based solely on primitivity, rank, decomposability, and opposite signs. It does not refute an estimate using the actual derivative recurrence or factorial-tail structure.

A productive continuation must use those additional actual-family properties to bound C, or estimate the complete companion quotient directly. No statement about rationality of e+pi follows.
