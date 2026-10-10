> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# L24 continuation: exact modulo8 Taylor branches and the remaining coupled transfer

Author structural lemma, 2026-10-02, within the fresh-gated L24 endpoint target. This is not another degree or prime atlas. The all-degree actual denominator result remains `WEIGHTED_REGULAR_ENDPOINT_DYADIC_RATE.md`: q2≥n+1 for n=4^j+1. The exact equality n+2 is unproved.

Let F=(O,E)^T be L23's INTEGRAL ordinary moment branches, with exact formal equation

    F(u)=M(u)F(u−2)+c(u).

The matrix and forcing polynomials are specified in that theorem. Put

    Q=(I−M)^−1c, R=(I−M)^−1M,
    D=det(I−M)=1+u+2u²−4u³−3u⁴.

All inverses exist as ordinary series over Z_2 because D(0)=1. Formal substitution by−2 is coefficientwise convergent for these integral series. Modulo8 the exact translation is

    F(u−2)=F−2F′+2F″ mod8.

All omitted terms have coefficients divisible8. Therefore

    F=Q−2R F′+2R F″ mod8.

Modulo4 this is F=Q−2R Q′. Taking its derivative and using that the second derivative of every integral power series has even coefficients gives the complete lift

    F=Q−2RQ′+4R(RQ′)′+2RQ″ mod8.            (1)

The last term must be retained; it is generally only4-divisible, not8-divisible. The common denominator in(1) divides D^5. The exact numerator polynomials modulo8, their constant polynomial parts, and the proper rational parts are saved in `WEIGHTED_BRANCH_MOD8_LIFT_RECEIPT.json` by `weighted_branch_mod8_lift.py`.

## 1. A certified period independent of the depth/degree

The polynomial D modulo2 is1+u+u⁴, which divides u^15−1 modulo2. Write u^15−1=D Q_0+2R_0 in Z/8[u]; the leading coefficient of D is a unit so the division is legitimate. Expanding

    u^480−1=(1+(u^15−1))^32−1

shows that D^5 divides this polynomial modulo8. Indeed its terms with exponents1,…,4 have8-divisible binomial coefficients. For exponents5,6 the coefficients supply at least16. In every term with exponent≥7, an expansion of(DQ_0+2R_0)^a either contains at least five D factors or at least three2 factors. This proves the polynomial divisibility at all coefficients.

The receipt also stores the exact finite polynomial remainder

    u^480 mod D^5 mod8 =1.

Consequently each PROPER rational part with denominator D^5 has480-periodic ordinary Taylor coefficients. The extracted polynomial parts are constants, so O,E modulo8 have480-periodic coefficients from degree1 onward. The constant coefficient is separately specified and never silently treated as periodic. This is a proved recurrence identity, not extrapolation from a list of moments.

## 2. Exact conversion to every normalized finite-difference entry

Let t_j be the appropriate ordinary Taylor branch coefficients. For a starting argument whose even branch coordinate is2c, define

    rho_d(c)=Delta_2^d b_start/(2^d d!).

Expanding the integral Taylor series gives EXACTLY modulo8

    rho_d(c)=t_d
      +2[(d+1)c+binom(d+1,2)]t_(d+1)
      +4[binom(d+2,2)c²+(d+2)c binom(d+1,2)
                       +S(d+2,d)]t_(d+2),   (2)

where S(d+2,d)=binom(d+2,3)+3binom(d+2,4). Higher Taylor terms carry8. The needed Gamma and endpoint matrices only use fixed starting values0,…,4, so c is fixed0,1,2. Equation(2) supplies the complete modulo8 normalized entries at every difference order.

An independent conversion from the exact normalized Newton differences is

    t_j=rho_j(0)−j(j+1)rho_(j+1)(0)
                 +4 e_2(0,1,…,j+1)rho_(j+2)(0) mod8.

It follows because the coefficient of u^j in u(u−2)...(u−2d+2) has depth at least d−j. The receipt has160 exact conversion checks,80 on each branch, supporting this author representation without any new full determinant node.

## 3. What the periodic data does and does not settle

The normalized coupled endpoint quotient from L24 is

    U=P_n(0)/D_m²,
    U[1−A_z((1−z²)^m)]
      =A_z(h_n(1−z²)^m)/D_m²
       −Σ_(i≥1)eta_i (D_m/D_i)
                   A_z(h_i(1−z²)^m)/D_m².  (3)

The actual pair formula gives q2=n+v2U. L24 proves U even by the COMPLETE mod2 Gram inverse. Exact equality q2=n+2 would require U=4 mod8. All moments, mixed vectors and rational corrections in(3) now have the explicit fixed-period inputs(1)–(2), multiplied by the appropriate integer binomial factors. But the inverse of the2m-dimensional unit Gram block remains coupled to those inputs. Its size increases with m. A periodic scalar input sequence does not imply a periodic inverse or the required residue of(3).

The remaining sharply scoped task was an exact matrix/block transfer under m→4m, or a square-class identity for the one Schur scalar. Sections4–5 now REMOVE the inverse structurally, but do not yet evaluate the resulting carry sums. The proven actual rate q2≥n+1 is unchanged; no odd-content or irrationality conclusion is inferred.

## 4. New all-degree identity: the complete residue inverse is index reversal

Write m=2^h with h odd, M=m−1. The nonconstant block B of the signed normalized Gram is indexed by P_d=z(z²−1)^d/D_d and E_d=z²(z²−1)^d/D_d,0≤d<m. Its residue in the order (all P,all E) is

    Bbar=[[H_e,H_o],[H_o,H_e]],
    (H_f)_(d,e)=binom(d+e,d) f_(d+e) mod2.

The binomial residue is zero if the binary supports of d,e intersect. Let R reverse d to M−d in BOTH member blocks. Then

    Bbar^−1 = R Bbar R.                                      (4)

This is an identity for EVERY m=2^h with a_M=e_M+o_M=1. It does not depend on an extrapolated list of inverses.

Proof. In the Boolean monomial algebra

    A_h=F2[X_0,…,X_(h−1)]/(X_0²,…,X_(h−1)²),

index X_d by binary support and let Ω extract X_M. For any sequence f define g_f=Σ_(d<m) f_(M−d)X_d. Its Frobenius matrix Ω(g_f X_d X_e) is H_f, so H_f=R M_(g_f), where M_g is multiplication by g. Every positive-degree element squares to zero in A_h. Hence g_a²=a_M²=1, and

    J=H_a^−1=M_(g_a) R,
    K=J H_e J=M_(g_e) R.

The elementary two-member inverse is

    Bbar^−1=[[K,J+K],[J+K,K]].

Since J+K=M_(g_o)R, this equals R Bbar R. This proof retains both coupled response blocks.

The corresponding binary lift C has the explicit entries

    C_((d,P),(e,P))=C_((d,E),(e,E))
        =1_(d OR e=M) e_(2M−d−e),
    C_((d,P),(e,E))=1_(d OR e=M) o_(2M−d−e),              (5)

with symmetric opposite block. These are ordinary integers0 or1.

## 5. New complete modulo8 endpoint quotient without an inverse

Take C to be that fixed binary lift and B the ACTUAL normalized block over Z2, not just its residue. Then BC=I+2E for an integral matrix E. Truncating the geometric inverse gives

    B^−1 = C(I−2E+4E²) mod8
           =3C−3CBC+CBCBC mod8.                              (6)

There is no assumption that E is symmetric. The second expression is symmetric because B,C are. The omitted term is8-divisible.

Let rho_r(b_j) denote Δ_2^r b_j/(2^r r!). In the interleaved member order the exact inputs modulo8 are

    B_(dP,eP)=binom(d+e,d)rho_(d+e)(b_2),
    B_(dP,eE)=binom(d+e,d)rho_(d+e)(b_3),
    B_(dE,eE)=binom(d+e,d)rho_(d+e)(b_4),
    omega_(dP)=binom(m+d,m)rho_(m+d)(b_2),
    omega_(dE)=binom(m+d,m)rho_(m+d)(b_3),
    t_(dP)=binom(m+d,m)rho_(m+d)(b_1),
    t_(dE)=binom(m+d,m)rho_(m+d)(b_2),
    L=binom(2m,m)rho_(2m)(b_1).

Formula(2) evaluates every rho from the fixed Taylor period. The previous complete endpoint bound gives v2 eta0≥sigma+1≥4. Thus the constant-coordinate coupling has zero residue modulo8, and eta_rest=B^−1 omega modulo8. Also A_z((1−z²)^m) has depth at least sigma≥3, so the factor multiplying U in(3) equals1 modulo8. Therefore the COMPLETE normalized endpoint quotient is

    U = L−3 t^T C omega+3 t^T C B C omega
                     −t^T C B C B C omega mod8.                (7)

No constant-coordinate or final-gcd contribution has been dropped. The actual reduced denominator remains q2=n+v2 U. Exact equality q2=n+2 is equivalent to(7) having residue4.

`weighted_endpoint_binary_inverse.py` saves the all-entry binary inverse identity at the existing m2,8,32 states and checks(6) against the full residual. It additionally compares the lifted solution with independently retained exact rational moment solutions at m2,8. The three contractions in(7) are (6,0,2),(0,0,4),(2,4,2) modulo8 respectively, while L=0 and U=4 at all three. Their variation makes clear that the fixed Taylor period alone does not evaluate(7).

The growing inverse has now been eliminated. The remaining original problem is a finite-state BINOMIAL-CARRY SUM evaluation of(7) under m→4m, or a structural identity implying its residue4. It is not a question of another degree atlas. Until such an identity or explicit carry transfer is proved, the all-degree theorem is q2≥n+1, and q2=n+2 remains conjectural.
