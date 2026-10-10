> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An accelerated cyclotomic-unit ray: moving-target gcd closure

Checked: 2026-08-27 UTC

## Verdict

Let



$$
K=\mathbb Q(\zeta_{20})^+,
 \qquad s=e+\pi,
 \qquad \Theta_d=-i\Lambda_{5,d},
 \tag{1}
$$



and let



$$
\theta_d=u_7^{t_d},
 \qquad t_d\in\mathbb Z_{>0},
 \qquad \frac{t_d}{d\log d}\longrightarrow\infty.
 \tag{2}
$$



Use the specific safe positive-integer clearing



$$
Q_d=(d!)^3\ell_d,\qquad
 \ell_d=\operatorname {lcm}(1,\ldots,d),\qquad
 Q_d\Theta_d=U_ds+V_d,
 \qquad U_d,V_d\in\mathcal O_K,
 \tag{3}
$$



put



$$
A_d=\operatorname {Tr}_{K/\mathbb Q}(\theta_dU_d),
 \qquad
 B_d=\operatorname {Tr}_{K/\mathbb Q}(\theta_dV_d),
 \qquad
 g_d=\gcd(A_d,B_d).
 \tag{4}
$$



Then the moving-target greatest-common-divisor theorem of Grieve and Wang
gives



$$
\boxed{\log g_d=o(t_d).}
 \tag{5}
$$



This conclusion holds for the full sequence, not merely along one infinite
subsequence.  The published theorem itself supplies only an infinite
small-gcd subset in one alternative; Section 5 below gives the necessary
bad-subsequence contradiction and rules out its translated-subgroup
alternative.

The coefficient trace satisfies



$$
\log|A_d|=t_d\log\sigma_1(u_7)
                                      +O(d\log d),
 \tag{6}
$$



and the analytic quotient satisfies



$$
\left|\frac{
   \operatorname {Tr}_{K/\mathbb Q}(\theta_d\Theta_d)}
  {\operatorname {Tr}_{K/\mathbb Q}(\theta_d\,[s]\Theta_d)}
       \right|
                 \asymp\frac1{d\varphi^d}.
 \tag{7}
$$



Here $[s]\Theta_d$ denotes the coefficient of $s$.  Therefore the
primitive rational form obtained from (4) satisfies



$$
\log\left|\frac{A_d}{g_d}s+\frac{B_d}{g_d}\right|
 =t_d\log\sigma_1(u_7)-d\log\varphi+o(t_d)
 \longrightarrow+\infty.
 \tag{8}
$$



The safe pair in (3) is generally not least-cleared.  If $q_d$ is the
least positive rational clearing, then integrality of $Q_d$ implies
$Q_d/q_d\in\mathbb Z_{>0}$; hence the safe pair is a positive integer
multiple of the least-cleared pair and both yield exactly the same
primitive integer pair.  Thus every accelerated ray (2) is an all-degree
primitive no-go.  The estimate (5) is asserted for the specified safe
clearing (and therefore for the least clearing), not for an arbitrary
extra degree-dependent multiple of it.  This
does **not** settle the rational linear rays $t_d\asymp d$, because their
moving coefficient height is not $o(t_d)$.  It also says nothing about
the transcendence or algebraicity of $e+\pi$.

The only external input is Theorem 1.2, together with its proof through
Theorems 3.1 and 3.2, of Nathan Grieve and Julie Tzu-Yueh Wang,
[“Greatest common divisors with moving targets and consequences for linear
recurrence sequences”](https://arxiv.org/abs/1902.09109),
*Transactions of the American Mathematical Society* **373** (2020),
8653--8676.  The application below checks every hypothesis explicitly.

## 1. The four conjugate sums

Index the real embeddings of $K$ by $k=1,3,7,9$, and put



$$
\alpha_k=\sigma_k(u_7),
       \qquad U_{d,k}=\sigma_k(U_d),
       \qquad V_{d,k}=\sigma_k(V_d).
 \tag{9}
$$



Because $N_{K/\mathbb Q}(u_7)=1$,



$$
\alpha_1\alpha_3\alpha_7\alpha_9=1.
 \tag{10}
$$



Consequently



$$
\begin{aligned}
 A_d&=\sum_{k=1,3,7,9}U_{d,k}\alpha_k^{t_d},\\
 B_d&=\sum_{k=1,3,7,9}V_{d,k}\alpha_k^{t_d}.
 \end{aligned}
 \tag{11}
$$



Set



$$
x_1=\alpha_1^{t_d},\qquad
       x_2=\alpha_3^{t_d},\qquad
       x_3=\alpha_7^{t_d}.
 \tag{12}
$$



All three are global units of $K$.  Multiplication of (11) by the common
unit $x_1x_2x_3=\alpha_9^{-t_d}$ gives evaluations of the ordinary
polynomials



$$
\begin{aligned}
 F_d(X)={}&U_{d,9}
  +U_{d,1}X_1^2X_2X_3
  +U_{d,3}X_1X_2^2X_3
  +U_{d,7}X_1X_2X_3^2,\\
 G_d(X)={}&V_{d,9}
  +V_{d,1}X_1^2X_2X_3
  +V_{d,3}X_1X_2^2X_3
  +V_{d,7}X_1X_2X_3^2.
 \end{aligned}
 \tag{13}
$$



Precisely,



$$
F_d(x_1,x_2,x_3)=x_1x_2x_3A_d,
 \qquad
 G_d(x_1,x_2,x_3)=x_1x_2x_3B_d.
 \tag{14}
$$



After discarding finitely many degrees, their degrees are the fixed positive
integer four, and both have nonzero constant term.  Indeed,
$P_d(x)/d!=(-1)^d\sum_{j=0}^d(-x)^j/j!$, so at the fixed points
$\eta,\bar\eta$ its modulus tends to the nonzero modulus of
$e^{-x}$; hence $U_d\ne0$ eventually.  The accepted endpoint asymptotic
makes the anti-fixed part of $V_d$, and hence $V_d$, nonzero for all
sufficiently large $d$.  Removing finitely many indices does not affect
any conclusion below.

## 2. Fixed $S$ and slow coefficient height

The safe rational clearing fixed in (3) is



$$
Q_d=(d!)^3\ell_d,
             \qquad \ell_d=\operatorname {lcm}(1,\ldots,d).
 \tag{15}
$$



The exact integral reconstruction has



$$
P_d=d!A_d^{\rm edge}\in\mathbb Z[X],
 \qquad
 R_d=d!\ell_d B_d^{\rm edge}\in\mathbb Z[X],
 \tag{16}
$$



and the coefficients of $U_d,V_d$ are finite sums of products of
evaluations of $P_d,R_d$ at the fixed algebraic-integer units
$1,\eta,\bar\eta$.  The elementary coefficient bounds



$$
\|P_d\|_\infty\leq d!,
 \qquad
        \|R_d\|_\infty\leq d\,d!\ell_d,
 \qquad
        \log\ell_d=O(d)
 \tag{17}
$$



therefore give



$$
h(U_d),h(V_d),h(F_d),h(G_d)=O(d\log d).
 \tag{18}
$$



The implied constant is independent of $t_d$.  Since



$$
h(x_i)=t_dh(\alpha_i),
 \tag{19}
$$



(2) and (18) prove the slow-growth hypothesis



$$
\max\{h(F_d),h(G_d)\}
     =o\!\left(\max_i h(x_i)\right).
 \tag{20}
$$



The $\alpha_i$ are global units, so one may take the fixed set $S$ to
consist only of the four archimedean places.  No degree-dependent prime is
inserted into $S$.  Polynomial height in the cited theorem is
projective, so it cannot by itself see a common scalar in the evaluations.
Section 5 normalizes each moving polynomial by its nonzero constant
coefficient and transfers the resulting generalized-gcd bound back to the
safe integer pair with an explicit local-height inequality.

## 3. Multiplicative independence of the moving point

Use $u_3,u_7,u_9$ as a basis of the free cyclotomic-unit group, ignoring
the sign torsion.  The exponent columns of
$\alpha_1,\alpha_3,\alpha_7$ are



$$
\begin{pmatrix}0\\1\\0\end{pmatrix},
 \qquad
 \begin{pmatrix}-1\\0\\0\end{pmatrix},
 \qquad
 \begin{pmatrix}0\\-1\\1\end{pmatrix}.
 \tag{21}
$$



Their determinant is one.  Hence



$$
\alpha_1^a\alpha_3^b\alpha_7^c
                  \text{ is a root of unity}
       \quad\Longrightarrow\quad a=b=c=0.
 \tag{22}
$$



In particular the moving points (12) are not contained in a fixed proper
algebraic subgroup of $\mathbb G_m^3$.

## 4. Coprimality of the two moving polynomials

The support exponent matrix of the three nonconstant monomials in (13) is



$$
E=\begin{pmatrix}
 2&1&1\\
 1&2&1\\
 1&1&2
 \end{pmatrix},
 \qquad \det E=4.
 \tag{23}
$$



Thus



$$
\psi:\mathbb G_m^3\longrightarrow\mathbb G_m^3,
 \qquad
 (X_1,X_2,X_3)\longmapsto
 (X_1^2X_2X_3,X_1X_2^2X_3,X_1X_2X_3^2)
 \tag{24}
$$



is a finite isogeny.  On the target torus, (13) is the pullback of the two
affine linear Laurent polynomials



$$
U_{d,9}+U_{d,1}Y_1+U_{d,3}Y_2+U_{d,7}Y_3,
 \qquad
 V_{d,9}+V_{d,1}Y_1+V_{d,3}Y_2+V_{d,7}Y_3.
 \tag{25}
$$



These two coefficient vectors are not proportional.  Indeed,
proportionality would first give $V_d=cU_d$ at the identity embedding;
the other three equalities force $c\in\mathbb Q$.  But $U_d$ lies in
the quadratic subfield $\mathbb Q(\sqrt5)$, whereas $V_d$ has a
nonzero anti-fixed component for all sufficiently large $d$.

If the pullbacks in (13) had a common irreducible divisor in the Laurent
ring, its image under the finite map (24) would be a divisor contained in
both distinct hyperplanes (25).  A finite map preserves dimension, whereas
the intersection of two distinct hyperplanes in the three-dimensional
torus has codimension two.  This is impossible.  Hence $F_d,G_d$ are
coprime in the Laurent ring.  Their nonzero constant terms exclude a common
coordinate monomial, so they are coprime in $K[X_1,X_2,X_3]$, exactly as
required by the moving-target theorem.

## 5. The theorem's dichotomy and the full-sequence conclusion

The coefficient height in Grieve--Wang is projective.  We therefore do not
apply the theorem directly to the integrally scaled pair (13).  On the
eventual tail where the constant coefficients are nonzero, put



$$
\widehat F_d=F_d/U_{d,9},
       \qquad\widehat G_d=G_d/V_{d,9}.
 \tag{26}
$$



Both normalized polynomials have constant coefficient one.  Scaling does
not change projective polynomial height, degree, or coprimality, so
(18)--(20) verify all moving-polynomial hypotheses for
$\widehat F_d,\widehat G_d$.  Write



$$
\Delta_d=\log\gcd_K
   \{\widehat F_d(x_1,x_2,x_3),
      \widehat G_d(x_1,x_2,x_3)\}
 \tag{27}
$$



for the generalized logarithmic gcd in the paper's normalization.

We first transfer $\Delta_d$ back to the rational safe pair.  By (14),
with the global unit $w_d=x_1x_2x_3$,



$$
\widehat F_d({\bf x}_d)=w_dA_d/U_{d,9},
 \qquad
 \widehat G_d({\bf x}_d)=w_dB_d/V_{d,9}.
 \tag{28}
$$



At a finite place $v$, write the four nonnegative integral valuations of
$A_d,B_d,U_{d,9},V_{d,9}$ as $r,s,c,e$, respectively.  The common
unit $w_d$ has valuation zero.  The elementary inequality



$$
\min(r,s)
 \leq \max\{0,\min(r-c,s-e)\}+c+e
 \tag{29}
$$



therefore compares the local rational gcd with the local contribution to
$\Delta_d$.  Summing (29) over all finite places, using
$[K:\mathbb Q]=4$, gives



$$
\boxed{
 4\log g_d
 \leq \Delta_d+\log|N_{K/\mathbb Q}(U_{d,9})|
                  +\log|N_{K/\mathbb Q}(V_{d,9})|
 \leq \Delta_d+h(U_{d,9})+h(V_{d,9}).}
 \tag{30}
$$



The last inequality uses that the two constant coefficients are nonzero
algebraic integers.  Equation (18) shows that the two added heights are
$O(d\log d)=o(t_d)$.  Thus (30) is the required clearing-sensitive
normalization; no scalar is silently discarded.

We next exclude, in the precise form proved in the paper, every exceptional
branch used to derive Theorem 1.2.  In the proof of Theorem 3.1, before
Proposition 3.5 packages the result as a translated-subgroup statement,
equations (3.36)--(3.37) give a fixed nontrivial character of slow height.
The proof of Theorem 3.2 gives the same type of relation as the ratio of
two distinct monomials (lines 840--847 of the arXiv version).  Thus either
exceptional branch, after passage to an infinite subset, supplies fixed
integers $(a,b,c)\ne(0,0,0)$ such that



$$
h\{x_1(d)^ax_2(d)^bx_3(d)^c\}
             =o\!\left(\max_i h(x_i(d))\right)=o(t_d).
 \tag{31}
$$



This is the proof's $(ii')$ relation (or its Theorem 3.2 analogue); it is
not inferred by reversing the one-way Proposition 3.5.  In both cases the
character comes from the difference of two distinct monomial exponent
vectors.  In the homogenized Theorem 3.1 argument the vectors have the same
total degree, so the entries on $(x_1,x_2,x_3)$ cannot all vanish unless
the homogenizing entry also vanishes.  This justifies
$(a,b,c)\ne0$ above.  Here the left side of (31) is exactly



$$
t_dh(\alpha_1^a\alpha_3^b\alpha_7^c).
 \tag{32}
$$



By (22) the fixed algebraic number inside the last height is not a root of
unity, so its height is positive.  Hence (31) is impossible on every
infinite subset.

It remains to combine the two smallness conclusions on nested infinite
subsets.  If
(5) failed, there would be an $\epsilon_0>0$ and an infinite index set
$\Lambda$ on which



$$
\log g_d\geq\epsilon_0t_d.
 \tag{33}
$$



By (30), on this set



$$
\Delta_d\geq4\epsilon_0t_d-o(t_d).
 \tag{34}
$$



Put $H=\max_i h(\alpha_i)>0$, and choose
$0<\epsilon<\epsilon_0/H$.  Apply Theorem 3.1 to
$\widehat F_d,\widehat G_d$ on $\Lambda$.  Its exceptional branch is
impossible by (31)--(32), so an infinite subset $A\subseteq\Lambda$
satisfies



$$
\Delta_d^{\mathrm{out}}
 :=-\sum_{v\notin S}\log^-
   \max\{|\widehat F_d({\bf x}_d)|_v,
          |\widehat G_d({\bf x}_d)|_v\}
 <\epsilon Ht_d.
 \tag{35}
$$



Now apply Theorem 3.2 to $\widehat F_d$ on $A$; its constant term is
one.  Again the exceptional monomial-ratio branch is impossible by
(31)--(32), so on an infinite $A'\subseteq A$,



$$
-\sum_{v\in S}\log^-|\widehat F_d({\bf x}_d)|_v
                         <\epsilon Ht_d.
 \tag{36}
$$



The $S$-part of $\Delta_d$ is at most the left side of (36).  Hence on
$A'$, equations (35)--(36) give



$$
\Delta_d<2\epsilon Ht_d
                                      <2\epsilon_0t_d,
 \tag{37}
$$



contradicting (34), whose right side is eventually larger than
$3\epsilon_0t_d$.  This contradiction proves (5) in the full sequential
$o(t_d)$ sense and explicitly resolves both nested
only-infinite-subset steps.

Finally, if the safe pair is a common integer multiple of the least-cleared
pair, its ordinary gcd is correspondingly larger.  Bounding the safe gcd
therefore also bounds the selected gcd of the least pair, while both pairs
give the same primitive form.

## 6. Dominance and primitive divergence

The four absolute conjugates of $u_7$ satisfy



$$
|\alpha_1|>5,
 \qquad |\alpha_3|,|\alpha_9|<\frac12,
 \qquad 1<|\alpha_7|<\frac65.
 \tag{38}
$$



Every nonzero conjugate of the safe coefficient $U_d$ has logarithmic
size $O(d\log d)$, above and below, by (18) and the product formula.
Thus (2) and (38) make the embedding-1 summand uniquely dominant in the
coefficient trace, proving (6).

For the analytic endpoint trace, the embedding-1 edge is
$\asymp\varphi^{-d}/d$; embeddings 3 and 7 are
$O(\varphi^d/d)$, and embedding 9 is $O(1)$.  The fixed exponential
separation in (38), multiplied by $t_d\gg d\log d$, overwhelms these
degree-dependent endpoint factors.  Hence embedding 1 is again uniquely
dominant and (7) follows, with a nonzero leading constant uniformly over
the five residue classes of $d$.

The ratio between the safe clearing and the least positive rational
clearing is a positive integer, so safe and least clearing yield the same
primitive pair.  Equations
(5)--(7) now give



$$
\begin{aligned}
 \log\left|\frac{A_d}{g_d}s+\frac{B_d}{g_d}\right|
  &={}t_d\log|\alpha_1|-d\log\varphi-log d+o(t_d)\\
  &={}t_d\log|\alpha_1|+o(t_d),
 \end{aligned}
 \tag{39}
$$



which tends to $+\infty$.  This proves (8).

## 7. Exact algebraic certificate

The companion script verifies, without floating-point arithmetic:

* the signed unit-exponent columns (21) and their determinant;
* the monomial support matrix (23) and its determinant;
* the trace Gram matrix and norm-one identity;
* the fixed/anti-fixed distinction excluding proportionality;
* the exact safe-height ingredients through the integral edge formulas.

The moving-target theorem and the dimension argument are proofs, not finite
experiments.  The certificate is
<scripts/cyclotomic_unit_accelerated_u7_gcd_certificate.py>, with output
<results/cyclotomic_unit_accelerated_u7_gcd_certificate.json>.
