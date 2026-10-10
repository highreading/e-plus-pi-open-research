> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinator proof proposal: exact doubled factorial endpoint at 3

2026-10-04. Ongoing research, for independent paper audit. No claim about
the whole rational center denominator or irrationality of e+pi.

Prior-work gate: the archive already uses orthogonality to double DYADIC
endpoint depth (WEIGHTED_REGULAR_ENDPOINT_DYADIC_RATE, Section3), and
Pascal Schur complements are classical. Reuse those ideas explicitly.
Bounded searches did not locate this exact odd-prime normalized unit theorem.
The elementary geometric identity below is a known identity, not new general
mathematics. Its application to the actual 3-adic Schur numerator is the target.

## Existing exact setup

Let n=3M+2, M>=1, N=n-1=3M+1 and L=N-1=3M.
The regular family n=4^j+1 is contained in this domain. Put delta=y-1,
phi_d=(y+1)delta^d/d!, rho=mu-evaluation_-1,
mu(F)=integral_0^infty exp(-t)F((1-t)^2)dt.
The normalized moments t_s=mu(phi_s) are integral at3 (indeed integers),
and t_s=2mod3, from the supplied factorial-normalized moment identities.
The nonconstant Gram is G_de=binom(d+e,d)e_(d+e), e_s=-smod3.

Let E=G_(0<=d,e<L), and chi_i=phi_i-sum_(e<L) eta^(i)_e phi_e,
where eta^(i)=E^-1(G_ei)_(e<L). E is a 3-adic unit by the established
triadic Pascal factorization. Consequently every eta^(i)_e is in Z3 and
rho(chi_i phi_e)=mu(chi_i phi_e)=0 for e<L.
Since all phi_e and chi_i vanish at -1, every constant/nonconstant pairing
in this argument is an actual mu pairing, with no unretained negative mass.

In the prior Schur notation,
b=mu(chi_L), xi_const=mu(chi_N),
c=mu(chi_L^2), xi_last=mu(chi_L chi_N).
The established first lift gives v3(c)=1, xi_last=2mod3, and
delta_S=c-b^2/a has depth1, while a is a unit. These identities are to be
checked against the original partition, not assumed from a changed basis.

## Geometric remainder provides a full factorial, not a coarse path bound

The exact polynomial identity is

  1 = (y+1)/2 sum_(d=0)^(L-1) (-delta/2)^d + (-delta/2)^L.

The first summand belongs to span(phi_0,...,phi_(L-1)), with coefficients
(-1)^d d!/2^(d+1), all 3-integral. Orthogonality therefore gives, for i=L,N,

  mu(chi_i)=(-2)^(-L) mu(delta^L chi_i).

For EVERY e>=0,

  mu(delta^L phi_e) = ((L+e)!/e!) t_(L+e).

It is divisible by L! in Z3 because the quotient by L! is
binom(L+e,e)t_(L+e), an integer. This also holds for the e=i leading term
and all eliminated e<L. Thus

  b, xi_const are in L! Z3.                              (1)

This is an all-depth exact identity. No inverse-decay estimate is needed.

## The normalized b unit is exactly an ordinary Pascal Schur complement

Reduce the quotient b/L! modulo3. The projection of phi_L on E satisfies

  Ebar=B_M tensor A,
  A=[[0,2,1],[2,2,0],[1,0,0]],
  (G_eL)bar=k tensor (0,2,1)^T = k tensor A e0,
  k_q=binom(M+q,q), 0<=q<M.

Hence eta^(L)bar=(B_M^-1 k) tensor e0. Only indices e=3q survive.
Lucas gives

  binom(2L,L)=binom(2M,M)mod3,
  binom(L+3q,3q)=k_q mod3.

Using t_(L+e)=2mod3, (1) gives

  b/L! = 2(-2)^(-L)[binom(2M,M)-k^T B_M^-1 k]mod3.

The bracket is EXACTLY 1 over the integers: B_(M+1)=P_(M+1)P_(M+1)^T
has determinant1 and its leading M block B_M also has determinant1, so its
last Schur complement equals1. Therefore

  b/L! =2mod3,  v3(b)=v3(L!).                            (2)

Since v3(c)=1 and xi_const is divisible by L!, the first term in
the actual coupled numerator c xi_const-b xi_last is strictly deeper
than its second term. In particular

  (c xi_const-b xi_last)/L! = -2*2 =2mod3,
  v3(c xi_const-b xi_last)=v3(L!).                       (3)

This evaluates the coupled cancellation rather than subtracting bounds.

## Transfer to the actual primitive polynomial

N=3M+1 is a 3-unit, so v3(L!)=v3(N!). The established monic endpoint
formula is P_n(-1)=-N!*(c xi_const-b xi_last)/(a delta_S).
Since a is a unit and v3(delta_S)=1,

  v3(P_n(-1))=2v3(N!)-1.

On the regular family, the established actual primitive leading multiplier
has depth1; therefore the proposed exact theorem is

  v3(Q_(4^j+1)(-1))=2v3((4^j)!), j>=1.                 (4)

The broader n3M+2 domain should be stated only if its leading multiplier
and polynomial normalization are independently verified; (1)-(3) have
been derived on that broader Schur domain.

As a normalization check, at n65 L63 and v3(L!)=30. The unit of63! is2mod3,
so (2),(3) predict b/3^30 and the coupled numerator/3^30 both1mod3,
matching the already executed controls. This check is not used to prove (4).

## Final endpoint gcd is still a separate obligation

The complete rational-arctan pair is
A=det T, B=ell Q(-1)det K, g=gcd(|A|,|B|), q=|B|/g.
Thus (4) determines the polynomial endpoint depth, NOT v3(q).
With A4's first low Schur matrix S,

  v3(q)=max(0,h+2v3(N!)-1+v3((S^-1)_00)).

The inverse distinguished coordinate must still be controlled. The whole
error remains sign(B)ell^k det H_complete/g, including both transcendental
contributions and eventual nonvanishing on the supplied regular domain.
