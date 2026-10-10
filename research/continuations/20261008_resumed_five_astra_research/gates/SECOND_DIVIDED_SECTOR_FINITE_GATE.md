> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bounded new second-divided sector diagnostic

The old exact243-sector decomposition in 7 October A1turn7 Section4
and A1turn8 Section8 is ALREADY proved. Its pairing121/364, shortened
sector242, signs and block sizes are reused. The parent read those
sections before formulating this diagnostic. No old dense matrix or
old original-sector receipt is repeated.

Current A1turn6 instead has the NEW divided coefficient polynomial
(1-y)^(2chi) and index(P/3-1)/2. In its delta=chi-1 branch, write
chi=243*c and P/3=243*T. The SAME existing sector decomposition then
reduces its rank to two c-by-c Hankel forms and one c-by-(c-1)
rectangle. This is an application of the existing finite decomposition,
not a new general block theorem. The proposed rank is

    122*rank(H_c((T-1)/2))
      +119*rank(H_c((T-3)/2))
      +2*rank(H_(c,c-1)((T-3)/2)),

with coefficient polynomial(1-z)^(2c). The isolated example T=81,c=19
lies in the previously unclassified range of A1turn6; c=10 and28 are
small surrounding diagnostics. The actual original low congruence
c=1mod9 is preserved, but these are AUXILIARY scaled tuples, NOT original
j,n,h values. No infinite conclusion will be extrapolated from them.

Scoped archive/current-control retrieval found the older method but no
receipt for these new divided-sector parameters. Prior Nicklasson/
Han--Monsky primary results are reused at selected graded-map scope;
the fresh primary abstract gate is SECOND_RADICAL_BORDER_AND_AUDIT_GATE
_20261009.md. No new theorem from a search abstract is imported.

Bounded diagnostic: at T=81,c=10,19,28, compute only those three small
blocks with modular elimination and exact nullspace checks over F3,
and test their ACTUAL evaluation-at-1 observation. Maximum block28.
There is no dense243*c-1 matrix and no network/credential access.
