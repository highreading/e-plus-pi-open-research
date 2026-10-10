> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A contiguous exact endpoint reduction and full-depth gcd gate for b=2

Date: 2026-09-13. Author: audit_results.
Status: FULL PASS in hp_b2_contiguous_endpoint_independent_review.md.
No new canonical degree or prime scan is used.

This concerns degree caps (n,2,n), order 2n+3, and
F(z)=4 arctan(z/(2-z)) from hp_b2_endpoint_attempt.md.
It replaces the entire endpoint kernel by adjacent Legendre data,
retaining the actual numerator. A second theorem restricts the
endpoint gcd of the primitive full triple at its full prime-power
depth. Neither result bounds the reduced denominator at fixed small
primes. The original equal-degree raw family's all-parity exclusion
is separate: raw_all_parity_raw_exclusion.md.

## 1. Normalizations and the rational second-kind endpoint

Let


$$
{\cal L}(f)=\int_{-1}^1f((1+iu)/2)\,du,\qquad
 L_k(t)=2^ki^kP_k(-i(2t-1))\in{\mathbb Z}[t].
$$


Set P=L_n, U=L_(n+1), A=P(1), B=U(1), and


$$
w_P={\cal L}\frac{P(t)-A}{t-1},\qquad
 w_U={\cal L}\frac{U(t)-B}{t-1}.
$$


These w values are rational. The second-kind Wronskian and
Christoffel--Darboux identity give exactly


$$
G:=Aw_U-Bw_P=\frac{(-1)^n2^{2n+3}}{n+1},\qquad
 K_n(1,t)=\frac{BP(t)-AU(t)}{G(1-t)}.                 \tag{1}
$$


Indeed multiply the monic CD identity by the two leading
coefficients 2^n binom(2n,n), 2^(n+1) binom(2n+2,n+1).
Their product times the monic norm h_n is the displayed G.
Integration of CD then proves the Wronskian.

Let E_r=sum_(v=0)^r 1/v! and, for j=0,1,2, define


$$
\ell_j(t^k)=\frac1{(n+k+1-j)!},\qquad
 a_j=\ell_j(U),\quad r_j=\ell_j(P),\qquad
 T_j(Q)=\sum_k[t^k]Q(t)\,E_{n+k-j}.                  \tag{2}
$$


Take n>=2, so every E index is nonnegative. Write T_P=T_0(P),
T_U=T_0(U). The exact elementary exponential-polynomial endpoint
x_j=A_j(1) and logarithmic endpoint t_j=-C_j(1), for the elementary
exponential polynomial z^j, satisfy


$$
\boxed{t_j=\frac{A T_j(U)-B T_j(P)}G,\qquad
 x_j=\frac{w_P T_j(U)-w_U T_j(P)}G.}                 \tag{3}
$$


Thus (3) includes the actual reconstructed A endpoint.

For proof put D(t)=(w_UP(t)-w_PU(t))/G, so D(1)=1.
The earlier exact projection remainder is
W(t)=D(t)/(1-t)-pi K_n(1,t).
The polynomial part of D/(1-t)-1/(1-t) is (D-1)/(1-t).
Taylor reconstruction gives
x_j=ell_j((D-1)/(1-t))-E_(n-j).
For every polynomial Q,


$$
\ell_j\frac{Q(t)}{1-t}=eQ(1)-T_j(Q).
$$


The e terms cancel using D(1)=1, proving (3).
The first formula follows in the same way from CD.

All subsequent quotient, reduced-denominator, and quotient-valuation
formulas assume Y!=0, equivalently D_n!=0 in (9). The inherited
normality theorem guarantees this for all sufficiently large n.
The polynomial determinant identities and the primitive endpoint-gcd
inequality retain their unconditional stated degree scope.

## 2. Two scalar determinants give the actual reduced ratio

Define


$$
{\cal S}=a_1^2-a_0a_2,\qquad
 {\cal C}=(a_1-a_0)r_2-(a_2-a_1)r_1,\qquad
 {\cal W}=a_1r_2-a_2r_1.                            \tag{4}
$$


Use the raw cross product of rows a=(a_0,a_1,a_2) and
1+t=(1+t_0,1+t_1,1+t_2).
Relative to the previous monic convention this multiplies the
raw scale by the leading coefficient of U, preserving X/Y.
Its endpoints are exactly


$$
\boxed{Y=\frac{B{\cal C}-A{\cal S}}G,\qquad
 X=\frac{(w_P+T_P){\cal S}-(w_U+T_U){\cal C}
                    -a_0{\cal W}}G.}               \tag{5}
$$


Consequently the actual reduced denominator is q_n=den(X/Y),
including all full coefficient content and endpoint gcd.

For the signs, write e=(1,1,1). Then
Y=det(a,e+t,e), X=det(a,e+t,x).
Since T_0(Q)-T_1(Q)=ell_1(Q) and
T_1(Q)-T_2(Q)=ell_2(Q), column differences give


$$
\det(a,e,T(U))={\cal S},\quad
 \det(a,e,T(P))={\cal C},\quad
 \det(a,T(U),T(P))=a_0{\cal W}+T_U{\cal C}-T_P{\cal S}.
$$


The determinant of the coefficients expressing (t,x) in
(T(U),T(P)) is -1/G by (1). This proves (5).

## 3. The denominator uses only five integer transforms

Use the established integer polynomials


$$
H_k(x)=k![s^k]e^{xs}(1-s+s^2/2)^k
$$


and write


$$
H_k=H_k(1),\quad J_k=kH_k(1)+H'_k(1),\quad
 K_k=k(k-1)H_k(1)+2kH'_k(1)+H''_k(1).               \tag{6}
$$


Here K_k is a scalar, distinct from K_n(t,s).
Set f=2^n/(n!)^2 and g=2^(n+1)/((n+1)!)^2. Then


$$
(r_1,r_2)=f(H_n,J_n),\qquad
 (a_0,a_1,a_2)=g(H_{n+1},J_{n+1},K_{n+1}).           \tag{7}
$$


Rodrigues gives the exact polynomial identity


$$
\sum_r[t^r]L_k(t)\frac{x^{k+r}}{(k+r)!}
       =\frac{2^k}{(k!)^2}x^kH_k(x).                \tag{8}
$$


Zero, one, and two derivatives at x=1 prove (7).

Define the integers


$$
S=J_{n+1}^2-H_{n+1}K_{n+1},\qquad
 C=(J_{n+1}-H_{n+1})J_n-(K_{n+1}-J_{n+1})H_n,
$$




$$
W=J_{n+1}J_n-K_{n+1}H_n,\qquad
 \boxed{\mathscr D_n=(n+1)^2 B C-2A S\in{\mathbb Z}.} \tag{9}
$$


Define the rational numerator


$$
\boxed{\mathscr X_n=
 2(w_P+T_P)S-(n+1)^2(w_U+T_U)C
                       -2fH_{n+1}W.}              \tag{10}
$$


Equations (5) and (7) imply


$$
Y=\frac{gf}{G(n+1)^2}\mathscr D_n,\qquad
 \boxed{X/Y=\mathscr X_n/\mathscr D_n.}              \tag{11}
$$


The previous eventual nonzero-endpoint theorem also proves eventual
nonvanishing of the integer D_n in (9).

For a wholly integral, deliberately nonminimal presentation set


$$
\Lambda_n=2^{n+1}(2n+2)!(n!)^2,\qquad
 \mathscr N_n=\Lambda_n\mathscr X_n\in{\mathbb Z}.
$$


The moment denominators in w_P,w_U divide 2^(n+1)(n+2)!;
the T denominators divide (2n+1)!. Thus the assertion follows
term by term. The actual denominator is exactly


$$
\boxed{q_n=\frac{|\Lambda_n\mathscr D_n|}
 {\gcd(|\Lambda_n\mathscr D_n|,|\mathscr N_n|)}.}      \tag{12}
$$


For every p>2n+2 both X_n and D_n are p-integral, and


$$
v_p(q_n)=\max\{0,v_p(\mathscr D_n)-v_p(\mathscr X_n)\}. \tag{13}
$$


No minimality of Lambda is asserted or needed.

## 4. Three integer minors restrict the primitive endpoint gcd

Define the scalar


$$
M_k=k(k-1)(k-2)H_k(1)+3k(k-1)H'_k(1)
                      +3kH''_k(1)+H'''_k(1)
$$


and the integer matrix


$$
{\bf M}_n=
 \begin{pmatrix}H_n&J_n\\J_{n+1}&K_{n+1}\\K_{n+2}&M_{n+2}\end{pmatrix},
 \quad
 \Omega_n=\gcd\{\text{its three maximal minors}\}.    \tag{14}
$$


For a primitive full integral triple (A,B,C) of the b=2 family,
and every prime p>2n+4,


$$
\boxed{v_p\gcd(A(1),B(1))\le v_p(\Omega_n).}         \tag{15}
$$


If all three minors vanish the zero-gcd convention makes the
bound vacuous. The statement retains full prime-power depth.

Proof: if p^d divides both endpoints, endpoint matching gives
C(1)=0 modulo p^d too. Divide the three polynomials by z-1 over
Z/p^d. The degree caps become (n-1,1,n-1), while the remainder
still has order 2n+3 because z-1 is a unit at zero. Every required
Taylor denominator is a p-unit.

The quotient B has a primitive two-coefficient vector modulo p.
Otherwise the first n logarithmic moment equations and p-unit
Legendre norms force quotient C=0 modulo p; the low equations
force quotient A=0, contradicting full primitiveness.

Test the quotient high moment equations against orthogonal
polynomials of degrees n,n+1,n+2. The C terms vanish since
its degree is n-1. The two functional columns are
1/(n+j)! and 1/(n+j-1)!.
Identity (8) and its first three derivatives identify the rows,
up to p-unit scalars, with (14). All factorials and Legendre
leading coefficients involved are units for p>2n+4.
Thus M_n has a primitive kernel vector modulo p^d.
Complete that vector to a unimodular 2-by-2 basis; the transformed
matrix has one column zero modulo p^d. Its maximal minors vanish
modulo p^d, proving (15).

## 5. Exact limit of the present arithmetic reduction

The integral-Jucys--Murphy theorem from the original raw family
compares same-size Schur shapes under an integral power-sum
specialization. It does not immediately supply a reduced-denominator
bound for (9). The actual numerator (10) retains the independent
partial-exponential contractions T_P,T_U and second-kind values.
Congruences for H,J alone do not remove these entries.

Concretely, the passed b=1 folding theorem shows that contraction
by factorial denominators after a kernel congruence modulo p can
depend on (K_n-K_m)/p modulo p. The passed b=2 theorem at n=p-1
shows p does not divide the actual q, despite factorial raw
coefficient denominators. These are actual obstructions to
inferring q depth from mod-p coefficient or Appell information.

The smaller remaining target is now explicit: control the common
depth of the two integers (Lambda_n D_n,N_n) in (12), or control
D_n and X_n locally using (13). Above 2n+4, (15) additionally
restricts the primitive full endpoint gcd by three stated integer
minors. At fixed small primes, neither (15) nor the old H/J
auxiliary gcd theorem applies to the actual endpoint gcd.
No primitive growth, primitive shrinking, or irrationality theorem
is claimed here.

## 6. Verification scope

The Section 2 determinant signs are checked with formal independent
scalar variables and the Wronskian relation. This is a universal
algebra control, not another approximant or prime scan.
The saved reproducible check is check_hp_b2_contiguous_formal_identity.py,
with output hp_b2_contiguous_formal_identity_checks.json; both pass.
Analytic normality and error rates are used only from the earlier
independently reviewed b=2 note.
