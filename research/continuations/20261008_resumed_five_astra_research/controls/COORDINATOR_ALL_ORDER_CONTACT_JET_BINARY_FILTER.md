> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-order contact-jet parity via a two-carry finite-field filter

Parent derivation, 9 October 2026. This is a source-specific extension
of the exact identity in A2turn12 Section4, conditional on that identity
and its established contact-source premises. Parent proof review of
the full report is favorable; DIFFERENT audit is pending. This note
does not assert a growing cofactor unit or any final gcd upper bound.

Scoped searches of the current, previous, and Desktop English math
archive recover the low-order r+j<16 statement only in A2turn12 and
no evaluated all-order law for these original sources. Classical Lucas
and finite-field root filters are reuse. Primary literature searches
recover Lucas surveys and unrelated/special Hankel evaluations, not
an upper bound for the complete corrected affine coefficient pair.
The abstract of https://arxiv.org/abs/1409.3820 is inspected only as
an overlap reference; no new theorem from the survey is imported.
https://arxiv.org/abs/2607.08279 is inspected at ABSTRACT scope only;
its dilated single-sequence determinants are not silently transferred
to this mixed corrected pencil. No full-paper inspection is claimed.

Let the normalized contact-jet parity be

    J(d,r,j) = Delta^j t_n^(r) / [2^j (r+1)_j] mod2.

The exact product-rule identity already gives, for every nonnegative
r,j in its source domain (without r+j<16),

    J(d,r,j) = sum_(t=0)^d binom(d+j,t+j)
                  binom(t+j+r,j+r) eta_(t+j+r) mod2.       (1)

The physical top row n disappears modulo2. This uses odd(o_d)=1 and
every odd factor Q_h(n)=1mod2; it does not commute A_d with Delta.
Write n0=d+j, K=j+r, l=t+j. The terms l<j vanish because
binom(l+r,K)=0, so (1) can be summed over 0<=l<=n0.

Work in F4=F2[omega]/(omega^2+omega+1), with Tr(x)=x+x^2.
The accepted contact sequence is

    theta_m = Tr(omega^(m+2)),
    eta_m = theta_m+(m+1)theta_(m+1)
          = Tr(omega^(m+2) [1+(m+1)omega]).                (2)

Indeed theta starts1,0,1 and satisfies theta_(m+2)=theta_(m+1)+theta_m.
All integer multipliers inside F4 are reduced modulo2. Substituting
(2), using binom(l+r,K)=[z^K](1+z)^(l+r), and differentiating the
binomial theorem in characteristic2 gives

    J(d,r,j) = Tr(omega^(r+2) * (
        [1+(r+1)omega] C(r,n0,K)
        +(n0 mod2) omega^2 C(r+1,n0-1,K))),              (3)

where n0>0 on every original index and

    C(a,b,K)=[z^K](1+z)^a [1+omega(1+z)]^b.

The derivative term is required: summing l binom(n0,l)X^l gives
n0 X(1+X)^(n0-1), and the extra omega from (2) makes its factor
n0 omega^2(1+z). Omitting that term outside the low-order regime
would invalidate the extension. Formula (3) requires no low-order
restriction and is a value formula for the normalized parity ONLY.

Since 1+omega=omega^2, Lucas gives the further exact expression

    C(a,b,K)=omega^(2b) * sum_(u+v=K,
                   u bitwise-subset a, v bitwise-subset b) omega^(-v).

This coefficient is computed in O(log(a+b+K+1)) digit steps by a
two-carry weighted automaton over F4. Begin carry0 with weight1;
carry1 has weight0. At binary position i choose u_i in{0,a_i} and
v_i in{0,b_i}, counting the unique zero choice only once when the
corresponding input bit is0. Retain only transitions

    u_i+v_i+carry = K_i+2*next_carry,

and multiply their weights by omega^(-v_i*2^i mod3). Add weights
over F4. After enough leading zero digits retain carry0, then multiply
by omega^(2b mod3). No growing polynomial or subset list is built.
Each of the two coefficients in (3) uses at most two carry registers.
The modulus and finite-field arithmetic are fixed; the complexity is
linear in the input bit length. This is classical Lucas/carry machinery
applied to the exact original source, not a new generic automaticity
theorem or closure theorem for inverses.

The remaining mathematical questions are different: whether these
evaluated parities select an attaining growing source-minor flag;
how all bottom corrections enter when the compound depth reaches
L_d=alpha_d-12; and how the two terminal coefficient borders behave.
Formula (3) alone answers none of these. Pure RN_d A has rank<=d
while the complete common matrix has d+1 columns. Every original
factorial, odd divisor, corrected border, terminal and all-prime gcd
must therefore remain in any proposed continuation.

No arithmetic comparison has yet been run for this note. A bounded
parent comparison of (3)'s digit rule with the independent finite
integer sum (1), including r+j>=16, would authenticate arithmetic at
its finite scope. The uniform statement is the derivation above.
