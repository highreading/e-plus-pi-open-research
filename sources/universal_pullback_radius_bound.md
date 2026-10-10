> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A universal hyperbolic upper bound for pullback radius

## Scope and theorem

Let



$$
F(w)=4\arctan\frac{w}{2-w}.
$$



Its only finite continued-germ singularities are $1-i$ and $1+i$.
Suppose that $\phi$ is holomorphic on a disk containing $0$ and $1$,
with



$$
\phi(0)=0,\qquad \phi(1)=1.
$$



If $\phi$ avoids $1\pm i$ on $|z|<R$, then



$$
\boxed{R\leq R_*<5.262410788162386,}
\tag{1}
$$



where $R_*$ is the exact hyperbolic constant defined below and



$$
R_*=5.2624107881623850775528279\ldots
\tag{2}
$$



numerically.  In particular, for every polynomial $\phi$ fixing $0$
and $1$, the Taylor radius of $F\circ\phi$ is at most $R_*$.

The constant is sharp in the larger class of arbitrary holomorphic maps:
there is a holomorphic map from the disk $|z|<R_*$ into
$\mathbb C\setminus\{1-i,1+i\}$ taking $0$ to $0$ and $1$ to
$1$.  The extremal map need not be a polynomial, have real coefficients,
or have integral derivative jets.  Thus (1) is a universal analytic ceiling,
not an attainable arithmetic construction.

For the polynomial consequence, no cancellation is hidden.  If
$\phi(z)-(1+i)$ has a zero of multiplicity $m$, then $\phi'$ has
multiplicity exactly $m-1$ there, and



$$
(F\circ\phi)'(z)=
\frac{4\phi'(z)}
 {(\phi(z)-(1+i))(\phi(z)-(1-i))}
$$



has a simple pole.  The same holds over $1-i$.  Thus every preimage is a
genuine logarithmic singularity, and applying (1) to every smaller disk and
then taking a limit bounds the Taylor radius.

## 1. Reduction to the twice-punctured plane

Set



$$
\Omega=\mathbb C\setminus\{1-i,1+i\}
$$



and use the affine coordinate



$$
T(w)=\frac{w-(1-i)}{2i}.
\tag{3}
$$



Then $T$ maps $\Omega$ conformally onto
$X=\mathbb C\setminus\{0,1\}$, and



$$
T(1)=\frac12,\qquad T(0)=\frac{1+i}{2}.
\tag{4}
$$



Let $d_X$ denote the complete hyperbolic distance of curvature $-1$
on $X$, and put



$$
\delta=d_X\left(\frac12,\frac{1+i}{2}\right).
\tag{5}
$$



If $\phi$ avoids the two punctures on the disk
$\mathbb D_R=\{|z|<R\}$, Schwarz--Pick gives



$$
\delta=d_\Omega(0,1)
\leq d_{\mathbb D_R}(0,1)
=2\operatorname{artanh}\frac1R.
\tag{6}
$$



Solving (6) yields



$$
R\leq\coth\frac{\delta}{2}.
\tag{7}
$$



It remains to evaluate the positive constant $\delta$.

## 2. Exact modular-uniformization formula

The modular lambda function



$$
\lambda:\mathbb H\longrightarrow
\mathbb C\setminus\{0,1\}
$$



is a universal covering with deck group $\Gamma(2)$ modulo its central
sign.  A principal inverse is



$$
\tau(z)=i\frac{K(1-z)}{K(z)},
\tag{8}
$$



where $K$ is the complete elliptic integral with parameter $z$.
The standard value $\lambda(i)=1/2$ gives the lift $i$ of the first
point in (5).  For



$$
z_1=\frac{1+i}{2},\qquad
\tau_1=\tau(z_1)=x+iy,
\tag{9}
$$



complex conjugation gives



$$
1-z_1=\overline{z_1},\qquad
K(1-z_1)=\overline{K(z_1)}.
$$



Therefore



$$
\tau_1=i\frac{\overline{K(z_1)}}{K(z_1)},
\qquad |\tau_1|=1.
\tag{10}
$$



The exact rational enclosure in Section 4 proves $0<y<1$, so
$\tau_1\in\mathbb H$.

The quotient distance is



$$
\delta=\inf_{\gamma\in\Gamma(2)}
d_{\mathbb H}(i,\gamma\tau_1).
\tag{11}
$$



We now show that the identity deck transformation realizes this infimum.
Write



$$
\gamma=
\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma(2).
$$



Thus $a,d$ are odd and $b,c$ are even.  The upper-half-plane distance
formula gives



$$
\cosh d_{\mathbb H}(i,\gamma\tau_1)
=
\frac{|a\tau_1+b|^2+|c\tau_1+d|^2}{2y}.
\tag{12}
$$



Because $|\tau_1|=1$ and $|x|<1$,



$$
|a\tau_1+b|^2=a^2+b^2+2abx\geq1.
\tag{13}
$$



Indeed, this is immediate when $b=0$; otherwise it is strictly larger
than $(|a|-|b|)^2$, which is at least $1$ because $|a|$ is odd and
$|b|$ is even.  The same parity argument gives



$$
|c\tau_1+d|^2\geq1.
\tag{14}
$$



Hence the numerator in (12) is at least $2$.  At the identity it is
$|\tau_1|^2+1=2$.  Thus (11) is attained at the identity and



$$
\cosh\delta
=\frac{|\tau_1|^2+1}{2y}
=\frac1y.
\tag{15}
$$



Combining (7) and the half-angle identity gives the exact constant



$$
\boxed{
R_*=\coth\frac{\delta}{2}
=\sqrt{\frac{\cosh\delta+1}{\cosh\delta-1}}
=\sqrt{\frac{1+y}{1-y}},
}
\tag{16}
$$



with



$$
y=\operatorname{Im}
\left(
i\frac{K((1-i)/2)}{K((1+i)/2)}
\right).
\tag{17}
$$



Equations (5), (8), and (16) are a definition of $R_*$ independent of
any numerical computation.

## 3. Sharpness in the unrestricted holomorphic class

Choose lifts of the two points in (5) whose distance is $\delta$;
Section 2 shows that $i$ and $\tau_1$ are such a pair.  Let



$$
p:\mathbb D\longrightarrow\Omega
$$



be a universal covering.  Disk automorphisms act transitively on ordered
pairs at a fixed hyperbolic distance.  Since



$$
2\operatorname{artanh}\frac1{R_*}=\delta,
$$



there is a disk automorphism $M$ such that the composition



$$
\Phi(z)=p\!\left(M(z/R_*)\right)
\tag{18}
$$



satisfies $\Phi(0)=0$ and $\Phi(1)=1$.  It avoids both punctures
throughout $|z|<R_*$.  This proves analytic sharpness.

The argument imposes no arithmetic condition on the Taylor coefficients
of $\Phi$; in particular, it does not show that the upper bound can be
approached by integral-Hurwitz polynomials.

## 4. Exact rational numerical certificate

The factor $\pi/2$ cancels in (8), so define



$$
H(z)=\frac{2K(z)}{\pi}
=\sum_{n=0}^{\infty}
\frac{\binom{2n}{n}^2}{16^n}z^n.
\tag{19}
$$



At $z_1=(1+i)/2$, write $H(z_1)=A+iB$.  Equation (10) gives



$$
y=\frac{A^2-B^2}{A^2+B^2}.
\tag{20}
$$



Every coefficient in (19) lies in $(0,1]$, and



$$
|z_1|=\frac1{\sqrt2}<\frac{71}{100}.
$$



After summing through index $N$, the omitted complex tail therefore has
the exact rational majorant



$$
\left|
\sum_{n>N}\frac{\binom{2n}{n}^2}{16^n}z_1^n
\right|
\leq
\frac{(71/100)^{N+1}}{1-71/100}.
\tag{21}
$$



For $N=180$, exact rational propagation of (21) through (20) proves



$$
0.930296508588526
<y<
0.930296508588527.
\tag{22}
$$



Substitution of the upper endpoint into the increasing function in (16),
followed by an exact rational square comparison, proves



$$
R_*<5.262410788162386.
\tag{23}
$$



The script
scripts/pullback_hyperbolic_radius_bound.py performs only rational
arithmetic for (21)--(23).  Its output is
results/pullback_hyperbolic_radius_bound.json.  Longer values of
$\tau_1$, $\delta$, and $R_*$ in that file are explicitly marked as
high-precision diagnostics.

## 5. Consequence for the current proof search

No endpoint-fixing analytic reparametrization can move both logarithmic
singularities arbitrarily far away.  The current exact construction with
radius $>3/2$ is still far below the universal ceiling $R_*$, so the
hyperbolic theorem does not rule out substantial improvement.  It does,
however, show that radius growth alone can never become an unbounded
resource.  Any successful Hermite--Padé construction must also obtain
arithmetic control of primitive height and endpoint gcd.
