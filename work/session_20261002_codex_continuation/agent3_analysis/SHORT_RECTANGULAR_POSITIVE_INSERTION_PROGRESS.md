> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Short rectangular kernel: positive determinant insertions

Author: Agent 3, 2026-10-02. The fresh gate is SHORT_RECTANGULAR_ANALYTIC_GATE.md. This is an original analytic proof of the complete determinant, not an audit of Root's finite receipts.

Let rho=mu-delta_{-1}, with mu the shifted-exponential square pushforward, and let sigma be the COMPLETE compact mixed measure

    dsigma(y)=[exp(sqrt(y))+4/(1+y)]dy/[2sqrt(y)], 0<y<1.

Root's k by 2k upper block is rho(y^(i+j)); its lower complete block is sigma(y^(i+j)), 0<=i<k, 0<=j<2k. Entrywise the latter is eC+R+S V. Subtracting e times each upper row from its corresponding lower row gives det[C;sigma moments]=det[C;R+S V] exactly. Write its determinant Delta_k=a_k+b_k S and actual center c_k=-a_k/b_k.

For x=(x_1,...,x_k), define Q_x(y)=product_i(y-x_i) and

    F_k(x)=det[ rho(y^(i+j)Q_x(y)) ]_(0<=i,j<k).

Repeated Andreief, or determinant multilinearity followed by the two Vandermonde factorizations, gives exactly

    Delta_k=(-1)^k/k! integral_[0,1]^k Vandermonde(x)^2 F_k(x) d sigma^k.    (1)

The sign is (-1)^(k^2)=(-1)^k from product_(a,i)(x_i-t_a). The actual affine S derivative adds delta_{-1} to the LOWER compact measure while retaining the fixed rho above. Its repeated lower atom terms vanish by the Vandermonde. Thus

    b_k=(-1)^k/(k-1)! integral_[0,1]^(k-1) Vandermonde(x)^2
          product_i(1+x_i)^2 F_k(x_1,...,x_(k-1),-1) d sigma^(k-1).       (2)

The insertion factor at -1 cancels the upper atom:

    F_k(x,-1)=det M_[mu·(y+1)·product_(i<k)(y-x_i),k].

Equations (1)--(2) retain BOTH actual exponential and arctangent endpoint contributions in sigma. The determinants inside the integrals are not replaced by unsigned modulus ensembles; their positivity is established below.

## Uniform finite-dimensional coercivity

For any k-1 nodes x_i in [-1,1], put Q(y)=product_(i<k)(y-x_i), nu=Q rho. On I=[k^2,4k^2],

    Q(y)>=(k^2-1)^(k-1),
    dmu_tail/dy>=exp(-2k-1)/(4k).

For every polynomial p of degree <k, the Legendre evaluation kernel on I gives

    integral_I p^2 dy >=3·16^(-(k-1))
        max(|p(-1)|^2,sup_[0,1]|p|^2).

The maximum exterior map value is less than 2 for k>=2, so its conformal factor is less than 4. Hence the positive tail contributes at least

    C_k max(|p(-1)|^2,sup_[0,1]|p|^2),
    C_k=3 exp(-2k-1)(k^2-1)^(k-1)/[4k16^(k-1)].

The absolute negative compact part is at most 2^(k-1)sup_[0,1]|p|^2 and the exterior atom at most 2^(k-1)|p(-1)|^2. For k>=24,

    C_k/2^k > 4/[k(k^2-1)] [(k^2-1)/288]^k
              >=4(3/2)^k/[k(k^2-1)]>1.                              (3)

Here e<3 was used; the last expression is already greater than 1 at k=24 and is increasing for k>7. Therefore nu(p^2)>0 for every nonzero deg p<k, UNIFORMLY over all k-1 node configurations in [-1,1].

For a k-node configuration in [0,1], its Q_x tail has an extra factor at least k^2-1. Its negative compact/atom bound is <=1+2^k. The same inequalities imply rho(Q_x p^2)>0 for all nonzero deg p<k. At a configuration containing -1 the atom is absent and the same estimate applies. Consequently (1)--(2) have signs

    sign Delta_k=sign b_k=(-1)^k,  k>=24,
    S-c_k=Delta_k/b_k>0.

This already proves eventual complete nonzero center and affine-coefficient normality. An all-size proof needs the remaining finite indices handled with certified real bounds, not diagnostic values.

## Uniform insertion-root separation and complete rate

This paragraph records the next proved estimate, to be written out in the final author note. Uniformly over the k-1 nodes in [-1,1], the compression of multiplication by y for nu on degrees <k has every root greater than A=a k^2, where a=1/(48e^4), for all k>=100. The same tail/Legendre estimate on [-1,A] gives

    nu((y-A)p^2)>0.

Indeed the positive tail is at least (k^2-A)C_k times the maximum on [-1,A]. The negative continuous/atom parts are bounded by

    [A(A+1)^(k-1)+(A+1)2^(k-1)] times that maximum.

For A>=2 this is <=3A(A+1)^(k-1), and the resulting positive/negative ratio is at least

    (1-a) exp(2k-4)/(4e a k)>1.

As a function of its final node x_i, F_k is therefore the characteristic product of those separated roots, with a positive Gram determinant prefactor. For x_i in [-1,1],

    exp(-4k/A)<=F_k(x)/F_k(x with x_i=-1)<=1.

Replacing the k nodes successively gives

    exp(-4/a)<=F_k(x)/F_k(-1,...,-1)<=1,

uniformly for all x in [-1,1]^k and k>=100. The reference insertion is the genuinely positive determinant det M_[mu·(y+1)^k,k].

Using (1)--(2), the actual complete error is bounded above and below by constant multiples (independent of k) of the positive reference Christoffel minimum for sigma at -1, degree <k. Comparison with y^(-1/2)dy and the exterior Jacobi/Legendre sum then gives

    log(S-c_k)=-4k log(1+sqrt(2))+O(log k).

The completed statement must retain the final primitive denominator Q_k in

    log|Q_k(S-c_k)|=log Q_k-4k log(1+sqrt(2))+O(log k).

No actual Q growth or favorable gcd is established by this analytic estimate.
