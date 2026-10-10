> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Parent denominator-bound application for the exact7-dimensional gauge

Candidate proof for independent inspection. The exact parent structural
certificate constructs the homogenized gauge Y=(ell^T,1) with Y(n+1)=N(n)Y(n).
It verifies its inverse and gives the entry denominator lcms

  den(N)=(n+2)(n+3),  den(N^-1)=(n+1)^3(n+2).

These matrix-entry lcms alone are not universal solution bounds. However
the following ordinary shift-orbit argument appears to supply a sharper
solution denominator without an arbitrary ansatz.

For a rational vector solution let r be the leftmost pole on one integer
shift orbit. At n=r-1, Y(n+1) has that pole, while Y(n) is regular. Therefore
N must have a pole at r-1. Its only poles are -3 and-2, so r must be -2 or-1.
For the rightmost pole R on that orbit, rewrite Y(n)=N(n)^-1 Y(n+1): since
Y(n+1) is regular at n=R, N^-1 must have a pole at R. Its only poles are
-2 and-1. Thus no noninteger orbit can contain a pole, and every possible
pole of Y lies at -2 or-1. The argument also applies over the algebraic
closure to irreducible factors, with finite pole orbits of rational functions.

At n=-3, N has at most a simple pole and Y(n) is regular. Hence the pole
order of Y at -2 is at most1. At n=-2, N again has at most a simple pole;
Y(n) has order at most1 there, so Y at -1 has order at most2.
The proposed universal rational-solution denominator is therefore

  Dstar(n)=(n+1)^2(n+2).

The old failed degree6 test with n(n+1)(n+2) omitted a possible second
factor of n+1; it is not a complete rational-gauge obstruction. Check the
pole-order proof and all shift orientations. It applies to vectors, using
maximum pole order/minimum coordinate valuation; cancellations can only
improve the upper bound. A polynomial degree bound at infinity is still
required before a finite Dstar ansatz can decide all rational gauges.

This is an application of existing rational shift-system denominator methods
to the actual seeded coefficient matrix, not a new general algorithm. It
does not evaluate original contact gcds or the all-prime primitive error.
