> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# D1910：hp_b2_endpoint_attempt.md

Attribution：/root/organization_evidence

Mathematical verdict：**valid eventual b=2 theorems and local prime exclusion; the total denominator remains unresolved**。

Original path：`work/session_20260913/hp_b2_endpoint_attempt.md`

Original SHA-256: `ba2b0e2c74e72892488ae9fea6a1f3b7483afa5e9f4bb622ddbe317af907cd05`

Actual reading: complete source textL1–L522，16114characters，16129bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 33。

inherited primaryscope：All proof sections including covariance domination and prime-family argument; historical small-degree fractions are not independently rerun here

Specific source-text basis：

- L25–45, 95–148: the signs in the two-row cross product and Y=-S(U,V) are correct.
- L155–231: the covariance lemma has a uniform-in-m O(n^-2) tail majorant; it does not interchange an infinite sum using only pointwise convergence for fixed m.
- L321–381: eventual Y<0 is under the normalization B(0)=1. The positive constant for R/Y is (sqrt(2)-1)^2; the sign of Y is not the sign of the error quotient.
- L383–424: the minimum endpoint q and complete error are retained. Positive Y at n=2,3 does not refute eventual negativity.
- L446–521: for each odd prime p, the local statement p does not divide q at n=p-1 is valid. It is not an all-n total-height theorem.

Rederivation and valid usable conclusions：

Set Delta=ell1-ell0, Theta=ell2-ell1, and S(P,Q)=Theta(P)Delta(Q)-Delta(P)Theta(Q). Expanding det(a,1+t,1) gives Y=-S(U,V); expanding det(a,1+t,w) gives R=S(U,W)+det(a,t,w). Primary review 33 checked uniform domination for the covariance. Consequently, S(U,V)~- (dV/n)U(0)V(0)e^(-2sqrt(2))/(n!)^2; the analogous formula for the other S uses dW. The third determinant has an additional factorial factor and vanishes asymptotically. Therefore R/Y~-(dW/dV)W(0)/V(0). The identities dW/dV=sqrt(2)-1 and (1+lambda_-/lambda_+)/2=sqrt(2)-1 yield the complete quotient constant (sqrt(2)-1)^2.

The fixed-half-plane root/resolvent proof and local boundary kernel confirmed in primary review 33 are reused. The complex-segment moment functional L is not assumed to be a positive measure; its h_k alternate in sign. Positivity in the source concerns the transformed symbol/covariance and actual eventual quotient. It must not be confused with raw even/odd objects or a different positive-energy metric.

Conditions of use and limits relative to the main goal：

- The conclusion holds for sufficiently large n; the source supplies no explicit uniform threshold.
- The fact that p does not divide q_(p-1) removes only one prime factor. Other primes and every prime-power/gcd cost remain relevant.
- The primitive error still equals q|R/Y| exactly. The stated analytic constant improvement does not control log q.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.
