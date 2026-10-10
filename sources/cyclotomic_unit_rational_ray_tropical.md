> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational-ray tropical classification for the cyclotomic-unit trace

Checked: 2026-08-26 UTC

## Verdict

Let



$$
K=\mathbb Q(\zeta _{20})^+,
 \qquad \Theta_d=-i\Lambda_{5,d},
 \qquad s=e+\pi,
 \tag{1}
$$



and put



$$
\theta_d=u_3^{m_3(d)}u_7^{m_7(d)}u_9^{m_9(d)},
 \qquad
 T_d=\operatorname {Tr}_{K/\mathbb Q}(\theta_d\Theta_d).
 \tag{2}
$$



Suppose



$$
(m_3(d),m_7(d),m_9(d))=d\mathbf r+O(1),
       \qquad \mathbf r\in\mathbb Q^3.
 \tag{3}
$$



Then the **raw rational trace** is eventually bounded away from zero.  More
precisely:

* if $\mathbf r$ is not on the quadratic-subfield line

  

$$
\mathcal F=\{(c,c,-c):c\in\mathbb Q\},
  \tag{4}
$$



  one of the four embedding summands is uniquely exponentially dominant,
  and $|T_d|$ grows exponentially;
* on $\mathcal F$, bounded offsets outside the quadratic subfield leave a
  nonzero anti-fixed leading term, while offsets in the quadratic subfield
  cancel that term exactly but leave a nonzero fixed term.  The latter is
  exponentially growing unless $c=0$, in which case it tends, up to the
  parity sign, to a nonzero constant.

Thus no affine-linear exponent triple, and no exponent triple within
$O(1)$ of a fixed rational slope, produces exponentially stronger signed
cancellation in the raw trace.  Baker's theorem, the $S$-unit theorem,
and the Subspace Theorem are not needed in this regime: exact Galois-unit
relations classify all rational resonances, and the endpoint asymptotics
resolve them.

This is deliberately separate from rational primitivization.  If
$q_dT_d=A_ds+B_d$ is integral and
$g_d=\gcd(A_d,B_d)$, the primitive form is
$(q_d/g_d)T_d$.  The theorem below gives no upper bound for $g_d/q_d$.
Consequently it is a raw-trace no-cancellation theorem, not an all-ray
primitive no-go and not a result about the arithmetic nature of $e+\pi$.

## 1. Exact Galois action and multiplicative independence

Let $\sigma_k$ denote the real embedding $w=\zeta _{20}\mapsto w^k$,
where $k=1,3,7,9$.  Exact cyclotomic-unit arithmetic gives



$$
\begin{array}{c|ccc}
 &u_3&u_7&u_9\\ \hline
\sigma _1&u_3&u_7&u_9\\
\sigma _3&u_9/u_3&-1/u_3&-u_7/u_3\\
\sigma _7&-1/u_7&u_9/u_7&-u_3/u_7\\
\sigma _9&-u_7/u_9&-u_3/u_9&1/u_9.
\end{array}
\tag{5}
$$



In particular,



$$
\frac{u_3u_7}{u_9}=\varphi^2,
                 \qquad \varphi=\frac{1+\sqrt5}{2}.
\tag{6}
$$



The three units are multiplicatively independent modulo torsion.  Here is
a short proof that will also justify the rational-wall computation.  Their
relative norms to $F=\mathbb Q(\sqrt5)$ are



$$
N_{K/F}(u_3)=N_{K/F}(u_7)=-\varphi^2,
 \qquad N_{K/F}(u_9)=1.
\tag{7}
$$



If $u_3^au_7^bu_9^c=\pm1$, (7) gives $a+b=0$.  Put



$$
\beta=-\log(u_3/u_7)>0,
 \qquad \gamma=\log u_9>0
\tag{8}
$$



at the distinguished embedding.  The first relation and its
$\sigma _3$-image, using (5), give



$$
-a\beta+c\gamma=0,
                 \qquad a\gamma+c\beta=0.
\tag{9}
$$



Since the determinant is $-\beta^2-\gamma^2\ne0$, one has
$a=b=c=0$.  The inequalities in (8) follow directly from monotonicity of
$\sin x$ on $(0,\pi/2)$.

Set



$$
\boldsymbol\ell=(\log u_3,\log u_7,\log u_9)^t
\tag{10}
$$



at the distinguished embedding; all three entries are positive.  It
follows from multiplicative independence that their coordinates are
linearly independent over $\mathbb Q$: a rational relation, after
clearing denominators, would make a unit monomial have distinguished
absolute value one and hence be the algebraic number $1$.

Ignoring the signs in (5), write the exponent-action matrices as



$$
\begin{aligned}
 A_1&=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\\
 A_3&=\begin{pmatrix}-1&-1&-1\\0&0&1\\1&0&0\end{pmatrix},\\
 A_7&=\begin{pmatrix}0&0&1\\-1&-1&-1\\0&1&0\end{pmatrix},\\
 A_9&=\begin{pmatrix}0&1&0\\1&0&0\\-1&-1&-1\end{pmatrix}.
\end{aligned}
\tag{11}
$$



Thus



$$
\log|\sigma_k(\theta_d)|
          =\boldsymbol\ell^tA_k\mathbf m(d).
\tag{12}
$$



## 2. The four endpoint summands

Write



$$
t_{d,k}=\sigma_k(\Theta_d).
\tag{13}
$$



The already proved endpoint expansion, specialized to the four real
embeddings, has the following sharper form.  Along each residue class of
$d$ modulo $5$,



$$
\begin{aligned}
 t_{d,1}&=c_{1,r}\frac{\varphi^{-d}}d
             \{1+O(d^{-1})\},\\
 t_{d,3}&=c_{3,r}\frac{\varphi^d}d
             \{1+O(d^{-1})\}+O(1),\\
 t_{d,7}&=-c_{3,r}\frac{\varphi^d}d
             \{1+O(d^{-1})\}+O(1),\\
 t_{d,9}&=4(-1)^d\pi e^{-2}+o(1),
\end{aligned}
\qquad c_{1,r}c_{3,r}\ne0.
\tag{14}
$$



For clarity, (14) does not add a numerical hypothesis.  The first three
lines are the endpoint formula



$$
\frac{2ie^{-3/2}}d\rho_k^d
 \left\{\sin\!\left(\frac{(d+2)\pi k}{5}
        +\frac12\tan\frac{\pi k}{5}\right)+O(d^{-1})\right\},
\tag{15}
$$



after multiplication by the fixed nonzero factors in $\Theta_d$.  The
sine has a positive minimum on the five residue classes, by the previously
proved algebraic-number-versus-$\pi$ argument.  The opposite leading
signs at $3,7$ follow from the fixed/anti-fixed decomposition
$\Theta_d=X_d+Y_d$.

For the last line, $t_{d,1}=o(1)$ and



$$
X_d=2A_d(\eta)A_d(\bar\eta)
        \{A_d(1)s-E_d(1)\}
     =2(-1)^d\pi e^{-2}+o(1)
\tag{16}
$$



at both embeddings of $F$.  Since
$2X_d=t_{d,1}+t_{d,9}$, the fourth line of (14) follows.  The same
identity at the other embedding gives



$$
t_{d,3}+t_{d,7}
                    =4(-1)^d\pi e^{-2}+o(1).
\tag{17}
$$



In particular every leading constant used below is nonzero, uniformly
after the finitely many residue classes are separated.

## 3. All pairwise walls and their rational points

The raw endpoint exponential exponents in the order $1,3,7,9$ are



$$
(a_1,a_3,a_7,a_9)=(-1,1,1,0).
\tag{18}
$$



Put $\mathbf h=(1,1,-1)^t$.  By (6),
$\log\varphi=\boldsymbol\ell^t\mathbf h/2$.  The four tropical rates
at slope $\mathbf r\in\mathbb R^3$ are therefore



$$
\lambda_k(\mathbf r)
   =\boldsymbol\ell^t
       \left(A_k\mathbf r+\frac{a_k}{2}\mathbf h\right).
\tag{19}
$$



Equations



$$
\boldsymbol\ell^t
 \left((A_i-A_j)\mathbf r
       +\frac{a_i-a_j}{2}\mathbf h\right)=0
\tag{20}
$$



are the six real pairwise walls.  They, together with the condition that
the common value is maximal, give the complete tropical complex.

For rational $\mathbf r$, independence of the entries of
$\boldsymbol\ell$ turns (20) into a vector equation over $\mathbb Q$.
Solving it gives the exact table



$$
\begin{array}{c|c}
 \text{equal pair}&\text{rational slope set}\\ \hline
 (1,3)&\{(1/2,1/2,-1/2)\}\\
 (1,7)&\{(1/2,1/2,-1/2)\}\\
 (1,9)&\varnothing\\
 (3,7)&\{(c,c,-c):c\in\mathbb Q\}\\
 (3,9)&\{(1/4,1/4,-1/4)\}\\
 (7,9)&\{(1/4,1/4,-1/4)\}.
\end{array}
\tag{21}
$$



Thus every rational resonance lies on $\mathcal F$.  On that line,



$$
\frac1{\log\varphi}
 (\lambda_1,\lambda_3,\lambda_7,\lambda_9)
       =(-1+2c,\,1-2c,\,1-2c,\,2c).
\tag{22}
$$



The rational part of the **upper** tropical wall is consequently



$$
\{(c,c,-c):c\leq1/4\}.
\tag{23}
$$



For $c<1/4$, the maximal pair is $(3,7)$; at $c=1/4$, embedding
$9$ joins it.  The lower equalities at $c=1/2$ never attain the
maximum because the $9$-term is larger.

Since every unit has norm one and $\sum_k a_k=1$,



$$
\sum_k\lambda_k(\mathbf r)=\log\varphi.
\tag{24}
$$



Hence the largest rate is always at least
$\tfrac14\log\varphi>0$.

## 4. Nonresonant rational rays

Let $\mathbf r\in\mathbb Q^3\setminus\mathcal F$.  By (21) the four
rates are distinct, so one embedding $k_*$ has a unique largest rate.
The bounded offset in (3) changes its summand by one of only finitely many
nonzero unit factors.  Separating also the five residue classes and using
(14), one obtains



$$
|T_d|\asymp_{\mathbf r,O(1)}
 \begin{cases}
  d^{-1}\exp(d\lambda_{k_*}(\mathbf r)),&k_*=1,3,7,\\
  \exp(d\lambda_9(\mathbf r)),&k_*=9.
 \end{cases}
\tag{25}
$$



All other summands have an exponential gap.  Equations (24)--(25) prove
exponential divergence, without a lower bound for a linear form in
logarithms.

## 5. Exact resolution of the resonant line

Now let $\mathbf r=c\mathbf h$.  On any subsequence on which the bounded
integer offset is fixed, write



$$
\theta_d=\varphi^{2n_d}\xi,
             \qquad n_d=cd+O(1),
             \qquad \xi\in\langle u_3,u_7,u_9\rangle.
\tag{26}
$$



The exact action (5) and multiplicative independence show that



$$
u_3^{b_3}u_7^{b_7}u_9^{b_9}\in F
   \quad\Longleftrightarrow\quad
        (b_3,b_7,b_9)=(b,b,-b).
\tag{27}
$$



Suppose first that $\xi\notin F$.  At the growing embedding of $F$,
the tied $(3,7)$-sum is exactly



$$
\varphi^{-2n_d}
 \{(\sigma_3\xi+\sigma_7\xi)X_d
    +(\sigma_3\xi-\sigma_7\xi)Y_d\}.
\tag{28}
$$



The coefficient of $Y_d$ is nonzero by (27), and (14) makes its leading
constant nonzero on every residue class.  At the other embedding, the
$9$-summand has nonzero limit before multiplication by
$\varphi^{2n_d}$.  Therefore



$$
|T_d|\asymp
 \begin{cases}
  d^{-1}\varphi^{(1-2c)d},&c<1/4,\\
  \varphi^{2cd},&c\geq1/4.
 \end{cases}
\tag{29}
$$



At $c=1/4$, the three terms have the same exponential rate, but the
$3,7$ pair has the extra factor $d^{-1}$; the nonzero $9$-term is
dominant.  Thus this triple tropical resonance is not an asymptotic signed
cancellation.

If $\xi\in F$, the anti-fixed term cancels identically.  Formula (16) at
the two embeddings of $F$ then yields



$$
|T_d|\asymp \varphi^{2|c|d}
                  \quad(c\ne0).
\tag{30}
$$



When $c=0$, the possible $\xi$'s form a finite set of powers
$\varphi^{2b}$, and more precisely



$$
T_d=4(-1)^d\pi e^{-2}
       \operatorname {Tr}_{F/\mathbb Q}(\xi)+o(1).
\tag{31}
$$



The trace in (31) is positive and nonzero.  Equations (29)--(31) resolve
every rational upper-wall resonance, including its bounded translates.

## 6. Scope of Diophantine lower-bound theorems

For a fixed nonresonant rational slope, the leading rate has a fixed
positive gap, so Baker-type estimates are superfluous.  On every rational
wall, (21) reduces the multiplier to the quadratic-subfield direction and
(28)--(31) give an exact algebraic cancellation test.  In particular, no
unresolved small linear form in logarithms remains on a rational ray.

The situation changes if slopes are allowed to vary with $d$, approach
one of the generally irrational real walls, or have unbounded sublinear
deviations.  Quantitative logarithmic-form estimates could then help
control how closely unit monomials approach a wall.  Such estimates still
would not bound the common integer divisor of the two traced coordinates.
Likewise, an $S$-unit or Subspace-Theorem exceptional-subspace statement
does not by itself control the factorial denominator clearing or the
primitive gcd.  Those regimes and that gcd remain outside this theorem.

The exact field identities, action matrices, rational wall solutions, and
subfield criterion are reproduced in
<scripts/cyclotomic_unit_rational_ray_tropical.py> and
<results/cyclotomic_unit_rational_ray_tropical.json>.
