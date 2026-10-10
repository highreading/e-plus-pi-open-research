> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Cyclotomic-unit traces of the two-log Rivoal edge

Checked: 2026-08-26 UTC

## Verdict

Let



$$
K=\mathbb Q(\zeta _{20})^+,
 \qquad F=\mathbb Q(\sqrt5),
 \qquad \varphi=\frac{1+\sqrt5}{2},
 \tag{1}
$$



and let $\Theta_d=-i\Lambda_{5,d}\in K(e+\pi)$ be the
$c=f=0$ form from the two-conjugate-log construction.  For a unit
$\theta\in\mathcal O_K^\times$, tracing gives a rational form



$$
T_d(\theta)=\operatorname {Tr}_{K/\mathbb Q}(\theta\Theta_d)
                  =a_d(\theta)(e+\pi)+b_d(\theta),
       \qquad a_d(\theta),b_d(\theta)\in\mathbb Q.
 \tag{2}
$$



This is a genuine rationalization of the algebraic-coefficient form, so it
is not disposed of merely by observing that the raw coefficient-field norm
grows.  Two rigorous obstructions nevertheless cover the most immediate
unit choices.

1. Every unit from the quadratic subfield $F$, even if it varies with
   $d$, annihilates the logarithmic component of $\Theta_d$.  Every
   nonzero primitive trace is then exactly the same reduced
   truncated-exponential form

   

$$
p_d(e+\pi)-q_d,
         \qquad \frac{p_d}{q_d}\longrightarrow e^{-1},
   \tag{3}
$$



   and its modulus is asymptotic to $\pi p_d\to\infty$.  In particular,
   the experimentally prominent ray
   $\theta=(u_9/(u_3u_7))^m=\varphi^{-2m}$ is a complete no-go after
   primitivization, not a promising cancellation.

2. Write $H(\theta)=\max_\sigma|\sigma(\theta)|$.  If
   $\theta_d\notin F$ and

   

$$
\frac{dH(\theta_d)^2}{\varphi^d}\longrightarrow0,
   \tag{4}
$$



   then every nonconstant primitive form obtained from (2) tends to
   infinity in modulus.  A trace with zero coefficient on $e+\pi$ is
   either zero or a nonzero rational constant, whose primitive modulus is
   one.  Hence no primitive trace in this height range tends to zero.
   In particular, exponent triples $(m_3,m_7,m_9)=o(d)$ are ruled out.

More precisely, (27)--(29) imply that there is an absolute $c_0>0$
such that any sequence of nonzero primitive traces tending to zero must,
for every sufficiently large $d$, leave the quadratic subfield and obey



$$
H(\theta_d)\geq
                  c_0\frac{\varphi^{d/2}}{\sqrt d}.
 \tag{5}
$$



it must also produce cancellations among different embeddings and a
sufficiently large exact gcd of the two rational trace coordinates.  A
continuous log-lattice balance exists at height about $\varphi^{5d/4}$,
but before trace cancellation its largest summands still have size
$\varphi^{d/4}$.  The exact bounded searches recorded here show only
small sporadic low-degree forms and then rapid growth.  They are diagnostics,
not an all-degree no-go theorem.  No viable decreasing primitive family was
found, but the exponentially large-height regime outside (4) remains open.

Nothing in this note proves either algebraicity or transcendence of
$e+\pi$.

## 1. The field and three cyclotomic units

Put $w=\zeta _{20}$.  For $a=3,7,9$, define the real cyclotomic unit



$$
u_a=w^{(1-a)/2}\frac{1-w^a}{1-w}.
 \tag{6}
$$



At the embedding $w\mapsto e^{2\pi ik/20}$,



$$
\sigma_k(u_a)=\frac{\sin(a k\pi/20)}{\sin(k\pi/20)},
       \qquad k=1,3,7,9.
 \tag{7}
$$



All three norms are one.  Use the integral basis



$$
1,\quad \zeta _5+\zeta _5^{-1},\quad
  i(\zeta _5-\zeta _5^{-1}),\quad
  i(\zeta _5^2-\zeta _5^{-2})
 \tag{8}
$$



of $K$.  The exact coordinate vectors of $u_3,u_7,u_9$ are



$$
(1,0,-1,0),\qquad
             (2,1,-1,-1),\qquad
             (2,2,-1,-1).
 \tag{9}
$$



Let $\tau$ be the nontrivial automorphism of $K/F$.  In the ambient
description $K\subset\mathbb Q(\zeta _5,i)$, it fixes $\zeta _5$ and
sends $i$ to $-i$.  Exact multiplication in (8) gives



$$
\tau(u_3)=-\frac{u_7}{u_9},\qquad
 \tau(u_7)=-\frac{u_3}{u_9},\qquad
 \tau(u_9)=u_9^{-1}.
 \tag{10}
$$



In particular,



$$
v:=\frac{u_9}{u_3u_7}\in F,
              \qquad v=\varphi^{-2}
 \tag{11}
$$



at the distinguished embedding.  Its multiplication characteristic
polynomial on $K$ is
$(X^2-3X+1)^2$.  Formula (11) explains why exponent vectors
$(-m,-m,m)$ repeatedly appeared on the boundary of finite searches.

## 2. Exact fixed and anti-fixed decomposition

Write $A_d,B_d,E_d$ for the edge polynomials, put
$s=e+\pi$, and set $\eta=(1+\zeta _5)^{-1}$,
$\bar\eta=1-\eta$.  Direct expansion of the algebraic form gives



$$
\Theta_d=X_d+Y_d,
 \tag{12}
$$



where



$$
\begin{aligned}
 X_d={}&2A_d(\eta)A_d(\bar\eta)
             \{A_d(1)s-E_d(1)\},\\
 Y_d={}&-5iA_d(1)
       \{A_d(\eta)B_d(\bar\eta)
          -A_d(\bar\eta)B_d(\eta)\}.
\end{aligned}
 \tag{13}
$$



Thus $X_d\in F(s)$, $Y_d\in K$, and



$$
\tau(X_d)=X_d,
                       \qquad \tau(Y_d)=-Y_d.
 \tag{14}
$$



Let $\nu_0,\nu_1$ be the two embeddings of $F$, with $\nu_0$ the
distinguished one.  Choose one extension of each to $K$.  The accepted
endpoint expansion for the two-log edge implies, uniformly over the five
residue classes of $d$,



$$
\nu_j(X_d)=O(1),\qquad \nu_0(Y_d)=O(1),\qquad
 |\nu_1(Y_d)|\asymp\frac{\varphi^d}{d}.
 \tag{15}
$$



For completeness, the last assertion does not rely on a numerical
noncancellation.  Substituting
$B(x)=A(x)\operatorname {Log}(1-x)-R_{\log}(x)$ into (13) shows that
the growing part is a nonzero constant multiple of



$$
A_d(\bar x)R_d(x)-A_d(x)R_d(\bar x),
 \tag{16}
$$



at $|x|=\varphi$.  Its leading term is



$$
\frac{2ie^{-3/2}}d\varphi^d
 \sin\!\left(\frac{2(d+2)\pi}{5}
        +\frac12\tan\frac{2\pi}{5}\right).
 \tag{17}
$$



The sine has a positive minimum over the five residue classes: its
algebraic second summand cannot be a rational multiple of the transcendental
number $\pi$.  This proves the two-sided estimate in (15).

For any $\theta\in K$, put



$$
\theta_+=\frac{\theta+\tau\theta}{2},
              \qquad
              \theta_-=\frac{\theta-\tau\theta}{2}.
 \tag{18}
$$



Taking first the relative trace and then the trace of $F$ gives the exact
identity



$$
T_d(\theta)
   =2\operatorname {Tr}_{F/\mathbb Q}
       \{\theta_+X_d+\theta_-Y_d\}.
 \tag{19}
$$



Here each product in braces is fixed by $\tau$, even though
$\theta_-$ and $Y_d$ separately are anti-fixed.

## 3. Complete collapse for quadratic-subfield units

If $\theta\in F$, then $\theta_-=0$, and (13), (19) give



$$
T_d(\theta)=4\operatorname {Tr}_{F/\mathbb Q}
   \{\theta A_d(\eta)A_d(\bar\eta)\}
   \{A_d(1)s-E_d(1)\}.
 \tag{20}
$$



The first factor is rational.  If it vanishes, the traced form is
identically zero.  Otherwise it disappears completely upon rational
primitivization.  On this edge,



$$
A_d(1)=(-1)^d\frac{D_d}{d!},\qquad
 E_d(1)=(-1)^d,\qquad
 D_d={!d},\qquad
 D_d=dD_{d-1}+(-1)^d.
 \tag{21}
$$



Consequently the primitive pair, up to a common sign, is exactly



$$
p_d=\frac{D_d}{g_d},\qquad
       q_d=\frac{d!}{g_d},\qquad
       g_d=\gcd(D_d,d!).
 \tag{22}
$$



The reduced rationals $p_d/q_d=D_d/d!$ tend to the irrational number
$e^{-1}$.  Their reduced denominators, and hence their numerators, tend
to infinity: otherwise infinitely many would lie in the finite set of
reduced rationals in a fixed compact interval with bounded denominator.
Finally,



$$
\frac{p_ds-q_d}{p_d}=s-\frac{q_d}{p_d}\longrightarrow\pi.
 \tag{23}
$$



This proves (3), for arbitrary degree-dependent choices of nonzero
$\theta_d\in F$.  In particular it proves the no-go for every power of
the unit (11).

## 4. A height barrier outside the quadratic subfield

Define



$$
H(\theta)=\max_{\sigma:K\hookrightarrow\mathbb R}
                                  |\sigma(\theta)|.
 \tag{24}
$$



Suppose $\theta\in\mathcal O_K^\times\setminus F$.  Then
$\delta=\theta-\tau\theta$ is a nonzero algebraic integer.  At each
embedding of $F$, its two extensions to $K$ differ only by sign.  If
$\delta_0,\delta_1$ denote one value above each embedding of $F$, then



$$
1\leq|N_{K/\mathbb Q}(\delta)|
       =|\delta_0\delta_1|^2.
 \tag{25}
$$



Since $|\delta_0|\leq2H(\theta)$, (25) gives, at the growing embedding,



$$
|\nu_1(\theta_-)|
                   =\frac{|\delta_1|}{2}
                   \geq\frac1{4H(\theta)}.
 \tag{26}
$$



All the other terms in (19) are $O(H(\theta))$, whereas (15), (26)
give



$$
|T_d(\theta)|
    \geq c\frac{\varphi^d}{dH(\theta)}-C H(\theta)
 \tag{27}
$$



with absolute positive constants for all sufficiently large $d$.  The
constants are uniform in $\theta$.

It remains essential to pass through rational primitivization.  Write
$T_d(\theta)=a s+b$, choose a positive integer $q$ clearing both
rational coefficients, and let $g=\gcd(qa,qb)$.  The coefficient on
$s$ in (13) has all four conjugates uniformly bounded, so



$$
|a|\leq C_1H(\theta).
 \tag{28}
$$



If $a\ne0$, then $g\leq|qa|$.  Once
$\varphi^d/(dH(\theta)^2)$ is larger than a fixed constant, the first
term in (27) dominates the second, and the primitive form
$L=(q/g)T_d(\theta)$ satisfies



$$
|L|\geq\frac{|T_d(\theta)|}{|a|}
       \geq c_1\frac{\varphi^d}{dH(\theta)^2}.
 \tag{29}
$$



Under (4), the right side tends to infinity.  If $a=0$, a nonzero
primitive form is a nonzero integer constant and has modulus at least one.
This proves the height-barrier assertion in the verdict.  It also makes
(5) quantitative: choose a fixed $R_0$ large enough that the first term
of (27) dominates whenever
$\varphi^d/(dH(\theta)^2)\geq R_0$.  Then (29) is bounded below by the
positive constant $c_1R_0$.  A sequence of primitive traces tending to
zero must therefore eventually have
$\varphi^d/(dH(\theta)^2)<R_0$, which is (5) with
$c_0=R_0^{-1/2}$.

For the three units (6), there is a fixed $C_3>1$ such that



$$
H(u_3^{m_3}u_7^{m_7}u_9^{m_9})
       \leq C_3^{|m_3|+|m_7|+|m_9|}.
 \tag{30}
$$



Thus every exponent sequence with
$\max|m_j|=o(d)$ satisfies (4) and is rigorously excluded.

## 5. What happens at linear and larger exponent height

The four raw conjugate exponential rates of $\Theta_d$, in the embedding
order $w\mapsto w^k$, $k=1,3,7,9$, are



$$
(-1,1,1,0)\log\varphi.
 \tag{31}
$$



Let $L_{k,a}=\log|\sigma_k(u_a)|$.  The three columns of $L$ span the
sum-zero hyperplane.  Ignoring signs and exact additive cancellation, the
smallest possible largest summand is obtained by solving



$$
L\begin{pmatrix}m_3/d\\m_7/d\\m_9/d\end{pmatrix}
  =\left(\frac54,-\frac34,-\frac34,\frac14\right)\log\varphi.
 \tag{32}
$$



Numerically this gives



$$
(m_3,m_7,m_9)/d
      \approx(0.33286442,\,0.41713558,\,-0.25984752).
 \tag{33}
$$



At this balance the unit height is about $\varphi^{5d/4}$, while all
four largest raw summands have scale $\varphi^{d/4}$, up to powers of
$d$.  Equations (32)--(33) are a tropical diagnostic, not a lower bound
for the signed trace.  Exact cancellation could occur on a balancing wall,
and the gcd formed after taking the trace is not controlled by the
coefficient-field content ideal from the untraced form.

The reproducible exact search over $|m_3|,|m_7|,|m_9|\leq7$, together
with exact quadratic-ray checks and the continuous balance, is in
<scripts/cyclotomic_unit_trace_probe.py> and
<results/cyclotomic_unit_trace_probe.json>.  Its finite minima are not used
in any proof.  To turn the remaining regime into a successful construction
one would still need all three of the following:

1. a nonzero signed trace cancellation stronger than the generic
   $\varphi^{d/4}$ balance;
2. an exact all-degree lower bound for the rational coordinate gcd after
   the trace, or an explicit recurrence proving that the primitive scaling
   survives;
3. a decreasing certified value for the resulting primitive integer form.

No such family is present in the computed range, and none of these three
requirements is proved in the exponentially large-height regime.
