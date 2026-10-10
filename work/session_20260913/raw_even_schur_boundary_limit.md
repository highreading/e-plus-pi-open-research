> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An explicit Schur boundary limit and a failure of strong model-space convergence

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review requested.

This note continues the independently reviewed raw_dual_factor_accessory_and_boundary_operator.md. It identifies the exact limits of the first boundary data and distinguishes weak, strong, and norm convergence. It does not identify the limit of the varying actual solution.

Throughout $m\ge1$, $n=2m$,


$$
F_m(z)=\Phi_m^*(-z^2),\quad
\Psi_m(z)=(-1)^m\Phi_m(-z^2),\quad
a_m=\frac{m}{2m+1}.
$$


The superscript indicating the weight parameter $m$ on $\Phi_j$ is suppressed.

## 1. The explicit Schur limit

Define


$$
\beta_m(z)=(-1)^m\frac{\Psi_m(z)}{F_m(z)}
          =\frac{\Phi_m(-z^2)}{\Phi_m^*(-z^2)}.
$$


Each $\beta_m$ is a finite inner function, is even, and satisfies


$$
\beta_m(0)=\frac12,\qquad \|\beta_m\|_{H^2}=1.             \tag{1}
$$


The constant term follows directly from
$\Phi_m(0)=(m)_m/(m+1)_m=1/2$.

The circular-binomial recurrence gives, for $1\le j\le m$,


$$
B_j^{(m)}(w)
 =\frac{wB_{j-1}^{(m)}(w)+a_{j,m}}
        {1+a_{j,m}wB_{j-1}^{(m)}(w)},\qquad
a_{j,m}=\frac{m}{m+j},\quad B_0^{(m)}=1,                 \tag{2}
$$


where $B_j^{(m)}=\Phi_j/\Phi_j^*$.

For every fixed $r<1$, the last $K$ parameters in (2) tend uniformly to $1/2$ as $m\to\infty$, for fixed $K$. The corresponding Möbius maps are uniformly continuous on $|w|\le r,|B|\le1$, since their denominators are bounded away from zero.

Here is a uniform contraction argument that also controls the unknown earlier state. The map


$$
T_a(B)=\frac{wB+a}{1+awB}
$$


is the composition of multiplication by $w$ and a disk automorphism. Multiplication by $w$ has hyperbolic Lipschitz constant at most $r$: its infinitesimal factor is
$r(1-|B|^2)/(1-r^2|B|^2)\le r$. For $a=1/2$, one application sends the closed unit disk into the compact disk of radius $(r+1/2)/(1+r/2)<1$. All subsequent iterates therefore approach its fixed point uniformly at a geometric rate in hyperbolic distance. Comparing the last $K$ actual maps with these constant maps, first sending $m\to\infty$ and then $K\to\infty$, proves local uniform convergence.

Solving the fixed-point equation
$wB^2+2(1-w)B-1=0$, with $B(0)=1/2$, gives


$$
\boxed{\displaystyle
\beta_m(z)\longrightarrow
\beta(z)=\frac{1}{1+z^2+\sqrt{1+z^2+z^4}}.}              \tag{3}
$$


The square root is the analytic branch equal to one at zero. Its polynomial has no zero in the open unit disk; its zeros lie on the unit circle. The denominator in (3) does not vanish in the disk, also directly from the fixed-point equation.

The convergence is also weak in $H^2$, because the coefficients converge and the norms in (1) are uniformly bounded. The limit is Schur but is not inner:


$$
\beta(1)=\frac1{2+\sqrt3}<1.
$$


It extends analytically through an arc around $z=1$, where its boundary modulus remains strictly below one, while its boundary modulus is at most one elsewhere. Consequently


$$
b:=\|\beta\|_{H^2}<1.                                  \tag{4}
$$


In particular the convergence in (3) is not strong in $H^2$, and


$$
\|\beta_m-\beta\|_{H^2}\longrightarrow\sqrt{1-b^2}>0.    \tag{5}
$$



## 2. The model-space projections have only a nonprojective weak limit

Let


$$
S_m=\{p/F_m:\deg p\le n\},\qquad \vartheta_m=z\beta_m.
$$


Then


$$
S_m=H^2\ominus\vartheta_mH^2.                           \tag{6}
$$


For example, direct boundary integration makes each $p/F_m$ orthogonal to $\vartheta_mH^2$: all powers remaining after cancellation are strictly negative. Both sides have dimension $n+1$, since $\vartheta_m$ is a finite Blaschke product of degree $n+1$. This proves (6) without changing the positive-weight normalization.

Writing $P_m$ for this projection,


$$
P_m=I-M_{\vartheta_m}M_{\vartheta_m}^*.
$$


On polynomial inputs the adjoints $M_{\vartheta_m}^*$ converge strongly by coefficient convergence; their uniform contraction bounds extend this to every $H^2$ input. Thus


$$
P_m\ \longrightarrow\
\mathcal P=I-M_{z\beta}M_{z\beta}^*
\quad\hbox{in the weak operator topology}.              \tag{7}
$$


Equivalently the reproducing kernels converge locally to


$$
\frac{1-z\overline w\,\beta(z)\overline{\beta(w)}}
     {1-z\overline w}.
$$



This is not strong convergence of projections. Indeed,


$$
P_mz=z-\frac12z\beta_m=:k_m,\qquad \|k_m\|^2=\frac34,
$$


whereas


$$
\mathcal Pz=z-\frac12z\beta=:k,\qquad
\|k\|^2=\frac12+\frac14b^2<\frac34.                      \tag{8}
$$


In particular $\mathcal P$ is not a projection: its quadratic form at $z$ is $3/4$, while the squared norm in (8) is smaller. The increasing degree does not make these spaces strongly exhaust the ambient Hardy space.

## 3. The exact quadratic correction and its precise topology

Use $u\otimes v$ for the rank-one map $f\mapsto\langle f,v\rangle u$, with the inner product linear in its first argument. Extend the actual monomial correction to $H^2$ by precomposing with $P_m$.

The reviewed quadratic identity becomes


$$
\mathcal E_{2,m}=a_m(1\otimes\beta_m).                   \tag{9}
$$


The sign $(-1)^m$ has been absorbed into $\beta_m$. Both the vector $\beta_m$ and the constant function belong to $S_m$, so (9) is exactly the natural extension of the finite operator.

For each fixed $f\in H^2$, weak convergence in (3) gives


$$
\mathcal E_{2,m}f\longrightarrow
\frac12\langle f,\beta\rangle\,1
\quad\hbox{in }H^2.
$$


However


$$
\left\|\mathcal E_{2,m}-\frac12(1\otimes\beta)\right\|
\longrightarrow\frac12\sqrt{1-b^2}>0.                  \tag{10}
$$


Thus the quadratic correction converges strongly, but not in operator norm. The degree-two exponential correction is half of (9), because of $2!$.

## 4. The cubic correction already fails strong convergence

There is an equally explicit next identity:


$$
\boxed{\displaystyle
\mathcal E_{3,m}
=a_m\big[1\otimes S^*\beta_m+k_m\otimes\beta_m\big],
\quad k_m=z-\tfrac12z\beta_m.}                          \tag{11}
$$


Here $S^*$ is the Hardy backward shift.

To verify it with the actual measures, the only unmatched Laurent exponent in $z^3p\overline q$ is $n+2$. The exponent $n+3$ is odd and its moments vanish in both measures. From the quadratic identity,


$$
c_m(\mu-\nu)(z^{n+2})=(-1)^m a_m.
$$


Therefore the cubic difference pairing is


$$
(-1)^m a_m(p_{n-1}\overline{q_0}+p_n\overline{q_1}).
$$


For $f=p/F_m$, the coefficient identities are


$$
(-1)^m p_n=\langle f,\beta_m\rangle,\qquad
(-1)^m p_{n-1}=\langle f,S^*\beta_m\rangle.
$$


The second follows by pairing $zf$ with $\Psi_m/F_m$; the possible additional term vanishes because $F_m'(0)=0$. For the test vector $q/F_m$, its first two Taylor coefficients are $q_0,q_1$, again because $F_m'(0)=0$. Their Riesz vectors are $1$ and $P_mz=k_m$. These facts prove (11), with the stated sign and scale.

All vectors in (11) lie in $S_m$. Their parities also show


$$
\|\mathcal E_{3,m}\|=a_m\sqrt{3}/2.
$$


There is a weak operator limit


$$
\mathcal E_{3,\infty}
=\frac12\big[1\otimes S^*\beta+k\otimes\beta\big].
$$


It is not a strong operator limit. On the single fixed input one,


$$
\mathcal E_{3,m}1=\frac{a_m}{2}k_m,\qquad
\mathcal E_{3,\infty}1=\frac14k,
$$


and (5) gives


$$
\|\mathcal E_{3,m}1-\mathcal E_{3,\infty}1\|
\longrightarrow\frac18\sqrt{1-b^2}>0.                  \tag{12}
$$


The cubic exponential contribution is (11) divided by $3!$.

## 5. What these limits do and do not establish

Equations (3), (9), and (11) supply explicit boundary data with all normalization constants retained. They also exhibit the obstruction to passing local limits through the full actual operator equation: even a fixed input does not have strong convergence under every low-degree correction.

There is an even simpler warning for varying inputs. The bounded sequence $f_m=\beta_m\in S_m$ converges locally to $\beta$, but


$$
\mathcal E_{2,m}f_m=a_m\,1\longrightarrow\tfrac12\,1,
$$


whereas applying the fixed-input limit operator to $\beta$ gives
$\tfrac12b^2\,1$. This example is a sequence in the exact model spaces, not a claim about the actual solved factors $R_n$.

A valid limiting equation for the actual factors must retain the boundary coordinates or establish a stronger joint convergence theorem. The uniform factorial approximation from the reviewed boundary-operator note remains useful, but its finite-rank pieces cannot be replaced by their local limits without this additional work.

