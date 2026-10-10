> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primary verification of the covering map, nearest branch, and elliptic parameters

Reviewer: main Codex. October 4, 2026. This note verifies the specific covering and parameters used by the project, without claiming full review of every page in the cited books.

The primary reviewer read complete original-page text on McMullen printed pages 37,95,96 and Beardon–Minda printed pages 41–43, visually inspecting McMullen 95/96 and Beardon–Minda 42. Complete original-page text on Dolgachev printed pages 115–119 was also read, with visual inspection of 116/117/118. Pinned originals, page texts, and images are preserved in the assistant's source directory. Original equations and context in official DLMF 23.15 and 20.9 were checked publicly, and the original HTTPS pages were separately saved by the assistant. Extraction, visual inspection, theorem adoption, and derivation here are recorded separately; these short reading scopes do not count as reviewing whole books.

## 1. Group action and the classification result that may be adopted

McMullen's fractional-linear-group convention already identifies the central element −I. Strictly, the effective group acting on the upper half-plane is Γ(2)/{±I}. Since −I belongs to Γ(2) in SL(2,Z), the matrix group cannot itself simply be called torsion-free. The effective quotient acts freely and properly discontinuously on the upper half-plane.

Cross-ratio classification of four ordered branch points gives a biholomorphic identification of the upper-half-plane quotient with C\{0,1}. Ordered marking of the 2-torsion points must be retained. Unmarked elliptic-curve isomorphism gives the larger SL(2,Z) quotient and six parameter choices. Dolgachev 9.1/9.2 provides the marked classification; McMullen's general description can be used with the marking retained. The standard parameter and its complementary parameter are coordinates for the same covering.

Several typographic or convention issues in the originals must be isolated. McMullen 96 omits a square root in the elliptic differential. Dolgachev 116 writes GL(2,Z) at an orbit previously defined with GL(2,C), and its signs in translation to Weierstrass form disagree. The denominator in formula 9.5 on 117 disagrees with the cross-ratio definition and 9.13 on 118; one λ index on 118 is swapped to the complementary parameter. Original PDF images confirm these literal issues. These formulas cannot be copied directly as computational definitions, but the correct ordered-marking classification is not thereby invalidated.

Original sources: [McMullen course notes](https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/10/html/home/course/course.pdf), [pinned Dolgachev version](https://websites.umich.edu/~lagarias/678books/ModularBook-171026.pdf). Source fingerprints are in the assistant's preservation register.

## 2. Project parameters and the local inverse branch

Fix



$$
\Omega=\mathbb C\setminus\{1-i,1+i\},\qquad
z(w)=\frac{w-(1-i)}{2i}.
$$



Then z(0)=(1+i)/2=:z_0 and z(1)=1/2. Use the standard parameter
$\lambda=\theta_2^4/\theta_3^4$, and write the elliptic integral in parameter form



$$
\mathcal K(z)=\frac\pi2 H(z),\qquad
H(z)=\sum_{k\ge0}\binom{2k}{k}^2\frac{z^k}{16^k}.
$$



It satisfies $\mathcal K(z)=K(\sqrt z)$ relative to the DLMF modulus form. Along the straight segment from z=1/2 to z=z_0, choose the continuous branch



$$
\tau(z)=i\frac{\mathcal K(1-z)}{\mathcal K(z)},\qquad \tau(1/2)=i.
$$



Official [DLMF 23.15](https://dlmf.nist.gov/23.15) and [20.9](https://dlmf.nist.gov/20.9) give the standard theta/modulus and local inverse relations. The specific path choice is supplied here. On Re z=1/2, 0≤Im z≤1/2, each $(1-zs^2)^{-1/2}$ in the integral representation has argument in [0,π/8), so $\mathcal K$ is nonzero. Along the path, $\mathcal K(1-z)$ is its conjugate, and $\tau$ continuously lies on the upper unit semicircle. Connecting to the known standard inverse at z=1/2 and analytically continuing gives the required local inverse, rather than an arbitrary deck translate.

Write H(z_0)=A+iB and t=B/A. The integral argument directly gives A>0 and 0<B/A<tan(π/8)<1/2. Therefore



$$
\tau_0=\tau(z_0)=u+iv,
\quad u=\frac{2t}{1+t^2},\quad
v=\frac{1-t^2}{1+t^2}>\frac35,\quad |\tau_0|=1.
$$



## 3. Quotient-surface distance and the nearest deck branch at this point

Local isometry of the covering means that every base path starting at a fixed lift uniquely lifts to another fiber point with the same length. Conversely, a path between two lifts in the upper half-plane projects with its length preserved. Hence



$$
d_\Omega(0,1)
=\inf_{\gamma\in\Gamma(2)/\{\pm I\}}
d_{\mathbb H}(\tau_0,\gamma i).
$$



This equality follows from path lifting and lengths, rather than defining distance through an unproved nearest-branch claim. Beardon–Minda 10.3 supplies local isometry and the curvature −1 normalization; the primary reviewer derives the quotient-distance formula here.

For $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma(2)$, c is even, d is odd, and



$$
\gamma i=\frac{ac+bd+i}{c^2+d^2}.
$$



If c=0, $\gamma i=2k+i$. Since |u|<1, i is uniquely nearest among these points. If c≠0, c²+d²≥5, so y=Im(γi)≤1/5. The upper-half-plane distance formula gives



$$
\cosh d_{\mathbb H}(\tau_0,\gamma i)
\ge\frac{v/y+y/v}{2}
\ge\frac{5v+1/(5v)}2
>\frac1v
=\cosh d_{\mathbb H}(\tau_0,i).
$$



The final strict comparison is precisely v>3/5. A finite group-element scan is not substituted for the infinite orbit. The distance is therefore attained at this path's endpoint i.

Since |τ_0|=1, substitution into pseudohyperbolic distance also gives



$$
\left|\frac{i-\tau_0}{i-\overline{\tau_0}}\right|=t,
\qquad d_\Omega(0,1)=2\operatorname{artanh}t.
$$



Original metric source: [complete Beardon–Minda notes](https://www.math.stonybrook.edu/~bishop/classes/math401.F09/Beardon-Minda.pdf). Their covering-existence statement in 10.2 cites earlier material. This note uses the classical covering/local-isometry theorem and does not claim that the short cited passage independently proves existence.

## 4. Covering derivative and the exact scale of the first integer jet

The parameter-form hypergeometric equation and its Wronskian give



$$
\tau'(z)=-\frac{i\pi}{4z(1-z)\mathcal K(z)^2}.
$$



The primary reviewer can determine the constant directly. As z→0, $\mathcal K(z)\sim\pi/2$ and $\mathcal K(1-z)\sim\frac12\log(16/z)$. Substitution into the numerator Wronskian gives −π/(4z), and the differential equation makes the remaining factor exactly 1/(1-z). The variable is parameter z, not modulus k.

For curvature −1, upper-half-plane density is 1/Im τ and disk density at zero is 2. Using |z'(w)|=1/2 and |z_0(1-z_0)|=1/2 gives



$$
\lambda_\Omega(0)
=\frac{|\tau'(z_0)|}{2\operatorname{Im}\tau_0}
=\frac1{\pi(A^2-B^2)}.
$$



Thus the normalized covering p:D→Ω with p(0)=0 and p'(0)>0 satisfies



$$
a=p'(0)=2\pi(A^2-B^2).
$$



Real-axis reflection lifts to disk reflection. With this derivative normalization, its fixed diameter is the real diameter. The real path 0→1 lifts to positive real t, with p(t)=1. For a real-coefficient polynomial φ satisfying φ(0)=0 and φ(1)=1, its real [0,1] path is endpoint-homotopic to the straight segment in Ω. The lift of φ starting at zero therefore has this same endpoint, rather than an arbitrary different fiber point.

This verifies a,t, the curvature convention, and the specific branch used in the first-integer-jet and subsequent Schur manuscripts. Existing exact series controls separately verify numerical intervals and radius constants. No conclusion about rational endpoint denominators, integral-coefficient heights, or irrationality of e+π is given here.
