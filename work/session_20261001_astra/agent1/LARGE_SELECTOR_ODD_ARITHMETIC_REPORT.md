> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-selector odd arithmetic report

New author deductions; offline, without scans or independent review. The main draft's rational representation and nonzero U are retained author inputs. Its dyadic law is not repeated.

For the allocated n=4k and m, let N=2n+4m, J=N-n, and take any odd prime max(n,N/2)<p<=J. Set s=J-p and R=N-p. Then n<p, N<2p, and v_p(J!)=1.

Normalize the COMPLETE center over Q as

 c=W/(n!J!U), W=Vexp+n!J!L,
 L=calL((K-U)/(t-1)).

The unique possible moment pole is mu_(p-1), with p mu_(p-1)=2chi modulo p, chi=(-1)^((p-1)/2). Retaining it gives the exact all-index residue

 W=s! H_p(B) mod p,
 H_p(B)=sum_{r=n}^R b_(p+r)[D_r-2chi r!]/(r-n)!.

The report's full derivation gives both a Frobenius extraction from B and a shorter reverse-product expression involving only s+1 coefficients. Hence the remaining scalar condition is explicit, with every factorial denominator below p.

If H_p(B) is nonzero, the ACTUAL reduced denominator satisfies

 v_p(q)=1+v_p(U).

If U is a p-unit, the gate is complete: H_p(B)=0 means v_p(q)=0; otherwise v_p(q)=1. The endpoint-unit condition is itself given by an explicit coefficient sum and is not assumed universally.

When both U and the residue vanish modulo p, the unresolved depth is exactly

 W=Vexp+n!(J!/p)(pL).

Both terms are p-integral. Formula v_p(q)=max(0,1+v_p(U)-v_p(W)) retains their possible cancellation. Higher lifts must restore all moment terms and falling-factorial terms omitted at first order.

No uniform unit claim, old Toeplitz window, prime scan, or asymptotic denominator product is asserted. Earlier files are preserved. Full derivation: work/session_20261001_astra/agent1/LARGE_SELECTOR_ODD_ARITHMETIC.md.
