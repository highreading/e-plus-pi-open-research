> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Proposed bounded contact-kernel compression

These are coordinator deductions for independent verification, not established inputs.
The target remains A2 turn23's unfinished universal 27-entry RC table.
Use p=29, n=2791829217, b=1395217, m=(n/p) mod p=7.

For a leading Newton polynomial h of degree at most 28, the contact operator
in A2 turn23 (8.2) may simplify at actual integer X, modulo p, to

L_s h(X)=(-1)^s choose(X,s) h(X-s), 1<=s<=28,

L_29 h(X)=-choose(X,29)h(X-29)
          +m h(X)choose(b+28-X,29).

In the second term only v=29 and i=0 should remain: choose(n,v)=0
mod p for 1<=v<=28, and choose(28+i,i)=0 mod p for 1<=i<=28.
Check this also for negative integer X-s and generalized binomials.

Consequently, h_A mod p^2 can be recovered by evaluating g_A and its
single contact correction at X=0..57 and taking finite differences.
The leading g_A is h0(X)=sum_(i0..28)(-1)^i i! choose(X,i) mod p.
All Newton coefficients at i>=29 are divisible by p.

For the complete boundary coefficients, F_r for r>=2 is divisible by
p^2 because b=-2 mod p^2. Thus c_h for h>=2 is divisible by p^2,
c0=1-2n mod p^2, and c1=-1 mod p^2. Since every d_s is divisible
by p, only c0,c1 contribute to a_Q mod p^3. Its formula should become

a_Q(X)=sum_(s1..58) d_s (-1)^(s+1)
       sum_(v1..s)(-1)^v choose(X,s-v)choose(n,v)
       [(1-2n)choose(b-X+s-1,v-1)+choose(b-X+s,v-1)] mod p^3.

The leading a_Q/p mod p is the retained expression
9[choose(b-X+28,28)+choose(b-X+29,28)].
One subsequent contact of this leading polynomial suffices for h_Q
mod p^3. This contact polynomial has degree at most28 after reduction;
verify its representation and the factor of p carefully.

All raw negative boundary coefficients must still be reconstructed
from every c_h through59 at precision p^4. The simplification concerns
the contact polynomial only; it does not discard the exterior boundary.

The fixed degree bound58 permits a Newton vector of length58, but
reconstructed kernels can still have Laurent powers0..58 and -60..58.
Carry factors and divisions in the universal table must be performed
with their actual valuations before reducing to p^2 or p.

This proposal does not establish coefficient periodicity, an RC table,
the original-index transfer, or any final primitive denominator bound.
