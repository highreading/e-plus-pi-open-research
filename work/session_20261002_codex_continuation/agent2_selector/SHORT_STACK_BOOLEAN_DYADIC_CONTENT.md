> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Simultaneous dyadic content of the actual two short-stack rectangles

Author theorem: Agent 2, 2026-10-02. Fresh archive and opened-primary gate: `SHORT_STACK_BOOLEAN_BASIS_GATE.md`. The word Boolean here refers only to a polynomial vanishing at 0 and 1; this is an integer monic basis argument, not an assumption about a finite-field normality or a new weighted matching family.

## 1. Exact actual-content statement

Retain all definitions and physical normalization from `SHORT_STACK_SIMULTANEOUS_JET_CONTENT.md`:

    N=[G;LK], size 2k by (2k-1),
    W=[C;LK], size (2k-1) by 2k,
    G_r=D_(2r)+D_(2r+2),
    K_r=-(2r)!-(2r+2)!+4/(2r+1),
    C_r=D_(2r)-(-1)^r,
    L=lcm(1,3,...,6k-5),
    I0=L^k beta0, J1=L^(k-1) beta1, I1=LJ1.

Put m_j=floor(j/2), b_j=v2(m_j!), a_j=m_j+b_j, and S_n=sum_(j=0)^(n-1)a_j. Define

    E_N=2S_k-a_(k-1)+S_(2k-1)+(k-1),
    E_W=S_k+S_(k-1)+S_(2k)-a_(2k-1)-b_(k-1)-b_(2k-1).

For EVERY k>=1, every maximal minor of N is divisible by 2^E_N and every maximal minor of W is divisible by 2^E_W. When beta1!=0 their positive contents therefore satisfy

    v2(h_N)>=E_N, v2(h_W)>=E_W.                          (1)

Since h_N divides BOTH actual physical coefficients, in particular

    2^E_N | gcd(I0,I1).                                 (2)

Both exponents are

    E_N=3k^2+O(k log k), E_W=3k^2+O(k log k).             (3)

This improves the earlier guaranteed dyadic exponent 2k^2+O(k log k) from the one-center top Gamma argument. It establishes no equality for h_N,h_W or the final gcd, and does not address unresolved odd specialized content.

## 2. A monic integer basis for both centers

For j=2m+epsilon, epsilon in {0,1}, use

    Q_j(y)=y^epsilon [y(y-1)]^m=y^(m+epsilon)(y-1)^m.

Its degree is j and its leading coefficient is 1. For every initial degree segment these polynomials are related to 1,y,... by an INTEGER unitriangular matrix of determinant 1. Their separate application to the two row blocks and the full column block thus preserves all maximal-minor contents exactly. There is no rational coefficient denominator, scalar height, or lattice index introduced by the change of basis.

For a product Q_i Q_j set

    m=m_i+m_j, u=m+epsilon_i+epsilon_j.

Then Q_i Q_j=y^u(y-1)^m. We will prove entry valuations at least a_i+a_j for each non-evaluation part, keeping the complete reciprocal term.

## 3. Shifted Gamma, factorial Gamma, and compact beta parts

Let mu be the same shifted Gamma pushforward used by Agent 3. The saved exact integer recurrence in `EVEN_GAMMA_ODD_SATURATION.md` gives

    A_s=mu((y-1)^s)=2^s s! U_s, U_s integral,
    U0=1,U1=0,U_(s+1)=(2s+1)U_s+U_(s-1), s>=1.

Since y^u=(1+(y-1))^u, mu(y^u(y-1)^m) is an integer binomial combination of A_(m+s), s=0,...,u. It is divisible by 2^m m!. Moreover

    mu((y+1)y^u(y-1)^m)

is a combination of A_(m+s+1)+2A_(m+s), so is divisible by 2^(m+1)m!. Because (m_i+m_j)! is divisible by m_i!m_j!, the transformed G entry has valuation at least

    a_i+a_j+1.                                         (4)

For the ordinary factorial functional f(y^r)=(2r)!, the polynomial

    (y+1)y^u(y-1)^m

has integer coefficients and no monomial of degree below u>=m. Every contributing (2r)! is divisible by (2m)!, whose dyadic valuation is exactly m+v2(m!), by Legendre's formula. This bounds the complete factorial part of K from below by a_i+a_j.

The COMPLETE compact part of K is 4 integral_0^1 Q_i(x^2)Q_j(x^2)dx. The exact beta integral is

    integral_0^1 x^(2u)(x^2-1)^m dx
       =(-1)^m 2^m m! / product_(s=0)^m(2u+2s+1).       (5)

EVERY denominator in (5) is odd. Thus its dyadic valuation, even before the factor 4, is at least a_i+a_j. The odd L multiplier neither loses nor supplies dyadic valuation. Although (5) can have repeated odd-prime depths in its denominator product, the entry is still exactly the original L-cleared polynomial moment and is integral; no unsupported odd-factorial divisor is asserted.

Equations (4)--(5) prove that the transformed N has its k G rows bounded by 2^(a_i+a_j+1), and its k K rows by 2^(a_i+a_j), entrywise. All rational endpoints remain included.

## 4. Tall rectangular content and the final physical pair

A maximal minor of N uses ALL 2k-1 columns and omits one of its 2k rows. Factor the column powers 2^a_j. The sum of row a_i powers is at least

    2S_k-max_(i<k)a_i=2S_k-a_(k-1),

because a_i is nondecreasing. At least k-1 of the selected rows are G rows, each supplying its extra factor 2. The resulting exponent is exactly E_N.

The integer basis changes preserve the ideal of all maximal minors, proving the first statement in (1). The previously proved cofactor extension gives h_N|I0 and h_N|J1. Since the PHYSICAL response is I1=LJ1, it also gives h_N|I1. This proves (2) without replacing an input row clear with the final output content.

The stronger individual response determinant has k G rows and k-1 rows of the functional (y+1)K after BOTH its response row and column are removed. Multiplying K by this extra y+1 retains the same entry divisor: the factorial polynomial still has minimum degree at least m and the compact part is the sum of two beta integrals with odd denominators. The same basis argument also gives

    v2(J1)>=S_k+S_(k-1)+S_(2k-1)+k=E_N+1.              (6)

Equation (6) is a component divisor, not a claim that this additional response factor survives the final gcd.

## 5. Wide content and the single endpoint evaluation

Apply the Q basis to all k C rows, k-1 K rows, and 2k columns of W. The transformed top block is

    mu(Q_i Q_j)-Q_i(-1)Q_j(-1).

Its Gamma part has the row and column a powers proved above. The complete K rows have those same powers. The endpoint is rank ONE, with

    Q_i(-1)=(-1)^epsilon_i 2^m_i.

In a maximal determinant, terms with two endpoint rows vanish. A term with one endpoint row is an expansion along that row, so it can lose only b_i from that row and b_j from ONE column. Therefore every selected minor has valuation at least its sum of row a powers plus its sum of selected-column a powers minus

    max_(i<k)b_i+max_(j<2k)b_j.

All rows are used and one column is omitted. The smallest selected-column sum is at least S_(2k)-a_(2k-1), and b_j is nondecreasing. This proves E_W and the second part of (1), including all carried sums: every determinant term has the stated divisor, so possible cancellations can only increase its valuation.

## 6. Asymptotics and honest combination with earlier normalization

Legendre gives a_j=2m_j-s2(m_j)=j-epsilon_j-s2(m_j), where s2 is the binary digit sum. Hence

    S_n=n(n-1)/2-O(n log n).

Inserting this in the exact exponents proves (3). The difference E_N-E_W is exactly

    k-1+b_(k-1)+b_(2k-1),

and is O(k), so the tall rectangle supplies the stronger guaranteed dyadic divisor.

Let d_old=k(k-1)+2v2(F_(k-1)), with F_s=product_(r=0)^(s-1)r!. The old complete divisor already includes the factorial's 2-content. The new allowed PRODUCT divisor is therefore

    2^max(d_old,E_N) * oddpart(F_(k-1)^2) * W_k,

not the product of 2^E_N with the full old dyadic factor. Here W_k is the already-proved odd common factor supported on 4k<p<6k-5, coprime to the factorial support. The additional GUARANTEED normalization factor relative to the old proof is

    2^max(0,E_N-d_old),
    log of this factor=(log 2)k^2+O(k log k).

The leading response-norm and actual-q ceiling remain 4 and 3 times k^2 log k, respectively, because this gain has scale k^2. The complete signed-error theorem and the exact physical gcd sandwich are unchanged. No claim that the actual q changes, or that its full gcd equals the guaranteed factor, follows from changing basis.

The single existing k=5 normalization was used for a NEW basis/entry/maximal-minor identity check. Four basis determinants,180 complete moment-entry divisors,20 maximal-minor divisors, the exact beta formula, both saved rectangular contents and the old308-bit actual q interface all passed in `SHORT_STACK_BOOLEAN_RECEIPT.json`. Here E_N=34,E_W=26 while the actual rectangular depths are46,40 and the full actual gcd depth50. No equality or all-degree valuation pattern is inferred from those numbers. Evaluating only the PROVED exponent formula at k64 gives new guaranteed depth11214 versus the prior7566; no new k64 full determinant or numerical approximation was computed.
