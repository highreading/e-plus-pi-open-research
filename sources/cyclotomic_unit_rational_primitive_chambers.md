> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primitive chambers for rational cyclotomic-unit slopes

Checked: 2026-08-26 UTC

## Verdict

Let



$$
K=\mathbb Q(\zeta_{20})^+,
 \qquad \Theta_d=-i\Lambda_{5,d},
 \qquad s=e+\pi,
 \tag{1}
$$



and consider



$$
\theta_d=u_3^{m_3(d)}u_7^{m_7(d)}u_9^{m_9(d)},
 \qquad
 \mathbf m(d)=d\mathbf r+O(1),
 \qquad \mathbf r\in\mathbb Q^3.
 \tag{2}
$$



Put



$$
T_d=\operatorname {Tr}_{K/\mathbb Q}(\theta_d\Theta_d)
                =a_d s+b_d.
 \tag{3}
$$



The raw trace diverges exponentially on every rational slope outside the
quadratic-subfield line.  That statement alone does not survive rational
gcd division.  This note gives the exact stronger conclusion that does.

Let $\mu_k(\mathbf r)$ be the four unit-height rates defined in (14)
below, in embedding order $k=1,3,7,9$, and put
$L=\log\varphi$.  The only rational slopes not ruled out after primitive
division by the value/coefficient comparison are in the open cone



$$
\boxed{
\begin{aligned}
 \mathcal C={}
 \{\mathbf r\in\mathbb Q^3\setminus\mathcal F:
 &\ \mu_1-\mu_3>L,\\
 &\ \mu_1-\mu_7>L,\\
 &\ \mu_1>\mu_9\},
\end{aligned}}
 \tag{4}
$$



where



$$
\mathcal F=\{(c,c,-c):c\in\mathbb Q\}.
 \tag{5}
$$



More precisely:

* every slope on $\mathcal F$ is already excluded by the exact
  quadratic-ray primitive theorem;
* for every rational $\mathbf r\notin\mathcal F\cup\mathcal C$, each
  eventually nonzero primitive trace is bounded away from zero;
* if the raw value has a strictly larger exponential rate than its
  coefficient on $s$, the primitive form diverges;
* if the two maximal rates are equal outside $\mathcal F$, both maxima
  must come from embedding $9$, and

  

$$
\frac{T_d}{a_d}\longrightarrow2\pi.
  \tag{6}
$$



No conclusion is claimed inside $\mathcal C$.  There the locally small
embedding $1$ dominates the coefficient strongly enough that
$|T_d/a_d|$ decays exponentially.  A primitive no-go in that cone would
require a new lower bound for the primitive coefficient, equivalently an
upper bound for the traced coordinate gcd.  The existing coefficient-ideal
norm and raw-trace estimates do not provide it.

Nothing here proves algebraicity or transcendence of $e+\pi$.

## 1. Exact unit and endpoint rates

Let $\sigma_k$ be the real embedding
$\zeta_{20}\mapsto\zeta_{20}^k$, for $k=1,3,7,9$.  At the distinguished
embedding put



$$
\boldsymbol\ell=(\log u_3,\log u_7,\log u_9)^t,
          \qquad \mathbf h=(1,1,-1)^t.
 \tag{7}
$$



All entries of $\boldsymbol\ell$ are positive and linearly independent
over $\mathbb Q$.  This follows from the exact unit identities



$$
\frac{u_3u_7}{u_9}=\varphi^2,
 \qquad
 N_{K/\mathbb Q(\sqrt5)}(u_3)
 =N_{K/\mathbb Q(\sqrt5)}(u_7)=-\varphi^2,
 \qquad N_{K/\mathbb Q(\sqrt5)}(u_9)=1,
 \tag{8}
$$



together with the signed Galois action.  Explicitly, if
$u_3^au_7^bu_9^c=\pm1$, the relative norm first gives $a+b=0$.
Put $\beta=-\log(u_3/u_7)>0$ and $\gamma=\log u_9>0$ at the
distinguished embedding.  The original relation and its $\sigma_3$-image,
using
$\sigma_3(u_3/u_7)=-u_9$ and
$\sigma_3(u_9)=-u_7/u_3$, give
$-a\beta+c\gamma=0$ and $a\gamma+c\beta=0$.  Their determinant is
$-\beta^2-\gamma^2\ne0$, so $a=b=c=0$.  A rational relation among
the entries of $\boldsymbol\ell$ would therefore give a forbidden unit
relation after clearing denominators.  In particular,



$$
L=\log\varphi
                           =\frac12\boldsymbol\ell^t\mathbf h.
 \tag{9}
$$



Ignoring embedding signs, the exact exponent-action matrices are



$$
\begin{aligned}
 A_1&=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\\
 A_3&=\begin{pmatrix}-1&-1&-1\\0&0&1\\1&0&0\end{pmatrix},\\
 A_7&=\begin{pmatrix}0&0&1\\-1&-1&-1\\0&1&0\end{pmatrix},\\
 A_9&=\begin{pmatrix}0&1&0\\1&0&0\\-1&-1&-1\end{pmatrix}.
\end{aligned}
 \tag{10}
$$



The coefficient on $s$ in $\Theta_d$ is the element of the quadratic
subfield



$$
U_d=2A_d(1)A_d(\eta)A_d(\bar\eta),
 \tag{11}
$$



and at all four real embeddings



$$
\sigma_k(U_d)
                           =2(-1)^de^{-2}+o(1).
 \tag{12}
$$



Thus the exponential rates of the four summands in the raw coefficient
$a_d=\sum_k\sigma_k(\theta_d)\sigma_k(U_d)$ are



$$
\mu_k(\mathbf r)
                           =\boldsymbol\ell^tA_k\mathbf r.
 \tag{13}
$$



For later reference, write



$$
M(\mathbf r)=\max_k\mu_k(\mathbf r).
 \tag{14}
$$



The endpoint factors in $\Theta_d$ have exponential exponents
$(-1,1,1,0)L$.  Therefore the raw-value rates are



$$
\begin{aligned}
 \lambda_1&=\mu_1-L,\\
 \lambda_3&=\mu_3+L,\\
 \lambda_7&=\mu_7+L,\\
 \lambda_9&=\mu_9,
\end{aligned}
 \qquad
 R(\mathbf r)=\max_k\lambda_k(\mathbf r).
 \tag{15}
$$



The endpoint summands at $1,3,7$ have an additional factor $d^{-1}$,
whereas the $9$-summand satisfies



$$
\sigma_9(\Theta_d)=4(-1)^d\pi e^{-2}+o(1).
 \tag{16}
$$



Every leading constant is nonzero after the finitely many residue classes
and bounded integer offsets are separated.

## 2. Uniqueness of the two dominant embeddings

Suppose $\mathbf r\in\mathbb Q^3\setminus\mathcal F$.  A coefficient-rate
tie $\mu_i=\mu_j$ gives



$$
\boldsymbol\ell^t(A_i-A_j)\mathbf r=0.
 \tag{17}
$$



By the rational independence of $\boldsymbol\ell$, this is a vector
equation over $\mathbb Q$.  Its exact solution table is



$$
\begin{array}{c|c}
 \text{pair}&\text{rational solution set}\\ \hline
 (1,3)&\{0\}\\
 (1,7)&\{0\}\\
 (1,9)&\mathcal F\\
 (3,7)&\mathcal F\\
 (3,9)&\{0\}\\
 (7,9)&\{0\}.
\end{array}
 \tag{18}
$$



Since $0\in\mathcal F$, all four $\mu_k$'s are distinct outside
$\mathcal F$.  Hence the coefficient has a unique exponentially dominant
embedding and is eventually nonzero.

The rational raw-rate wall table was classified previously: every rational
tie among the $\lambda_k$'s lies on $\mathcal F$.  Thus outside
$\mathcal F$ the raw value also has a unique dominant embedding.  If
$j$ maximizes $\mu_j$, $i$ maximizes $\lambda_i$, and



$$
\Delta(\mathbf r)=R(\mathbf r)-M(\mathbf r),
 \tag{19}
$$



then the endpoint expansions give



$$
\left|\frac{T_d}{a_d}\right|
   \asymp_{\mathbf r,O(1)}
      d^{-p_i}\exp\{d\Delta(\mathbf r)\},
 \qquad
 p_i=\begin{cases}1,&i=1,3,7,\\0,&i=9.
       \end{cases}
 \tag{20}
$$



This equation concerns the raw quotient, not yet the primitive form.

## 3. Exact classification of the negative-gap cone

If $j=3$, then
$R\geq\lambda_3=\mu_3+L=M+L$, so $\Delta\geq L>0$.  The same holds
for $j=7$.  If $j=9$, then
$R\geq\lambda_9=\mu_9=M$, so $\Delta\geq0$.  Consequently
$\Delta<0$ forces $j=1$.

When $j=1$, all four inequalities $\lambda_k<M=\mu_1$ reduce to



$$
\mu_1-\mu_3>L,
 \qquad
 \mu_1-\mu_7>L,
 \qquad
 \mu_1>\mu_9;
 \tag{21}
$$



the inequality $\mu_1-L<\mu_1$ is automatic.  Conversely (21) makes
$\mu_1$ the unique coefficient maximum and makes every raw rate smaller
than it.  Therefore



$$
\boxed{\Delta(\mathbf r)<0
                    \quad\Longleftrightarrow\quad
                    \mathbf r\in\mathcal C.}
 \tag{22}
$$



This proves that (4) is exactly, rather than merely sufficiently, the
unresolved open cone for the quotient method.

## 4. Zero gap outside the quadratic line

Assume $\Delta=0$.  Equality of the two unique maxima means
$\lambda_i=\mu_j$, or



$$
\boldsymbol\ell^t
 \left((A_i-A_j)\mathbf r+\frac{a_i}{2}\mathbf h\right)=0,
 \qquad (a_1,a_3,a_7,a_9)=(-1,1,1,0).
 \tag{23}
$$



For rational $\mathbf r$, independence again turns (23) into a rational
vector equation.  Solving all sixteen ordered pairs gives:

* the identity family $(i,j)=(9,9)$, with arbitrary $\mathbf r$;
* isolated or one-dimensional solutions contained in $\mathcal F$;
* no other solutions.

The complete exact table is in the certificate.  Hence outside
$\mathcal F$, a zero gap forces



$$
i=j=9.
 \tag{24}
$$



Both the value and its $s$-coefficient are then led by the same single
embedding.  The unit value, including every fixed bounded-offset factor,
cancels in their quotient.  From (12) and (16),



$$
\frac{T_d}{a_d}\longrightarrow
 \frac{4(-1)^d\pi e^{-2}}{2(-1)^de^{-2}}=2\pi.
 \tag{25}
$$



Because a bounded integer offset takes only finitely many values, the same
limit and a uniform positive lower bound hold without passing to an
eventually constant offset.

## 5. Passage to primitive rational forms

Choose any positive integer $q_d$ clearing the two rational coefficients
of (3), write



$$
q_dT_d=\mathcal A_ds+\mathcal B_d,
                       \qquad g_d=\gcd(\mathcal A_d,\mathcal B_d),
 \tag{26}
$$



and let



$$
\widehat L_d
                         =\frac{\mathcal A_d}{g_d}s
                           +\frac{\mathcal B_d}{g_d}.
 \tag{27}
$$



If $\mathcal A_d\ne0$, then



$$
\frac{\widehat L_d}{\mathcal A_d/g_d}=\frac{T_d}{a_d},
             \qquad
             |\widehat L_d|\geq\left|\frac{T_d}{a_d}\right|.
 \tag{28}
$$



If $\mathcal A_d=0$ and the pair is nonzero, the primitive form is a nonzero
integer constant of modulus one.

For $\Delta>0$, (20) and (28) make the primitive form diverge.  For
$\Delta=0$ outside $\mathcal F$, (25) and (28) give a limiting lower
bound $2\pi+o(1)$.  Slopes in $\mathcal F$ were independently resolved
by the quadratic-ray primitive theorem.  This proves the verdict outside
$\mathcal C$.

Inside $\mathcal C$, (20) instead gives an exponentially decaying
$|T_d/a_d|$.  Equation (28) then supplies no lower bound because the
nonzero integer $|\mathcal A_d/g_d|$ may grow.  A proof would have to quantify that
growth or, equivalently, prevent $g_d$ from absorbing almost all of the
cleared $s$-coefficient.  No such all-degree content theorem is asserted.

The exact matrices, the coefficient-tie table (18), all ordered zero-gap
solutions in (23), and the logical cone classification are reproduced in
<scripts/cyclotomic_unit_rational_primitive_chambers.py> and
<results/cyclotomic_unit_rational_primitive_chambers.json>.
