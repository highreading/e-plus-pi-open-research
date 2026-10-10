> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinator proposal: integral divided contact and an admissible even branch

Status: elementary integral strengthening and a new proof obligation. Audit
against prior sources before claiming novelty. No denominator or error theorem
for the proposed branch is asserted.

For phi=1-z+z^2/2, the coefficient a_s(n) has dyadic denominator dividing
2^floor(s/2): expand phi^n by choosing linear and quadratic terms. Since
(n+i)_s is divisible by s! and v2(s!)>=floor(s/2),

 a_s(n)(n+i)_s is an INTEGER for every s,n,i in the defining finite range.

Thus the divided contact matrix Ntilde in A5 is an integer matrix. In the
nonconstant identity

 a_s(n)(n+i)_s = n (s-1)! binom(n+i,s)
                             [z^(s-1)]phi' phi^(n-1),

phi'=-1+z is integral and the coefficient's dyadic denominator divides
2^floor((s-1)/2), canceled by (s-1)!. Therefore the entire correction C
is integer and Ntilde=B(n)+nC over Z, rather than only Z[1/2]. In particular
Ntilde is a unit at EVERY prime dividing n, including 2 when n is even.

For c_r=[z^r]phi^-1, the recurrence c_r=c_(r-1)-c_(r-2)/2 shows its dyadic
denominator divides 2^floor(r/2). For m>=r>=1, m!/r is an integer whose
2-valuation is at least v2((r-1)!)>=floor((r-1)/2). Hence

 m! [z^m](F/(1-z)) = sum_(r=1)^m 2(m!/r)c_(r-1)

is an EVEN integer. Both complete forcing columns h^e,h^F are therefore
integral, with all logarithmic terms retained. Check the finite support
indices in this claim; no negative-factorial continuation is intended.

The existing odd branch n=2001*3^a,b=3^a has an exact actual-q 3-part but
uncontrolled 3-prime-to part. A proposed complementary SAME-center family is

 n=4002*3^a, b=3^a, a>=1, m_w=1, ell=n+2,
 Omega=diag((ell!/(ell-j)!)^2), c=b/n=1/4002.

This keeps proportional growth inside the inherited c<0.001 error domain.
Verify that theorem's parity and endpoint conditions before importing it.
The integral contact lemma makes Ntilde a unit at BOTH 2 and3 for every
such n, regardless of dimension. This avoids importing a fixed-b transfer.

The first task is a rigorous 3-adic extension of the new split-product
cross-norm proof from coefficient2001 to4002, with all unit changes and
base-3 digit sums tracked. The second, harder task is the ACTUAL final
2-adic quotient

 vp2(q)=max(0,vp2(lambda)+vp2(D)-vp2(C)),
 lambda=(n!)^2/2^n, D=z^T Omega z, C=z^T Omega v.

Track the full common 2-content of the weighted P-column, its norm, and
the FULL weighted Q-column after endpoint cancellation. Merely knowing
Ntilde is a local unit or that residual rho has a factorial factor gives
no upper bound on vp2(C), and hence no useful lower bound on vp2(q).
Use exact tail subtraction with its logarithmic forcing at the required
precision, not an exp-only replacement. A proved aggregate denominator
lower rate may exclude this even subfamily; an upper rate below the full
signed error rate could instead establish primitive shrinking. Neither
is established here. Do not assign hypothetical first-lift values as facts.
