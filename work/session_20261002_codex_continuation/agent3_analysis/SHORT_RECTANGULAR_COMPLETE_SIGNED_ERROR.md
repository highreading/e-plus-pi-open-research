> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Short rectangular paired kernel: complete sign and exponential scale

Author theorem: Agent 3, 2026-10-02. Fresh archive and primary-literature gate: SHORT_RECTANGULAR_ANALYTIC_GATE.md. Root's exact family and basis/content identities are in main/SHORT_PAIRED_KERNEL_LINEAR_S.md. This note proves the analytic interfaces directly; it is not an audit of Root's finite certificates. No small-index real-value certification is attempted or required for the infinite criterion.

## The precise family and result

Let mu be the probability pushforward of exp(-t)dt, t>=0, by y=(1-t)^2. Put rho=mu-delta_{-1} and

    dsigma(y)=[exp(sqrt(y))+4/(1+y)]dy/[2sqrt(y)], 0<y<1.

The upper block C of size k by 2k has entries

    C_ij=rho(y^(i+j))=D_(2(i+j))-(-1)^(i+j),

and the lower COMPLETE block L has entries sigma(y^(i+j)). Entrywise L=eC+R+S V, S=e+pi, V_ij=(-1)^(i+j), and

    R_ij=-(2(i+j))!+4 sum_(a=1)^(i+j) (-1)^(i+j-a)/(2a-1).

Subtracting e times upper row i from lower row i is an EXACT determinant-preserving row operation. Thus det[C;L]=det[C;R+S V]. The identification is at the STACKED determinant, not an entrywise omission of the eC term. Write

    Delta_k=det[C;R+S V]=a_k+b_k S,
    c_k=-a_k/b_k.

Root proves this is the same rational center and final reduced denominator for any basis of the fixed matching kernel. That basis invariance is not an analytic improvement by itself.

**Theorem.** For EVERY k>=24,

    b_k!=0,  Delta_k!=0,
    sign b_k=sign Delta_k=(-1)^k,
    0<S-c_k=Delta_k/b_k.                              (1)

As k tends to infinity,

    log(S-c_k)=-4k log(1+sqrt(2))+O(log k).             (2)

Thus the actual complete center converges to S from below, with strictly nonzero signed error, and the coefficient normalization is controlled. This is a TWO-SIDED logarithmic scale result for the full exponential/arctangent determinant, not an asymptotic for just one endpoint.

If Q_k is the FINAL REDUCED denominator of c_k, its primitive complete form satisfies exactly

    log|Q_k(S-c_k)|=log Q_k-4k log(1+sqrt(2))+O(log k). (3)

The analytic theorem gives no lower or upper growth law for the actual Q_k and no favorable gcd. In particular Root's O(k^2 log k) cost upper bound is not a denominator lower bound.

## 1. Exact double-integral determinant identities

For x=(x_1,...,x_k), define Q_x(y)=product_i(y-x_i), and

    F_k(x)=det[ rho(y^(i+j)Q_x(y)) ]_(0<=i,j<k).

Repeated Andreief, or direct determinant expansion and symmetrization, gives

    Delta_k=(-1)^k/k! integral_[0,1]^k Vandermonde(x)^2 F_k(x) d sigma^k.   (4)

To verify the sign, the two blocks' Vandermondes contribute product_(a,i)(x_i-t_a), equal to (-1)^(k^2)product_a Q_x(t_a). Integration of the t variables, including the upper signed atom, gives F_k. Since (-1)^(k^2)=(-1)^k, (4) follows. Fubini is legitimate: all measures have every required finite moment, and there are finitely many polynomial factors.

The moment block for sigma+(s-S)delta_{-1} is eC+R+s V. Within the stack, subtracting e times the corresponding upper rows gives the normalized lower block R+s V. Its determinant is affine: terms with two copies of the lower atom have a zero Vandermonde. Differentiating (4) therefore gives EXACTLY the actual coefficient

    b_k=(-1)^k/(k-1)! integral_[0,1]^(k-1) Vandermonde(x)^2
           product_(i<k)(1+x_i)^2 F_k(x_1,...,x_(k-1),-1) d sigma^(k-1). (5)

The insertion factor kills the upper atom:

    F_k(x,-1)=det M_[mu·(y+1)product_(i<k)(y-x_i),k].                  (6)

There is no unaccounted contribution from either rational endpoint. Both exp(sqrt(y)) and 4/(1+y) remain in sigma throughout (4)--(5).

## 2. All-node finite-dimensional positivity for k>=24

Take ANY k-1 nodes x_i in [-1,1] and put Q(y)=product_(i<k)(y-x_i), nu=Q rho. Let p be any nonzero real polynomial of degree <k. On I=[k^2,4k^2],

    Q(y)>=(k^2-1)^(k-1),
    dmu_tail/dy=exp(-1-sqrt(y))/(2sqrt(y))>=exp(-2k-1)/(4k).

The Legendre evaluation kernel on I gives

    integral_I p(y)^2dy >=3·16^(-(k-1)) L(p),
    L(p)=max(|p(-1)|^2,sup_[0,1]|p|^2).                              (7)

Indeed |I|=3k^2, the affine image of -1 has absolute value (5k^2+2)/(3k^2)<2 for k>=2, and all points in [0,1] are closer to I. The exterior Legendre factor is <4. Summing its evaluation kernel for degrees 0,...,k-1 yields at most k^2·16^(k-1)/|I|, giving (7).

Thus the positive tail for nu(p^2) is at least

    C_k L(p),
    C_k=3 exp(-2k-1)(k^2-1)^(k-1)/[4k16^(k-1)].                     (8)

On [0,1], |Q|<=2^(k-1); the absolute compact negative part is at most 2^(k-1)L(p). The exterior atom's absolute contribution is also at most 2^(k-1)L(p). For every k>=24,

    C_k/2^k >4/[k(k^2-1)] [(k^2-1)/288]^k
              >=4(3/2)^k/[k(k^2-1)]>1.                            (9)

The first inequality uses e<3. The second uses k^2-1>=432, which holds at and beyond 24. The final expression is greater than 1 at k=24, as an exact rational inequality, and its ratio between successive indices is (3/2)(k-1)/(k+2)>1 for k>7.

Consequently

    nu(p^2)>=(C_k-2^k)L(p)>0                                     (10)

for every nonzero deg p<k, uniformly over the nodes in [-1,1]. This establishes positive definiteness of the needed truncated modified moment matrices; the underlying signed measure has not been assumed positive.

For a FULL k-node configuration in [-1,1]^k, its positive tail receives one more factor at least k^2-1. Its total absolute compact and atom loss is at most 2^(k+1)L(p). Equations (8)--(9) imply

    rho(Q_x p^2)>=[(k^2-1)C_k-2^(k+1)]L(p)>0.

Hence F_k(x)>0 for ALL x in [-1,1]^k and k>=24. In particular the integrands in (4)--(5) are strictly positive off the usual coincident-node diagonals. Sigma has a positive density on (0,1), so their integrals are strictly positive. This proves every assertion in (1), including the actual affine coefficient's nonvanishing and the complete signed error.

## 3. Uniform root separation for each conditional determinant

This section controls the actual inverse normalization needed for the complete rate. Keep ANY k-1 nodes in [-1,1], nu=Q rho, and the positive degree-k Gram from (10). Its compressed multiplication-by-y matrix in an orthonormal basis is real symmetric, and its characteristic polynomial is the degree-k monic polynomial orthogonal for nu. All norms below degree k are positive, so its off-diagonal entries are nonzero and the roots are simple.

Let

    a=1/(48e^4),   A=a k^2.

For every k>=100, A>=2 and A<k^2. Apply the same evaluation estimate as in (7) to the larger test set [-1,A]; its maximum exterior image is still attained at -1. The positive tail in nu((y-A)p^2) is therefore at least

    (k^2-A)C_k L_A(p),
    L_A(p)=max(|p(-1)|^2,sup_[0,A]|p|^2).

All of its negative continuous and atom contributions are bounded by

    [A(A+1)^(k-1)+(A+1)2^(k-1)]L_A(p)
       <=3A(A+1)^(k-1)L_A(p),                                  (11)

using A>=2 and the unit total mass of mu. The ratio of positive to this negative bound is at least

    (1-a)/(3a) · C_k/[((3/2)a k^2)^(k-1)]
       >=(1-a)/(4e a k) exp(-2k)[1/(48a)]^(k-1)
       =(1-a)exp(2k-4)/(4e a k)>1.                              (12)

Here k^2-1>=k^2/2 was used. The last inequality is elementary at k>=100; it is far from a limiting equality. Therefore

    nu((y-A)p^2)>0

for every nonzero deg p<k. The compressed multiplication matrix minus A times the identity is positive definite. Its EVERY root z_j is greater than a k^2, uniformly over all the other compact/exterior node choices. This is a conditional-root bound for the exact modified moments, not for the unsigned pushforward alone.

For a final node u, the determinant has the characteristic factorization

    F_k(x_1,...,x_(k-1),u)=det M_(nu,k) product_(j=1)^k(z_j-u).

Thus, uniformly for -1<=u<=1 and k>=100,

    exp(-4k/A) <= F_k(x,u)/F_k(x,-1) <=1.                       (13)

The lower bound follows from (z_j-1)/(z_j+1)>=(A-1)/(A+1)>=exp(-4/A), valid for A>=2. Replace the k nodes successively by -1. With

    F_k^*=F_k(-1,...,-1)=det M_[mu·(y+1)^k,k]>0,

one obtains the UNIFORM bounds

    exp(-4/a) <= F_k(x)/F_k^* <=1,
                    x in [-1,1]^k, k>=100.                     (14)

The constant is deliberately coarse but independent of k. This estimate controls the whole determinant/cofactor ratio and prevents an unproved inverse-conditioning loss from being hidden in an error majorant.

## 4. Reduction of the complete error to a positive reference quantity

Let D_(sigma,k) be the k by k ordinary sigma Hankel determinant, and

    B_(sigma,k)=v^T adj(M_(sigma,k))v,   v_i=(-1)^i.

The standard positive integral identities are

    D_(sigma,k)=1/k! integral Vandermonde(x)^2 d sigma^k,
    B_(sigma,k)=1/(k-1)! integral Vandermonde(x)^2
                    product_i(1+x_i)^2 d sigma^(k-1).

Both are strictly positive. Equations (4)--(5) and (14) give, for every k>=100,

    exp(-4/a) D_(sigma,k)/B_(sigma,k)
         <= S-c_k <= exp(4/a) D_(sigma,k)/B_(sigma,k).            (15)

The reference ratio is the genuine positive Christoffel minimum

    Lambda_(sigma,k)(-1)=min_(deg p<k,p(-1)=1) integral p^2 dsigma.

Its use is justified by (14)--(15), not by replacing the original stack with a positive Gram matrix. The original complete matrix need not itself be a positive square Gram matrix.

Compare sigma with the reference dgamma=y^(-1/2)dy:

    (3/2)dgamma <=dsigma <=((e+4)/2)dgamma.

This gives the corresponding two-sided comparison of Christoffel minima. For gamma the shifted Jacobi polynomial P_j^(0,-1/2)(2y-1) has squared norm 1/(2j+1/2) and value at -1 equal to (-1)^j P_j^(-1/2,0)(3). Hence

    Lambda_(gamma,k)(-1)=1/sum_(j=0)^(k-1)
                           (2j+1/2)[P_j^(-1/2,0)(3)]^2.        (16)

The positive binomial formula

    P_j^(-1/2,0)(3)=sum_(m=0)^j binom(j-1/2,m)binom(j,m)2^m

shows the exterior values increase with j. Elementary Stirling/Laplace bounds for this positive sum give

    log P_(k-1)^(-1/2,0)(3)
         =k log(3+2sqrt(2))+O(log k).

Bounding (16) between its final term and k times that term proves

    log Lambda_(gamma,k)(-1)
         =-2k log(3+2sqrt(2))+O(log k)
         =-4k log(1+sqrt(2))+O(log k).

Comparisons (15)--(16) now prove (2), with both full endpoint contributions retained. The exterior Jacobi identities and positive-kernel interpretation are classical; their comparison to these exact signed modified moments is the original mechanism established here.

## 5. Scope and arithmetic interface

The theorem is unconditional at every k>=24 and asymptotic as k grows. The finitely many smaller indices are outside its claimed range. Root's k=1,...,9 exact receipts are supporting construction data with diagnostic real values; they are not promoted to real interval certificates here.

The determinant coefficient b_k is rational and nonzero; after rational clearing and FINAL gcd the center has a well-defined positive denominator Q_k. Multiplying the two-sided complete error scale by that exact Q_k yields (3). A primitive smallness proof would need its reduced growth to beat 4log(1+sqrt(2)) per k; a raw cofactor estimate or a cost upper bound cannot establish that need.

Changing the basis of the fixed kernel retains c_k and Q_k. Root's distinct M25 one-extra-column coefficient lattice is reserved; it has not been substituted for the present family. No claim of irrationality, rationality, global novelty, or a global construction obstruction is made.
