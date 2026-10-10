> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Child 3 current-stage closeout: factorial deficit local geometry

Original author deductions, not independently reviewed. Finish-only closeout of the accepted b=3,m=1 factorial B-Gram task. No prime scan, seed replay, modulo-121 replay, or other agent's task was performed.

The full primitive normalization is retained. Write u0+v0=c_H H with H primitive. Complete H to a unimodular matrix and put y=H w, z=J w. There are explicit integers a,b such that

    u0 w=a y+b z,
    v0 w=(c_H-a)y-b z,
    gcd(a,b,c_H)=1.

The FINAL evaluated gcd remains

    h0=gcd(D1,|a y+b z|,|c_H y|),
    Wcancel=c_H y/h0.

Both the endpoint and logarithmic terms remain in the row defining H.

For Q=Bprim, its actual discriminant is

    Disc(Q)=-4 det(Rbar^T Omega Rbar)/abar_B^2
           =-(4/abar_B^2) sum_(i<j)
                 omega_i^2 omega_j^2 det(r_i,r_j)^2<0.

The paper distinguishes good split primes, good nonsplit primes, discriminant primes, and 2. Real positivity does not imply nonsplitness modulo every prime.

In the coordinates y,z, the quadratic's z^2 coefficient is the retained positive resultant Rresultant=Q(-H1,H0). For every prime,

    min(v_p(Q(w)),v_p(y))<=v_p(Rresultant).

If v_p(y)>v_p(Rresultant), then v_p(Q(w)) equals the resultant valuation exactly. This is a prime-power restriction, not merely a support statement.

The main local reduction is at primes p not dividing c_H b. Any lost p-power then forces y divisible by p, z a unit, and v_p(h0)=0. Put

    f=2v_p(n!),
    A0=v_p(d0 L t0 k_R abar_B), E0=v_p(e shat).

If p also does not divide Rresultant,

    v_p(delta_F)=min(f,v_p(y),max(0,f+A0-E0)).

Equivalently, loss of k powers is precisely the primitive congruence H w=0 modulo p^k together with k<=f and f+A0-E0>=k. At regular row primes with resultant valuation r_p, the analogous criterion holds for k>r_p with f+A0+r_p-E0>=k. Shallower levels use the exact quadratic.

At other primes, the paper gives an exact formula retaining h0 and all contents. Testing k powers in Wcancel requires precision k+v_p(shat)+v_p(h0) in the original integer sum row. Good split quadratic roots admit simple lifting; no such assumption is made at discriminant primes or 2.

The structural limitation is precise: a nonsplit quadratic has unit value on primitive responses, but the external factor (n!)^2 remains in Dtilde. When A0>=E0, the entire local question becomes min(f,v_p(H w)). Thus anisotropy alone cannot exclude factorial-depth cancellation. This does not assert that an arbitrary locally allowed response is attained by the canonical sequence.

Unresolved: there is no proved uniform subfactorial bound for delta_F or for its remaining primitive linear congruence depths. The exceptional factor delta_exc=delta_reg delta_res is preserved separately, including its prior unresolved residual condition. Neither a total-deficit bound nor applicability of the 5/72 threshold is established. The actual e+pi problem remains OPEN.

Provenance and handoff: prior normalization papers and their reports were saved and fully read back in the supplied record. The new paper coherently records the bounded local completion; its derivations are author results without computational or independent verification claims. The paper also records a wording amendment: the prior k_C|Delta argument uses left multiplication M(adj(M)Drow)=Delta Drow. No original artifact was overwritten for that clarification.

Current-stage file index, all under work/session_20261001_astra/agent3/:

- CANONICAL_FACTORIAL_DEFICIT_LOCAL_GEOMETRY.md: current local elimination, discriminants, lifting precision and unresolved valuation condition.
- CANONICAL_FACTORIAL_DEFICIT_LOCAL_GEOMETRY_REPORT.md: this final handoff.
- CANONICAL_EXCEPTIONAL_DEFICIT_CONTENT.md and its _REPORT.md: preserved primitive normalization and separate exceptional-factor analysis.
- CANONICAL_OVERLAP_DEFICIT.md and its _REPORT.md: preserved total-deficit factorization and exact original gcds.
- CANONICAL_DENOMINATOR_OVERLAP.md, its _REPORT.md, and denominator_overlap_seed3.json: preserved earlier overlap evidence; not replayed.

No missing earlier current-task derivation is claimed to have been recovered beyond the supplied transcript. This paper/report records all new deductions made in this bounded completion. Following actual save/readback of these two files, Child 3 ends its current stage with no new assignments or research loop.
