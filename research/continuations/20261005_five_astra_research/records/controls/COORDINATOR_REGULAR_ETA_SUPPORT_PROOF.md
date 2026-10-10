> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent reconstruction of the actual divided-coordinate radical support

This is a coordinator proof of the missing source interface, using the
actual definitions of A1 turns4--5. Those reports' unit-block and first
Schur-lift results remain explicit inputs. This proves a coordinate map;
it does not prove a bound for the final center denominator.

Revision: the three dangerous lower eta indices are N-1,N-2,N-3;
eta_N is the retained last coordinate theta/3. This corrects an index
label in the first dispatched version, without changing the argument.

Let n=4^j+1, N=n-1=3M+1. Use

    h0=1, h_(d+1)=(y+1)(y-1)^d,
    psi0=1, psi_(d+1)=h_(d+1)/d!.

The actual functional is rho=mu-evaluation at -1, where
mu(F)=integral_0^infinity exp(-t) F((1-t)^2) dt. The actual Gram and forcing are

    G_ik=rho(psi_i psi_k), 0<=i,k<n,
    omega_i=rho(psi_i psi_n), psi_n=h_n/N!.

For every integral F, mu((y-1)^s F) is divisible by s!: substitute
y-1=t(t-2) and expand into factorial moments (s+a)!. Hence every entry
of G is integral, and every forcing entry omega_i is integral. In
particular, for nonconstant index i=d+1,

    omega_(d+1)=mu((y+1)^2 (y-1)^(d+N))/(d! N!)

is integral because (d+N)!/(d!N!) is integral. The constant forcing is
mu((y+1)(y-1)^N)/N!, also integral. There is no negative-mass term in
either expression because psi_n(-1)=0. This verifies the full forcing,
without truncating its factorial expansion.

Partition G into the regular coordinates d=0,...,3M-1 and the two
remaining coordinates (constant,last d=3M). Write

    G = [[E,u,x],[u^T,G00,G0last],[x^T,G0last,Glastlast]].

The established residue theorem gives Ebar=B_M tensor A, where
B_M(D,E)=choose(D+E,D), A=[[0,2,1],[2,2,0],[1,0,0]]. Thus E is a
3-adic unit and E^-1 is integral. The last cross-column satisfies

    xbar=b tensor (A e0), b_D=choose(M+D,D).

With P_M(D,a)=choose(D,a), Vandermonde gives B_M=P_M P_M^T and
b=P_M v, v_a=choose(M,a), for a<M. Consequently

    (B_M^-1 b)_D
      = sum_(a=D)^(M-1) (-1)^(a-D) choose(a,D) choose(M,a)
      = (-1)^(M-1-D) choose(M,D).

The identity is exact over the integers before reduction. Therefore
E^-1 x reduces to the vector supported only at d=3D, D<M, with
coefficient (-1)^(M-1-D) choose(M,D). This is the map from the radical
column to the ORIGINAL psi coordinates, not a different basis.

Let [[a,beta],[beta,c]] be the Schur matrix after E elimination,
xi=omega_W-[u,x]^T E^-1 omega_E. The established first lift gives

    a=2 mod3, beta=0 mod3,
    delta=c-beta^2/a=3 mod9,
    xi_last=2 mod3, xi_const=0 mod3.

The exact actual solve eta=G^-1 omega is

    eta_last=(xi_last-(beta/a)xi_const)/delta,
    eta_const=(xi_const-beta eta_last)/a,
    eta_E=E^-1 omega_E-E^-1 u eta_const-E^-1 x eta_last.

Thus eta_const is integral, eta_last has valuation -1, and theta=3eta_last
is integral with theta=2 mod3. Multiplying the last identity by3 proves

    3eta_(d+1)=theta (-1)^(M-D) choose(M,D) mod3 if d=3D, D<M;
    3eta_(d+1)=0 mod3 otherwise.

At the actual last coordinate d=3M the same formula holds with D=M,
because its coefficient is theta itself. The constant coordinate reduces
to zero after multiplication by3. All coordinates have now been matched.

The monic polynomial identity is exactly

    P_n=h_n-N!eta_const
        -sum_(d=0)^(N-1) (N!/d!) eta_(d+1) h_(d+1).

This follows by multiplying psi_n-sum eta_i psi_i by N!, and therefore
uses the same eta as the forcing solve above. If 3 divides M, the
coefficients 3eta_(N-1), 3eta_(N-2), 3eta_(N-3) vanish modulo3: their d
indices are respectively 3M-1,3M-2,3M-3, and the last residue is
-M theta. These are precisely the three dangerous lower factorial indices
in A1turn17. For m=v3(M)>=2, their factorial quotients have depth m+1;
all lower quotients have depth at least m+2. The constant term is also
deep. Hence all these lower terms disappear in 3P_n modulo3^(m+2).

Conditional only on the independently retained true-jet/projected
contraction in A1turn17, Ntheta=68+3M modulo3^(m+2), the resulting
ACTUAL normalized polynomial is

    3P_n=(y+1)(y-1)^(n-2) [3y-71-(n-2)] mod3^(m+2).

For the primitive polynomial Q_n=L_n P_n, retain the actual unit
lambda=L_n/3: Q_n=lambda(3P_n). No endpoint-value or final determinant
gcd conclusion follows merely from this coefficient congruence.
