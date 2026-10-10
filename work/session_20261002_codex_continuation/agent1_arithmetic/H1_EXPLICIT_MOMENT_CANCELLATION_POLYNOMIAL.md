> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Explicit h1 quotient constants for b4 and b5

Author result, continuing target L13, 2026-10-02. This is an exact dependency elimination from BOUNDARY_FACTORIAL_MOMENT_QUOTIENT.md. It uses a formal polynomial calculation over Q, not interpolation from finite residues. Full kappa remains in nu. No independent review is asserted.

For h=1 let alpha_s=[z^s](1-z+z²/2)^(-1), and, at an odd prime p>2b, put

    U=mu_0=sum_(t=0)^(p-1) alpha_t(-1)^t t!,
    W=mu_1=sum_(t=0)^(p-1) alpha_(t+1)(-1)^t t!,
    L=lambda_0=sum_(t=0)^(p-1) alpha_t(-1)^t t!
                                      Dcal_((-2-t) mod p),
    C=C_p=sum_(t=0)^(p-1)(-1)^t t!.

The h1 boundary n=-1 mod p, with k=v_p(n+1), has the previously proved all-depth normalized constants D_n/((n+1)²P_n²)=delta and V_n/((n+1)²P_n)=nu modulo p. For m_w=1 the constants are exactly

    b=4:
      det N_seed = 4(2W-1),
      delta = 340,
      nu = 4[85L-170U+(326-194C)W+12C-78];                 (1)

    b=5:
      det N_seed = 48(1-U),
      delta = 35712,
      nu = 384[93L+(86C-220)U+(310-62C)W-148C-28].         (2)

Neither nu depends on lambda_1 or chi=(-1|p), although the unsimplified quotient uses them. The denominator constant delta loses every prime-dependent moment. These eliminations are polynomial identities in the formal variables mu0,mu1,lambda0,lambda1,C for EACH chi=±1, so they do not require any unproved relation among the actual moment values.

## Exact reduction

The order2 moment recurrence gives

    mu_(-1)=2U-2W,
    mu_(-2)=2+2U-4W,
    mu_(-3)=2-4W,
    mu_(-4)=4-4U.

The scalar backward values are R_1=C,R_(j+1)=(1-R_j)/j. The lambda recurrence has forcing (-1)^(-c)(-c)!R_(2-c) at c<=0 and0 at c>0. Substitution into the h-dimensional block formulas and the two unit triangular solves of BOUNDARY_FACTORIAL_MOMENT_QUOTIENT.md yields the following low normalized reconstructed endpoint responses:

|b|X_0|X_1|nonzero high xbar_j|
|---:|---:|---:|---|
|4|4|-16|xbar_2=6,xbar_3=-4,xbar_4=-2|
|5|48|-144|xbar_3=-48,xbar_4=36,xbar_5=12|

All these entries are constants. For M=1, low weights are1,1, and the high quotient weight at j is((j-2)!)². Consequently

    delta_4=4²+(-16)²+6²+(-4)²+4(-2)²=340,
    delta_5=48²+(-144)²+(-48)²+4·36²+36·12²=35712.

The complete corrected contraction uses low Tc_0=(t0+Delta)/(n+1), Tc_1=t1/(n+1), and the high xbar_j tbar_j contractions. Its formal collection gives exactly(1),(2). This retains the correction already proved in the finite quotient formula; deleting Delta would change the calculation.

h1_symbolic_moment_quotient.py implements this rational polynomial substitution without a symbolic algebra dependency or numeric fitting. H1_SYMBOLIC_MOMENT_QUOTIENT.json retains every coefficient of Delta,delta,nu,X,Tc for both characters in each dimension. The formal arithmetic finds delta has just its constant monomial, and nu has exactly6 monomials for b4 and7 for b5; all other monomials cancel identically. Evaluation at the finite moment receipts is supporting implementation evidence only, separate from the formal identity.

## Actual arithmetic consequence and limits

Assume the full endpoint-digit unit hypothesis of the all-depth theorem. For b4, every p>8 except17 has delta a unit, since340=2²·5·17. For b5, every p>10 except31 has delta a unit, since35712=2^7·3²·31. Hence throughout the h1 disk, at ALL depths,

    v_p(D_n)=2v_p(n+1)

for these primes. If the respective bracket in(1) or(2) is nonzero modulo p, nu is a unit as well, and the complete-beta comparison proves the ACTUAL reduced denominator identity

    v_p(q_n)=2v_p(n!), for every normal n>=2p in this disk.

The exceptional constants and the explicit numerator hypersurface are distinct. On the latter, only v_p(V_n)>=2v_p(n+1)+1 is obtained at this precision; neither deeper loss nor shrinking primitive forms follows. The nonzero coefficient of L makes the surviving logarithmic moment dependence explicit. No C-only cancellation criterion, distribution theorem, prime supply, broader family atlas or conclusion about e+pi is inferred.
