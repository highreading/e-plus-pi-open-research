> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the paired-log algebraic-unit Rivoal family

Checked: 2026-08-26 UTC

## 1. Audited snapshot and verdict

This audit treats the following candidate artifacts as read-only:

* `sources/algebraic_unit_global_norm_rivoal.md`, SHA-256
  `139dfecca71f4d0f980374d4955b330b779193e96c46f69455b680550fee7ff8`;
* `scripts/algebraic_unit_two_log_rivoal_certificate.py`, SHA-256
  `6c1b40f677fb9191bad2e9cc7870812c819ae1c8a640d31796c902d5183e2738`;
* `results/algebraic_unit_two_log_rivoal_certificate.json`, SHA-256
  `3d2264d6b0f3cae92677d3e7c827fff853615b49bf2159e49fed985e74e0f163`;
* `scripts/algebraic_unit_two_log_n5_ideal_content.py`, SHA-256
  `120ea17e9c27a2b0ebaa48e3e651220bfe59f06bc028b6d764dcd0798570bb80`;
* `results/algebraic_unit_two_log_n5_ideal_content_d200.json`, SHA-256
  `d90be1fd2858a99df16c3c2b4efdac63f480c0578348cac0bb2eb1c37b3811f6`.

The mathematics in this frozen snapshot is accepted.  In particular, I
independently verified all of the following.

1. For odd $n\geq5$,
   $\eta=(1+\zeta_n)^{-1}$ is a cyclotomic unit,
   $\bar\eta=1-\eta$, and the distinguished principal logarithms differ
   by $2\pi i/n$.
2. The paired expression has exactly the coefficient and signs asserted
   in the candidate equation (20), and its specialization has coefficient
   $2iA(1)A(\eta)A(\bar\eta)$ on $e+\pi$.
3. On $c=f=0$, the logarithmic pair has the stated nonzero leading
   phase and is $\asymp_n\rho_k^d/d$.  The combined distinguished form
   is therefore eventually nonzero and $\asymp_n\rho_1^d/d$.
4. At every coefficient-field embedding, the branch numerator is $2k$
   while the algebraic target numerator is $2\epsilon$.  Their exact
   mismatch is the candidate equation (41), with sign
   $+2i(\epsilon-k)\pi$.
5. The product over $L_n=\mathbb Q(\zeta_n,i)$ has exponential base
   $B_n>1$ and polynomial power $-2(1+|\mathcal T_n|)$.  For $n=5$
   this is $\varphi^{2d}d^{-6}$.
6. Positive-integer denominator clearing cannot improve this raw relative
   product.  No conclusion is available after division by unbounded
   common algebraic coordinate content, or for the remaining absolute-norm
   blocks at unknown conjugates of a hypothetical algebraic $e+\pi$.
7. In the $n=5$ maximal real subfield, the displayed four elements are
   an integral basis, the $4$ by $8$ Smith matrix computes the complete
   coefficient-content ideal, and the archived degree-$200$ finite pattern
   and strict comparisons with $\varphi^d$ are exact.  They do not imply
   an all-degree content bound.

The candidate establishes a genuine new locally contracting form, followed
by a proved coefficient-field norm-growth obstruction on the edge
$c=f=0$.  It does not prove an absolute-norm obstruction for every target
conjugate, and it does not prove anything about every admissible degree
sequence.  These limitations are correctly material: they are not merely
technical disclaimers.

## 2. Algebraic unit and principal branches

Let



$$
\xi=e^{2\pi i/n},\qquad
 \eta=\frac1{1+\xi},\qquad n\geq5\text{ odd}.
\tag{1}
$$



For odd $n>1$,



$$
\Phi_n(-1)=\Phi_{2n}(1)=1,
\tag{2}
$$



because $2n$ is not a prime power.  Hence $1+\xi$, and therefore its
inverse $\eta$, is an algebraic-integer unit.  Direct algebra gives



$$
\bar\eta=\frac1{1+\xi^{-1}}
 =\frac{\xi}{1+\xi}=1-\eta.
\tag{3}
$$



At the distinguished embedding, with $\theta=\pi/n$,



$$
\eta=\rho e^{-i\theta},\qquad
 \bar\eta=\rho e^{i\theta},\qquad
 \rho=(2\cos\theta)^{-1}<1.
\tag{4}
$$



Both arguments lie strictly between $-\pi$ and $\pi$, so on the
principal branches



$$
\operatorname {Log}(1-\eta)-\operatorname {Log}(1-\bar\eta)
 =\operatorname {Log}(\bar\eta)-\operatorname {Log}(\eta)
 =\frac{2\pi i}{n}.
\tag{5}
$$



The same branch statement is valid at every cyclotomic embedding.  For a
unit residue $k$, choose $-n/2<k<n/2$, and set



$$
x_k=\frac1{1+\xi^k},\qquad y_k=1-x_k=\bar x_k.
\tag{6}
$$



Writing $\theta_k=\pi k/n$, one has



$$
x_k=\rho_ke^{-i\theta_k},\qquad
 y_k=\rho_ke^{i\theta_k},\qquad
 \rho_k=(2\cos\theta_k)^{-1}.
\tag{7}
$$



In particular $\Re x_k=\Re y_k=1/2$, so neither point lies on the
continuation cut $[1,\infty)$, including when $\rho_k>1$.  Therefore



$$
\operatorname {Log}(1-x_k)-\operatorname {Log}(1-y_k)
 =\operatorname {Log}(y_k)-\operatorname {Log}(x_k)
 =\frac{2\pi ik}{n}.
\tag{8}
$$



This verifies the branch input used later; it is not a formal replacement
of $\xi$ without branch control.

## 3. Exact isolation and its sign

Put



$$
R_{\exp}(1)=A(1)e-E(1),qquad
 R_{\log}(x)=A(x)L_x-B(x),
\tag{9}
$$



and suppose



$$
L_\eta-L_{\bar\eta}=i\pi a/b.
\tag{10}
$$



Then direct expansion, with no asymptotics, gives



$$
\begin{aligned}
 &iaA(\eta)A(\bar\eta)R_{\exp}(1)\\
 &\quad+bA(1)\{A(\bar\eta)R_{\log}(\eta)
                 -A(\eta)R_{\log}(\bar\eta)\}\\
 &=iaA(1)A(\eta)A(\bar\eta)(e+\pi)
   -iaA(\eta)A(\bar\eta)E(1)\\
 &\qquad-bA(1)A(\bar\eta)B(\eta)
          +bA(1)A(\eta)B(\bar\eta).
\end{aligned}
\tag{11}
$$



Thus every sign in the candidate equation (20) is correct.  Substituting
$(a,b)=(2,n)$, allowed because $n$ is odd, gives the candidate form



$$
\Lambda_n
 =2iA(\eta)A(\bar\eta)R_{\exp}(1)
 +nA(1)\{A(\bar\eta)R_{\log}(\eta)
          -A(\eta)R_{\log}(\bar\eta)\},
\tag{12}
$$



with coefficient



$$
2iA(1)A(\eta)A(\bar\eta)
\tag{13}
$$



on $e+\pi$.  The independent script checks (11) symbolically and gets
the exact zero residual.

## 4. Endpoint asymptotic and eventual nonvanishing

On the edge $c=f=0$, the exact polynomial is



$$
A_d(x)=(-1)^d\sum_{j=0}^d\frac{(-x)^j}{j!}
 =(-1)^d\left(e^{-x}
 +O_x\left(\frac{|x|^{d+1}}{(d+1)!}\right)\right).
\tag{14}
$$



The accepted integral specializes to



$$
R_d(x)=(-1)^{d+1}x^{d+1}
 \sum_{q=0}^d\frac{(-1)^q}{q!}
 \int_0^1\frac{u^{d-q}}{1-xu}\,du.
\tag{15}
$$



This formula gives a short rigorous endpoint derivation.  For fixed
$x\notin[1,\infty)$, and uniformly for $q\leq d/2$,



$$
\int_0^1\frac{u^{d-q}}{1-xu}\,du
 =\frac1{(d-q+1)(1-x)}+O_x(d^{-2}).
\tag{16}
$$



The part $q>d/2$ is factorially small.  Summing (16), using
$\sum_{q\geq0}(-1)^q/q!=e^{-1}$ and
$\sum(q+1)/q!<\infty$, proves



$$
R_d(x)=\frac{(-1)^{d-1}}{ed}
         \frac{x^{d+1}}{1-x}\{1+O_x(d^{-1})\}.
\tag{17}
$$



This independently verifies the candidate equation (36), including its
sign, $1/e$, and power of $d$.

Put $x=x_k=\rho_ke^{-i\theta_k}$ and
$y=y_k=1-x=\rho_ke^{i\theta_k}$.  Combining (14) and (17), and using



$$
x=\frac12-\frac i2\tan\theta_k,qquad
 y=\frac12+\frac i2\tan\theta_k,
\tag{18}
$$



gives



$$
\begin{aligned}
 D_{d,k}
 &:={A_d(y)R_d(x)-A_d(x)R_d(y)}\\
 &=\frac{2ie^{-3/2}}d\rho_k^d
 \left\{
  \sin\left((d+2)\theta_k+\frac12\tan\theta_k\right)
  +O_n(d^{-1})
 \right\}.
\end{aligned}
\tag{19}
$$



For clarity, the first main term before taking the difference is



$$
\frac{e^{-x}}{ed}\frac{y^{d+1}}x
 =\frac{e^{-3/2}}d\rho_k^d
   e^{i((d+2)\theta_k+\tan\theta_k/2)},
\tag{20}
$$



and the other is its conjugate; this fixes the phase and the sign in
(19).

The sine in (19) is never zero.  If it vanished, then the nonzero algebraic
number $\tfrac12\tan(\pi k/n)$ would equal a rational multiple of
$\pi$, which is impossible because $\pi$ is transcendental.  The first
phase term has only finitely many residue classes modulo $2\pi$ as $d$
varies.  Hence the absolute sines have a positive minimum depending only on
$n$, and



$$
|D_{d,k}|\asymp_n\rho_k^d/d.
\tag{21}
$$



Finally, $A_d(1)=(-1)^d(e^{-1}+o(1))$, while
$R_{\exp}(1)=O((d!d)^{-1})$.  At $k=1$, the second term of (12)
therefore dominates.  This proves both eventual nonvanishing and



$$
|\Lambda_{n,d}|\asymp_n\rho_1^d/d.
\tag{22}
$$



## 5. Every coefficient-field embedding

Because $n$ is odd,
$\mathbb Q(\zeta_n)\cap\mathbb Q(i)=\mathbb Q$.  The embeddings of



$$
L_n=\mathbb Q(\zeta_n,i)
\tag{23}
$$



are therefore indexed by $(k,\epsilon)$, where



$$
\zeta_n\mapsto\zeta_n^k,qquad i\mapsto\epsilon i,qquad
 \epsilon\in\{1,-1\}.
\tag{24}
$$



Expanding the algebraic expression (11), while temporarily holding the
distinguished $s=e+\pi$ fixed, gives



$$
\sigma_{k,\epsilon}(\Lambda_{n,d})
 =\widetilde\Lambda_{d,k,\epsilon}
 +2i(\epsilon-k)\pi A_d(1)A_d(x_k)A_d(y_k),
\tag{25}
$$



where



$$
\widetilde\Lambda_{d,k,\epsilon}
 =2\epsilon iA_d(x_k)A_d(y_k)R_{\exp}(1)
   +nA_d(1)D_{d,k}.
\tag{26}
$$



This verifies both the sign and the distinction between the algebraic
coefficient numerator $2\epsilon$ and the analytic branch numerator
$2k$.  The correction in (25) vanishes only at



$$
(k,\epsilon)=(1,1),\quad(-1,-1).
\tag{27}
$$



Let



$$
\mathcal S_n=\{k:\rho_k<1\},\qquad
 \mathcal T_n=\{k:\rho_k>1\}.
\tag{28}
$$



There is no equality case for odd $n\geq5$.  At the two embeddings in
(27), equation (21) supplies $\rho_1^d/d$.  At every other
$k\in\mathcal S_n$, the correction tends to the nonzero modulus



$$
2|\epsilon-k|\pi e^{-2}.
\tag{29}
$$



At each $k\in\mathcal T_n$, both choices of $\epsilon$ have size
$\asymp_n\rho_k^d/d$, because this exponential term dominates the
constant correction.  Consequently



$$
\prod_{k,\epsilon}|\sigma_{k,\epsilon}(\Lambda_{n,d})|
 \asymp_n
 \left(\rho_1^2\prod_{k\in\mathcal T_n}\rho_k^2\right)^d
 d^{-2(1+|\mathcal T_n|)}.
\tag{30}
$$



The unit identity gives



$$
\prod_k\rho_k=|N_{\mathbb Q(\zeta_n)/\mathbb Q}(\eta)|=1.
\tag{31}
$$



It follows that the base is



$$
B_n=\left(
  \rho_1\prod_{k\in\mathcal S_n\setminus\{1,-1\}}\rho_k
 \right)^{-2}>1.
\tag{32}
$$



For $n=5$,



$$
\rho_{\pm1}=\varphi^{-1},\qquad
 \rho_{\pm2}=\varphi,qquad
 B_5=\varphi^2,qquad |\mathcal T_5|=2,
\tag{33}
$$



so (30) is exactly



$$
\asymp\varphi^{2d}d^{-6}.
\tag{34}
$$



### 5.1 The chosen coefficient field is convenient, not minimal

There is a harmless structural refinement.  Complex conjugation sends
$\Lambda_{n,d}$ to $-\Lambda_{n,d}$, because its $s$- and
$E(1)$-coefficients are $i$ times real elements and its $B$-part is
anti-real.  Hence



$$
-i\Lambda_{n,d}\in L_n^+(s),
\tag{35}
$$



where $L_n^+$ is the maximal real subfield of $L_n$.  The product in
(30) is therefore the square of the corresponding degree-$\varphi(n)$
relative product, up to the norm-one common unit $-i$.  In the $n=5$
case this maximal-real-subfield block has order



$$
\asymp\varphi^d d^{-3}.
\tag{36}
$$



This remains exponentially growing.  Thus the candidate use of the full
field $L_n$ is correct but nonminimal; it does not manufacture growth by
including unrelated embeddings.

## 6. Field intersection, clearing, and content

Assume temporarily that $s=e+\pi$ is algebraic.  If



$$
L_n\cap\mathbb Q(s)=\mathbb Q,
\tag{37}
$$



then the Galois extension $L_n/\mathbb Q$ is linearly disjoint from
$\mathbb Q(s)$.  Each coefficient-field embedding extends while fixing
the distinguished $s$, so (30) is the distinguished absolute value of
the relative norm from $L_n(s)$ to $\mathbb Q(s)$.  It grows.

Multiplication by a positive integer used to clear rational coordinate
denominators raises this product by that integer to the power
$[L_n:\mathbb Q]$.  It cannot create contraction.  This observation
does **not** cover either of the following operations.

1. After clearing, all coordinates might have a common rational or
   algebraic divisor whose norm grows with $d$.  Dividing by it can
   decrease the product.  No all-degree coordinate-content theorem is
   proved.
2. A full absolute norm from $\mathbb Q(s)$ to $\mathbb Q$ also has
   blocks in which $s$ moves to its other hypothetical conjugates.  The
   analytic remainder identity at the distinguished real $e+\pi$ does
   not bound those blocks, even when (37) holds.

If (37) fails, only coefficient-field maps agreeing on the intersection
extend while fixing $s$, so even the formal identification of all factors
in (30) with one relative norm fails.  Maps outside that subgroup must be
paired with unknown target conjugates.  This is another control gap, not a
source of certified contraction.

These distinctions justify only the following negative conclusion:

> The raw coefficient-field relative-norm block on $c=f=0$ grows; the
> small distinguished embedding does not by itself furnish a norm
> contraction.

They do not justify saying that every primitively divided form, or the full
absolute norm over all target conjugates, has been ruled out.

## 7. Scope wording and coefficient field

Three proof-hygiene points in earlier candidate snapshots are repaired in
the audited snapshot.

1. The monotonicity statement applies specifically to multiplication by a
   positive rational integer used for denominator clearing.  Division by
   common coordinate content is treated separately.
2. The negative conclusion is expressly limited to contraction of the
   direct coefficient-field relative-norm block.  It does not include the
   target-conjugate blocks in a full absolute norm.
3. Since $-i\Lambda_{5,d}$, rather than $\Lambda_{5,d}$, has
   coefficients in the maximal real subfield, the degree-four product is
   correctly written with $\tau(-i\Lambda_{5,d})$.

The final source consistently states every unresolved content and
field-intersection issue and makes no absolute-norm claim beyond what (30)
proves.

## 8. Exact audit of the $n=5$ ideal content

Write $w=\zeta_{20}$.  Then



$$
L=\mathbb Q(w),\qquad \zeta_5=w^4,\qquad i=w^5,
 \qquad \Phi_{20}(X)=X^8-X^6+X^4-X^2+1.
\tag{38}
$$



The candidate computes in the tensor basis of
$\mathbb Z[\zeta_5,i]$.  For an independent check, I instead performed
all arithmetic in the power basis of
$\mathbb Z[w]/(\Phi_{20}(w))$.  In this model,



$$
\eta=w^2-w^4,
 \qquad (1+w^4)(w^2-w^4)=1.
\tag{39}
$$



The four elements in the candidate integral basis reduce respectively to



$$
1,\quad w^4-w^6,\quad
 w^7-w^5+w^3-2w,\quad w^7-w^3.
\tag{40}
$$



There are two independent ways to see that this is the full integer ring
of $K=L^+$.  First,
$\mathcal O_L=\mathbb Z[\zeta_5,i]$, because the two cyclotomic
integer rings have coprime discriminants, and solving the fixed-lattice
equations under conjugation gives exactly (40).  Second, direct
multiplication in the $w$-power basis gives trace Gram matrix



$$
\begin{pmatrix}
 4&-2&0&0\\
 -2&6&0&0\\
 0&0&10&0\\
 0&0&0&10
 \end{pmatrix},
 \qquad \det=2000,
\tag{41}
$$



the discriminant of $\mathbb Q(\zeta_{20})^+$.  Thus there is no hidden
index in the basis used for the Smith computation.

After least positive-integer rational clearing, write



$$
q_d(-i\Lambda_{5,d})=u_ds+v_d,
 \qquad \mathfrak c_d=(u_d,v_d)\subset\mathcal O_K.
\tag{42}
$$



The columns of multiplication by $u_d$ and by $v_d$, in an integral
basis of $\mathcal O_K$, generate the ideal $\mathfrak c_d$ as a
rank-four integer lattice.  Therefore the product of the four nonzero
Smith invariants of the resulting $4$ by $8$ matrix is its lattice
index, namely $N(\mathfrak c_d)$.  If $\gamma$ divides both
coordinates, then



$$
\mathfrak c_d\subseteq(\gamma),\qquad
 |N_{K/\mathbb Q}(\gamma)|\leq N(\mathfrak c_d),
\tag{43}
$$



so the candidate norm inequality has the correct direction.  Extending an
ideal from $K$ to the quadratic extension $L$ squares its absolute
norm.  This proves the square relation between the degree-four and
degree-eight content computations and also explains why the real-subfield
relative product has order $\varphi^d d^{-3}$.

I rederived the integral recurrences used to construct the coordinates:



$$
P_0=1,\qquad P_d(X)=X^d-dP_{d-1}(X)=d!A_d(X),
\tag{44}
$$



and, for $\ell=\operatorname {lcm}(1,\ldots,d)$,



$$
[X^m](d!\ell B_d)
 =-\sum_{j<m}[X^j]P_d\,\frac{\ell}{m-j}.
\tag{45}
$$



Substitution into the paired form gives exactly the three blocks in the
candidate equation (53).  Taking the gcd of their integral coordinates
together with $d!^3\ell$ indeed gives the least positive rational
integer $q_d$: for integers $c_1,\ldots,c_r,D$, the least positive
$q$ for which every $qc_j/D$ is integral is



$$
\frac{D}{\gcd(D,c_1,\ldots,c_r)}.
\tag{46}
$$



The complete degree range was rerun byte for byte.  It proves exactly, and
only for $1\leq d\leq200$,



$$
N(\mathfrak c_1)=16,\qquad
 N(\mathfrak c_d)=
 \left(5^{[d\equiv2\pmod5]}
       19^{[d\equiv15\pmod{19}]}
 \right)^2\quad(2\leq d\leq200).
\tag{47}
$$



My independent $w$-basis implementation recomputed the Smith diagonals
at $d=1,2,3,7,15,72,167,200$; they agree exactly, including
$(1,1,95,95)$ at $d=72,167$.  It also independently reconstructs the
least-clearing digit count at each selected degree.  Finally, the archived
comparison



$$
N(\mathfrak c_d)<\varphi^d\qquad(3\leq d\leq200)
\tag{48}
$$



is exact: it checks
$2N(\mathfrak c_d)<3F_d+2F_{d-1}<2\varphi^d$, using
$\varphi>3/2$.  This finite result does not prove a recurrence for the
observed residue-class pattern.  The limsup condition in the candidate
equation (50) remains necessary but unproved, exactly as stated.

## 9. Independent computation and reproducibility

The independent audit script:

* verifies (11) symbolically;
* checks $\Phi_n(-1)=1$ exactly for every odd $5\leq n\leq31$;
* independently constructs all unit-residue representatives, principal
  branches, $\mathcal S_n$, $\mathcal T_n$, and $B_n$;
* verifies $\prod_k\rho_k=1$ and $B_n>1$ numerically at 120 decimal
  digits for those $n$;
* reconstructs the $c=f=0$ polynomials independently and checks the
  phase ratio in (19) for $d=20,40,80$;
* checks (25) directly at all eight $n=5$ embeddings;
* checks that $B_5=(3+\sqrt5)/2$ satisfies $X^2-3X+1=0$;
* reconstructs $\mathcal O_K$ in the unrelated $\zeta_{20}$ power
  basis and obtains the exact trace discriminant $2000$; and
* independently recomputes the least clearing and content-ideal Smith
  invariants at eight selected degrees through $d=200$.

At $d=80$, the ratios of the exact logarithmic pairs to the leading
term in (19) are



$$
0.9721550\ldots\quad(k=\pm1),
 \qquad
 0.9794743\ldots\quad(k=\pm2),
\tag{49}
$$



consistent with the proved $1+O(d^{-1})$ error.  The largest residual in
the exact mismatch identity (25) is below $6\times10^{-107}$ at the
working precision.  These decimal checks are diagnostics; Sections 2--8
contain the proof.

Independent artifacts:

* `scripts/independent_algebraic_unit_two_log_audit.py`, SHA-256
  `a1ba583b9068d7debb595bd8fa904a8478f77c712aaa14992f6d9a9d47b47c96`;
* `results/independent_algebraic_unit_two_log_audit.json`, SHA-256
  `5e7371e06ec6c04fa7b15530405d405e5e0769cb4b2a42a9d0e01bfc121f7853`.

Both candidate certificates were also rerun from scratch and reproduced
their results byte for byte.  Python compilation, Pandoc/MathJax rendering,
UTF-8/control-character checks, balanced math delimiters, and unique
equation-tag checks pass.
