> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coupling the two weighted left-factorial sums on the $n=5$ edge

Checked: 2026-08-27 UTC

## Verdict

The two complementary weighted left-factorial sums admit two exact
couplings.  First, their simultaneous vanishing is the vanishing of the two
coefficients of one linear remainder; equivalently it is detected, up to
radical, by that remainder's linear coefficient together with a quadratic
resultant.  Second, it is equivalent to a fixed cyclotomic unit being a
double root of a polynomial with every coefficient in one residue class
modulo five missing.

Neither coupling proves that the common ideal is supported only over $19$.
The resultant by itself is insufficient: already at $p=11,d=4$ exactly
one of the two weighted sums vanishes.  The exact pair still has only the
known $(p,d)=(19,15)$ hit in the finite companion scan, but that scan is
diagnostic and is not an all-prime classification.

## 1. Complementary polynomial and its differential equation

Let $p\ne5$ be an odd prime, let $0\le d<p$, and put



$$
m=p-1-d,\qquad
 W_m(Z)=\sum_{j=0}^{d}(m+j)!Z^j\in\mathbb F_p[Z].
\tag{1}
$$



As before, put



$$
\zeta=\zeta _5,\quad u=1+\zeta,\quad v=1+\zeta^{-1},\quad
 A=u+v=uv,\quad A^2-3A+1=0.
\tag{2}
$$



The exact complementary-factor identities are



$$
P_d(u^{-1})=\frac{u^{-d}}{m!}W_m(u),\qquad
 P_d(v^{-1})=\frac{v^{-d}}{m!}W_m(v)\pmod p.
\tag{3}
$$



Thus all prefactors are units and the original simultaneous $P$-zero is
equivalent to $W_m(u)=W_m(v)=0$.

The factorial ratio in (1), including its terminal coefficient, gives the
polynomial differential equation



$$
\boxed{
 Z^2W_m'(Z)+\{(m+1)Z-1\}W_m(Z)=-m!}
 \qquad(\bmod p).
\tag{4}
$$



Indeed, the coefficient of $Z^k$, $1\le k\le d$, on the left is



$$
(m+k)(m+k-1)!-(m+k)!=0.
$$



The constant coefficient is $-m!$, while the possible top coefficient is
$(m+d+1)(m+d)! =p(p-1)!=0$.  No unproved summation formula is used here.

## 2. Linear remainder and the exact resultant data

Over the real quadratic coefficient ring, set



$$
q(Z)=Z^2-AZ+A=(Z-u)(Z-v)
\tag{5}
$$



and write the unique remainder



$$
W_m(Z)\equiv a_m+b_mZ\pmod {q(Z)},
                     \qquad a_m,b_m\in\mathbb F_p[A].
\tag{6}
$$



Away from $5$, $u-v=\zeta-\zeta^{-1}$ is a unit.  Hence



$$
\binom{W_m(u)}{W_m(v)}
 =
 \begin{pmatrix}1&u\\1&v\end{pmatrix}
 \binom{a_m}{b_m}
\tag{7}
$$



is an invertible change of coordinates after localization.  Consequently



$$
\boxed{W_m(u)=W_m(v)=0\quad\Longleftrightarrow\quad a_m=b_m=0.}
\tag{8}
$$



The quadratic resultant is only their product:



$$
\mathcal R_m=\operatorname {Res}_Z(q,W_m)
 =W_m(u)W_m(v)=a_m^2+Aa_mb_m+Ab_m^2.
\tag{9}
$$



If $\mathcal I_m=(a_m,b_m)$, then the exact ideal identity



$$
(b_m,\mathcal R_m)=(b_m,a_m^2),
 \qquad
 \mathcal I_m^2\subseteq(b_m,\mathcal R_m)\subseteq\mathcal I_m
\tag{10}
$$



shows that



$$
\sqrt{(b_m,\mathcal R_m)}=\sqrt{\mathcal I_m}.
\tag{11}
$$



Thus the resultant plus one remainder coefficient detects the correct prime
support, but the resultant alone does not.

There is also an exact recursion in the complementary index.  Define
$W_p=0$, so $a_p=b_p=0$.  Since



$$
W_m(Z)=m!+ZW_{m+1}(Z),
$$



reduction modulo $q$ gives



$$
\boxed{
 \binom{a_m}{b_m}
 =\binom{m!}{0}+
 M\binom{a_{m+1}}{b_{m+1}},\qquad
 M=\begin{pmatrix}0&-A\\1&A\end{pmatrix}.}
\tag{12}
$$



The eigenvalues of $M$ are $u,v$.  With
$\kappa=5A-2$, the identities $u^5=v^5=-\kappa$ imply



$$
M^5=-\kappa I.
\tag{13}
$$



Therefore the five-block form is



$$
\binom{a_m}{b_m}
 =\sum_{j=0}^4(m+j)!M^j\binom10
  -\kappa\binom{a_{m+5}}{b_{m+5}},
\tag{14}
$$



whenever the displayed factorial indices lie below $p$.  This is the
weighted-left-factorial version of the previously derived five-step law; it
does not turn the endpoint sum into a fixed algebraic integer.

## 3. A lacunary double-root reformulation

Define



$$
H_m(Z)=W_m(\zeta^{-1}Z)-\zeta W_m(Z).
\tag{15}
$$



Its coefficient of $Z^j$ is



$$
(m+j)!(\zeta^{-j}-\zeta),
\tag{16}
$$



so every coefficient with $j\equiv4\pmod5$ is zero.  Applying (4) at
$Z$ and at $\zeta^{-1}Z$, and subtracting with the indicated weights,
gives the polynomial identity



$$
\boxed{
 Z^2H_m'(Z)=\{\zeta-(m+1)Z\}H_m(Z)
             +\zeta(\zeta-1)W_m(Z).}
\tag{17}
$$



Because $\zeta^{-1}u=v$, evaluation at $u$ yields



$$
H_m(u)=W_m(v)-\zeta W_m(u)
\tag{18}
$$



and



$$
W_m(u)=
 \frac{u^2H_m'(u)-\{\zeta-(m+1)u\}H_m(u)}
      {\zeta(\zeta-1)}.
\tag{19}
$$



All denominators in (19) are local units for $p\ne5$, and (18) then
recovers $W_m(v)$.  Hence there is an equality of localized ideals



$$
\boxed{(W_m(u),W_m(v))=(H_m(u),H_m'(u)),}
\tag{20}
$$



and the simultaneous weighted zero is exactly the assertion that $u$ is
a multiple root of the lacunary polynomial $H_m$.

This reformulation is exact, but a full discriminant of $H_m$ is too
coarse: it detects multiple roots anywhere, whereas (20) prescribes the
specific cyclotomic unit $u$.

## 4. Exact counterexample to using the product alone

Take $p=11$, choose $\zeta=4\in\mathbb F_{11}$, and take $d=4$, so
$m=6$.  Then



$$
u=5,\quad v=4,\quad u^{-1}=9,\quad v^{-1}=3,\quad A=9.
$$



Direct evaluation gives



$$
W_6(5)=3,\qquad W_6(4)=0,
\tag{21}
$$



or equivalently



$$
P_4(9)=3,\qquad P_4(3)=0\pmod {11}.
\tag{22}
$$



The remainder in (6) is $a_6+b_6Z=10+3Z$.  Thus
$\mathcal R_6=0$, but $b_6=3$ and $\mathcal I_6=(1)$ locally.  This
rigorously refutes the inference “zero product/resultant implies the two
weighted sums vanish.”  It does **not** refute the stronger conjecture that
the true common ideal $\mathcal I_m$ is supported only over $19$.

The companion script verifies (4), (6)--(14), and (17)--(22) in exact
finite-field arithmetic over its stated range.  Its scan of common ideals is
finite diagnostic evidence only.  Nothing here proves either algebraicity
or transcendence of $e+\pi$.
