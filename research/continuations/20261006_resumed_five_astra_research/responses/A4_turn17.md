> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, turn 17 — Correct source normalization, factorial-aligned observations, and saturation of the endpoint affine-depth obstruction

## Executive conclusions

The irrationality of $e+\pi$ remains unresolved. This report makes the following corrections, audits, and advances.

1. **The logarithmic-source label in A4 turn 16 was wrong.** The original source is
   

$$
\boxed{\mathcal L_m=m![z^m]\frac{F(z)}{1-z}},
$$


   not $m![z^m](e^zF(z))$. The finite sum used in turn 16 was nevertheless the correct sum for $F/(1-z)$. Consequently, both
   

$$
B_{\rm new}=n-v_2(b!)-2-3\ell
$$


   and the refinement
   

$$
\boxed{B_*=n-v_2(b!)-1-2s_2(n)-\ell}
$$


   remain valid for the **original complete source**. The erroneous packet is retained as history; this is a correction of its identification, not a replacement source.

2. **The common actual first-column content theorem is reused as closed:**
   

$$
\boxed{
   0\le a\le
   \max_{0\le j<b}v_2\binom{n+2}{j}-1
   \le\lfloor\log_2(n+2)\rfloor-1.
   }
$$


   No additional producer, independent finite verification, or rerun is needed.

3. **A5 turn 11’s factorial moment identity, integer scalar, complete residual, and exact scalar depth pass the audit.** In particular,
   

$$
y^E=c_nx+z^E,\qquad
   c_n\in\mathbb Z,\qquad
   \boxed{v_2(c_n)=d:=\frac n2-v_2(b!)-1}.
$$


   The sign of the scalar and the exterior return are correct. Its nonresonance theorem is valid with its stated hypotheses. The ensuing denominator divergence is a deduction using the retained whole-error theorem—not an unconditional exclusion of every original index.

4. **A new, original-source simultaneous-observation identity exposes the remaining norm obstruction.** If $!j$ denotes the derangement number, the same actual adjoint observations $\theta_j$ satisfy
   

$$
\boxed{
   \sum_{j=0}^{2n+b-1}!j\,\theta_j
   =\Lambda\,2^{a+1}R\,Q,
   \qquad Q=x_0^Tx_0.
   }
$$


   Thus the primitive norm is a **complete derangement-weighted observation**, whereas the exponential contraction is a paid factorial observation. This distinction matters: $!(2r)$ is odd, so the factorial-tail cutoff cannot be transferred to the norm observation term by term.

5. **The paid factorial observation gives a new norm-independent exclusion certificate.** A single nonzero exponential observation modulo
   

$$
2^{a+d+1}
$$


   proves
   

$$
\delta_2\le d-\nu\le d
$$


   even in the deep-norm regime where A5’s first-resonance guard might fail. The observation needs only the justified factorial prefix
   

$$
\boxed{
   j\le \frac n2+a+s_2(b)+\ell+2
   }
$$


   rather than the complete exponential-source length. This is an exact conditional certificate for the original producer. Its required nonvanishing has **not** been established uniformly.

6. **A3 turn 12’s fixed-seed observation determinant and third-force elimination pass the audit.** The determinant really contains $F$, up to large-prime units. The coordinate-content payment $\eta_j\mid 2(n+2)^2$, exact local ideal equality, divisibility chain, and $\mathcal W^{\rm ref}\mid\mathcal G$ are valid at their stated scope.

7. **There is a sharper full-depth endpoint theorem.** At a prime $p>n+2$, write
   

$$
f=v_p(F),\quad a=v_p(\mathcal I_n),\quad
   \zeta=v_p(\mathcal Z_j),\quad e=v_p(\mathcal E_j),\quad
   k=v_p(\Delta_j).
$$


   If $F\ne0$, then
   

$$
\boxed{
   k>f\quad\Longrightarrow\quad
   f=a+\zeta,\qquad e=\zeta.
   }
$$


   Thus affine depth beyond $F$ is confined to a **fully saturated force-overlap locus**. Off that locus, the entire depth—not just a clipped gcd—is bounded:
   

$$
\boxed{k\le a+\zeta.}
$$


   On the saturated locus, explicit unit-chart formulas below identify the exact remaining affine cancellation against the actual factorial scalar $\kappa$. This is stronger than merely introducing another gcd, but it still does not bound those unit resonances uniformly.

No computation was executed. No accepted calculation is proposed for repetition.

---

# 1. Original objects and finite boundaries

## 1.1 Binary family

All binary conclusions remain on


$$
\boxed{
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
}
$$


Set


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
R=2^{n/2}\binom n{n/2},\qquad
\Lambda=\frac{(n!)^2}{2^n},
$$




$$
W_j=\binom{n+2}{j},\qquad M=2n+b-1.
$$



The contact matrix has exactly $b$ rows and columns:


$$
A_{ij}
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
\qquad 0\le i,j<b,
$$


where


$$
\lambda_s=s![z^s]\phi(z)^n.
$$



The reconstruction has exactly the rows $0\le j\le b$:


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$



The actual corrected columns are


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
V_w=\mathcal RA^{-1}(h^e+h^F)+e_0,
$$




$$
x=\frac{Z_w}{2R},\qquad
y=\frac{V_w}{4b!}=y^E+y^F,
$$


with


$$
y^E=\frac{\mathcal RA^{-1}h^e+e_0}{4b!},
\qquad
y^F=\frac{\mathcal RA^{-1}h^F}{4b!}.
$$



No force term or exterior return is removed.

### Agreement with the complete contact excerpt

The excerpt uses $\widetilde N$, whose final binomial is
$\binom{n+i-s}{j}$. These are not different sources.

Let $S$ be the upper shift on the original $b$-dimensional contact space. Finite Vandermonde convolution gives


$$
A=\widetilde N(1+S)^n.
$$


Indeed,


$$
\binom{2n+i-s}{j}
=
\sum_{r=0}^{j}
\binom{n+i-s}{r}\binom n{j-r}.
$$


Consequently,


$$
\mathcal RA^{-1}
=
\operatorname{diag}(W_j)\mathcal Z(1+S)^{-n}\widetilde N^{-1},
$$


which is exactly the weighted reconstruction in the excerpt.

This is an identity of the original finite matrices. It does not continue the contact recurrence through row $b$.

## 1.2 Primitive denominator and whole error

Retain


$$
N=x^Tx,\qquad H=x^Ty,\qquad
\mathscr D_n=\frac{\Lambda R}{2b!}.
$$


The actual weighted integers and all-prime reduction remain


$$
A_B=d_B^2\,4\Lambda^2R^2N,\qquad
H_B=d_B^2\,8\Lambda Rb!H,
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


Thus


$$
\frac{p_n}{q_n}=\frac{H}{\mathscr D_nN},
$$


and, for every prime $p$,


$$
v_p(q_n)
=
\max\{v_p(\mathscr D_n)+v_p(N)-v_p(H),0\}.
$$



The whole error is


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


No exponential component is substituted for this whole evaluated error.

---

# 2. Source correction and survival of both logarithmic guards

## 2.1 The exact correction

The complete source excerpt defines


$$
\mathcal F_m=[z^m]\frac{F(z)}{1-z},
\qquad
\mathcal L_m=m!\mathcal F_m,
$$


where


$$
F'(z)=\frac2{\phi(z)},\qquad F(0)=0.
$$


Writing $g_r=F^{(r)}(0)$,


$$
\boxed{
\mathcal L_m
=
\sum_{r=1}^{m}\frac{m!}{r!}g_r.
}
\tag{2.1}
$$


Equivalently,


$$
\mathcal L_0=0,\qquad
\mathcal L_m=m\mathcal L_{m-1}+g_m.
$$



By contrast,


$$
m![z^m](e^zF(z))
=
\sum_{r=1}^{m}\binom mr g_r.
$$


These expressions differ. Since $g_1=g_2=g_3=2$, at $m=3$ they are respectively


$$
20\quad\text{and}\quad14.
$$



Accordingly, the displayed $e^zF$ identification in A4 turn 16, §3, is withdrawn. Its finite sum and subsequent valuation argument were for the correct expression (2.1).

The earlier erroneous source packet and its recorded hash remain part of the audit history. The coordinator’s addendum corrects that packet; it does not define a new forcing column.

## 2.2 Reverification of the paid estimate

The symbol expansion gives


$$
v_2(\lambda_s)
\ge
v_2(s!)-\lfloor s/2\rfloor
=
\lceil s/2\rceil-s_2(s).
\tag{2.2}
$$


Also,


$$
\frac1{\phi(z)}
=
\frac{1+z+z^2/2}{1+z^4/4},
$$


so


$$
v_2(g_r)
\ge
1+v_2((r-1)!)-\left\lfloor\frac{r-1}{2}\right\rfloor.
$$


Applying this to the **correct** sum (2.1) yields


$$
\boxed{
v_2(\mathcal L_m)
\ge
\left\lfloor\frac m2\right\rfloor+2
-s_2(m)-\lfloor\log_2m\rfloor.
}
\tag{2.3}
$$



In an original summand of $h_i^F$,


$$
m=2n+i-s,\qquad n\le m\le M,\qquad s+m=2n+i.
$$


With


$$
\ell=\lfloor\log_2M\rfloor,
$$


combining (2.2)–(2.3) gives


$$
v_2(h_i^F)\ge n+\lfloor i/2\rfloor-3\ell.
$$


The retained $2$-integrality of $A^{-1}$ and $\mathcal R$, followed by the actual division by $4b!$, proves


$$
\boxed{
y^F\in2^{B_{\rm new}}\mathbb Z_2^{b+1},
\qquad
B_{\rm new}=n-v_2(b!)-2-3\ell.
}
$$



## 2.3 The refined guard also survives

The refinement in turn 16 used


$$
\lambda_s\binom{n+i}{s}
=
\frac{(n+i)!}{(n+i-s)!}[z^s]\phi(z)^n
$$


and


$$
v_2((2n+i-s)!)-v_2((n+i-s)!)\ge v_2(n!).
$$


Together with the same correct bound (2.3), this gives


$$
v_2(h_i^F)
\ge
n+\left\lfloor\frac i2\right\rfloor+2
-s_2(n+i)-s_2(n)-\ell.
$$


Using


$$
s_2(n+i)\le s_2(n)+s_2(i),
\qquad
s_2(i)\le\lfloor i/2\rfloor+1,
$$


we recover


$$
v_2(h_i^F)\ge n+1-2s_2(n)-\ell.
$$


Hence


$$
\boxed{
y^F\in2^{B_*}\mathbb Z_2^{b+1},
\qquad
B_*=n-v_2(b!)-1-2s_2(n)-\ell.
}
\tag{2.4}
$$



Thus **both guards survive for the actual source**. Below, $B$ may be taken to be $B_*$; A5’s stated results with $B_{\rm new}$ remain valid.

---

# 3. Audit of A5’s exact factorial alignment

Write


$$
x=2^a x_0,\qquad
Q=x_0^Tx_0=2^\nu Q_*,
\qquad Q_*\in\mathbb Z_2^\times.
$$


The common theorem supplies


$$
0\le a\le\lfloor\log_2(n+2)\rfloor-1.
$$


It is reused, not reproved or recomputed here.

## 3.1 Formal substitution and complete moment identity

For $d_i=n+i$, the complete factorial moment is


$$
\begin{aligned}
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}(2n+i-s)!
&=
d_i!\sum_{s=0}^{d_i}
[z^s]\phi(z)^n\frac{(n+d_i-s)!}{(d_i-s)!}\\
&=
n!d_i![z^{d_i}]\phi(z)^n(1-z)^{-n-1}.
\end{aligned}
$$



The formal substitution


$$
[z^d]G(z)
=
[t^d](1+t)^{d-1}G\!\left(\frac t{1+t}\right)
$$


is correct: it follows directly by formal residue substitution, including the Jacobian $(1+t)^{-2}$.

Since


$$
\phi\!\left(\frac t{1+t}\right)
=
\frac{1+t+t^2/2}{(1+t)^2},
$$


the coefficient becomes


$$
[t^{n+i}](1+t+t^2/2)^n(1+t)^i.
$$


Reciprocation of this polynomial, of degree $2n+i$, gives


$$
2^{-n}[t^n](1+2t+2t^2)^n(1+t)^i.
$$


Therefore


$$
\boxed{
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}(2n+i-s)!
=
\Lambda f_i^0.
}
\tag{3.1}
$$



There is no sign error. The positive polynomial after reciprocation and the factor $2^{-n}$ are both correct.

The original $s$-range is preserved. Since $i<b<n$, it also agrees with the support convention in the complete excerpt.

## 3.2 Complete residual and all inner bounds

Let


$$
\sigma_n=\sum_{r=0}^n\frac1{r!}=\frac{\mathcal D_n}{n!}.
$$


Every factorial index $m=2n+i-s$ in the force satisfies $m\ge n$. Thus


$$
\mathcal D_m
=
\sigma_n m!
+
\sum_{r=n+1}^{m}\frac{m!}{r!}.
$$


The exact residual source is consequently


$$
\boxed{
\rho_i=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}
\sum_{r=n+1}^{2n+i-s}
\frac{(2n+i-s)!}{r!}.
}
\tag{3.2}
$$


The inner sum is empty when $2n+i-s=n$. No other endpoint is changed.

Equation (3.1) proves


$$
h^e=\sigma_n\Lambda f^0+\rho.
$$


Therefore


$$
\boxed{
y^E=c_nx+z^E,
\qquad
c_n=\mathscr D_n\sigma_n,
\qquad
z^E=\frac{\mathcal RA^{-1}\rho+e_0}{4b!}.
}
\tag{3.3}
$$



The $+e_0$ sign is correct.

## 3.3 Integer scalar and exact binary depth

Because $n$ is even,


$$
\mathcal D_n=n\mathcal D_{n-1}+1
$$


is odd. Also


$$
c_n
=
\mathcal D_n\,
\frac{(n!/b!)\binom n{n/2}}{2^{n/2+1}}.
$$


The numerator before the binary division is an integer; its valuation is


$$
v_2(n!)-v_2(b!)
+v_2\binom n{n/2}
=
n-v_2(b!).
$$


Here


$$
v_2\binom n{n/2}=s_2(n).
$$


It follows that


$$
\boxed{
c_n\in\mathbb Z,\qquad
v_2(c_n)=d=\frac n2-v_2(b!)-1.
}
\tag{3.4}
$$



There is no unaccounted odd-prime denominator.

The integrality of $z^E$ follows from the complete identity


$$
z^E=y^E-c_nx.
$$


This pays the **whole** $4b!$-division in (3.3); it does not make that division legitimate term by term in the displayed double sum.

Finally, for $t=(j!)_{0\le j<b}$,


$$
\mathcal Rt=-e_0+b!W_be_b.
$$


Hence


$$
\boxed{
z^E=
\frac{\mathcal RA^{-1}(\rho-At)+b!W_be_b}{4b!}.
}
\tag{3.5}
$$


The finite terminal is retained exactly.

## 3.4 Relative depth and denominator consequence

Put


$$
E=x_0^Ty^E,\qquad
\Psi=x_0^Tz^E,\qquad
L=x_0^T(2^{-B}y^F),\qquad z=a+\nu.
$$


Writing $c_n=2^du_n$, with $u_n$ a binary unit,


$$
\boxed{
\delta_2
=
v_2\!\left(2^{z+d}u_nQ_*+\Psi+2^BL\right)-z.
}
\tag{3.6}
$$



If


$$
z+d<B,\qquad v_2(\Psi)\ne z+d,
$$


then the unequal-valuation rule gives


$$
\boxed{
\delta_2
=
\min\{d,v_2(\Psi)-z\}\le d.
}
\tag{3.7}
$$



A5’s guard


$$
z<\frac n2-1-3\ell
$$


is exactly $z+d<B_{\rm new}$. With the audited refinement, it may be enlarged to


$$
\boxed{
z<\frac n2-2s_2(n)-\ell.
}
\tag{3.8}
$$



All of A5’s protected, intermediate, and deep-regime congruences follow correctly from (3.6). The strict guard protects a digit; a non-strict guard suffices for the corresponding divisibility test.

Using the actual denominator,


$$
v_2(q_n)\ge C_n-d=n-s_2(n)
$$


whenever $\delta_2\le d$. Combining this with the retained exact ternary law,


$$
v_3(q_n)=n-\frac{b+15}{2},
$$


gives


$$
q_n\ge 2^{n-s_2(n)}3^{n-(b+15)/2}.
$$


Under the retained whole-error theorem,


$$
\log|\epsilon_n|=-\beta n+o(n),
$$


the growth margin is


$$
\log2+\left(1-\frac1{8004}\right)\log3-\beta
=0.02865\ldots>0.
$$


Thus


$$
|q_n\epsilon_n|\to\infty
$$


along any infinite original sequence satisfying the nonresonance hypotheses.

**Audit verdict:** A5’s arithmetic identities and conditional implications are correct. The nonresonance hypotheses are not proved uniformly.

---

# 4. New simultaneous observations: factorial forcing versus the actual norm

The factorial alignment and the paid-tail identity can be combined without replacing either observable.

## 4.1 The actual common adjoint

Define


$$
w=A^{-T}\mathcal R^Tx_0\in\mathbb Z_2^b.
$$


For $0\le j\le M$, let


$$
(\mathbf a_j)_i
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}
\binom{2n+i-s}{j},
$$


and


$$
\theta_j=w^T\mathbf a_j.
$$


These observations are $2$-integral. For $j<b$, $\mathbf a_j$ is the actual $j$-th column of $A$; for $j\ge b$, it is only a source column, not an added contact column.

The first-source observation is


$$
\boxed{
w^Tf^0=2^{a+1}R\,Q.
}
\tag{4.1}
$$



## 4.2 A derangement observation for the norm

Let


$$
!j=j!\sum_{r=0}^{j}\frac{(-1)^r}{r!}
$$


be the integer derangement number, with $!0=1$.

The elementary finite identity


$$
m!=\sum_{j=0}^{m}\binom mj\,!j
\tag{4.2}
$$


follows, for example, by partitioning permutations according to their non-fixed points. It is also an immediate binomial inversion identity.

Insert (4.2) into the complete factorial moment (3.1), then interchange finite sums. This proves


$$
\Lambda f^0=\sum_{j=0}^{M}!j\,\mathbf a_j.
$$


Contracting with the **same** $w$ gives the new identity


$$
\boxed{
\mathcal U:=
\sum_{j=0}^{M}!j\,\theta_j
=
\Lambda\,2^{a+1}R\,Q.
}
\tag{4.3}
$$


In particular,


$$
\boxed{
v_2(\mathcal U)
=
\frac{3n}{2}+a+1-s_2(n)+\nu.
}
\tag{4.4}
$$



This is an exact original-force representation of the primitive norm loss. It is not an arbitrary quadratic-lattice example.

## 4.3 The factorial observation and complete residual

The complete exponential identity remains


$$
h^e=\sum_{j=0}^{M}j!\mathbf a_j.
$$


For $j<b$,


$$
\theta_j=(j+1)W_{j+1}x_{0,j+1}-W_jx_{0,j}.
$$


Consequently,


$$
\sum_{j=0}^{b-1}j!\theta_j
=-x_{0,0}+b!W_bx_{0,b},
$$


and


$$
\boxed{
4E
=
W_bx_{0,b}
+\sum_{j=b}^{M}\frac{j!}{b!}\theta_j.
}
\tag{4.5}
$$



Combining (4.3) and (4.5) with $E=c_n2^aQ+\Psi$ yields


$$
\boxed{
4\Psi
=
W_bx_{0,b}
+\sum_{j=b}^{M}\frac{j!}{b!}\theta_j
-\frac{\sigma_n}{b!}\sum_{j=0}^{M}!j\,\theta_j.
}
\tag{4.6}
$$


The coefficient and sign of the norm-aligned term are exact:


$$
\frac{\sigma_n}{b!}\mathcal U
=4c_n2^aQ.
$$



Equation (4.6) is a complete relative-source identity. It includes the physical terminal and both full observations.

## 4.4 Why factorial truncation does not bound the norm

The factorial observation admits the paid cutoff because


$$
v_2(j!/b!)\longrightarrow\infty.
$$


The derangement observation does not have the same property. The recurrence


$$
!j=(j-1)(!(j-1)+!(j-2))
$$


shows that


$$
\boxed{!(2r)\ \text{is odd}.}
$$


Thus, at arbitrarily large even indices within the source, its weights remain binary units.

Moreover,


$$
v_2(\sigma_n)=-v_2(n!).
$$


Therefore the last sum in (4.6) cannot be truncated by applying the factorial-tail argument to its individual terms. Its large valuation is a property of the **whole evaluated observation** (4.3).

This identifies a precise obstruction:

> The paid exponential tail controls the cost of observing $E$. It does not, by itself, control $\nu$, because the actual norm is represented by a different complete weight sequence with no factorial valuation decay.

Any successful forced-norm lemma must control (4.3) using the actual common adjoint and source columns.

---

# 5. A norm-independent half-length exclusion certificate

The preceding identities also provide a useful improvement that does not require a prior bound on $\nu$.

## 5.1 Paid prefix at arbitrary depth

For $S\ge0$, choose $J\le M$ such that either $J=M$, or


$$
v_2((J+1)!/b!)\ge S+2.
$$


Define the finite bracket


$$
P_J=
W_bx_{0,b}
+\sum_{j=b}^{J}\frac{j!}{b!}\theta_j.
$$


Then


$$
\boxed{4E\equiv P_J\pmod{2^{S+2}}.}
\tag{5.1}
$$


A sufficient cutoff is


$$
J=\min\{M,b+S+\ell+2\}.
\tag{5.2}
$$


The two extra bits pay the whole division by $4$.

## 5.2 The new certificate

Take


$$
S=a+d+1.
$$


On every original index,


$$
B_*>S.
$$


Indeed,


$$
B_*-(a+d+1)
=
\frac n2-2s_2(n)-\ell-a-1,
$$


which is positive throughout the original family, using the closed logarithmic bound for $a$.

### Theorem 5.1 — Norm-independent exponential exclusion

If


$$
\boxed{
P_J\not\equiv0\pmod{2^{a+d+3}},
}
\tag{5.3}
$$


with the paid cutoff for $S=a+d+1$, then


$$
\boxed{\delta_2\le d-\nu\le d.}
\tag{5.4}
$$



#### Proof

Equation (5.1) and (5.3) give


$$
v_2(E)<a+d+1,
$$


hence $v_2(E)\le a+d$. Since $B_*>a+d+1$, the complete logarithmic contribution cannot change this valuation. Therefore


$$
\delta_2
=
v_2(E+2^{B_*}L)-a-\nu
=
v_2(E)-a-\nu
\le d-\nu.
$$


No upper bound for $\nu$ was used. ∎

The sufficient endpoint (5.2) simplifies:


$$
\begin{aligned}
b+S+\ell+2
&=b+a+d+1+\ell+2\\
&=\frac n2+a+s_2(b)+\ell+2.
\end{aligned}
$$


Thus the certificate requires only


$$
\boxed{
J\le \frac n2+a+s_2(b)+\ell+2
=\frac n2+O(\log n).
}
\tag{5.5}
$$



This improves the organization of the outstanding problem:

* If the half-length observation has a nonzero digit at this precision, the original route fails at that index regardless of how deep its primitive norm is.
* If it vanishes, the norm/residual problem remains; no conclusion about $\nu$ follows.

Under the retained whole-error theorem, an infinite original sequence satisfying (5.3) has


$$
|q_n\epsilon_n|\to\infty.
$$



### Status and limitation

The theorem is rigorous. The required nonzero residues have not been evaluated or proved uniformly.

It does not authorize a short contact matrix, a shortened original force, or a truncated norm observation. It is a paid evaluation identity for one contraction of the original finite producer.

---

# 6. Independent audit of A3’s fixed-seed and elimination results

For this section, the domain is separately


$$
\boxed{
n=15^r\ \text{or}\ n=105^r,\qquad r\ge2,
}
$$


with


$$
m=n+1,\qquad N=n+2.
$$



## 6.1 Fixed-seed observation determinant

The moment recurrence


$$
a_{k+1}
=(k+1-n)a_k
+\frac{k(2n-k-1)}2a_{k-1}
+\frac{k(k-1)}2a_{k-2}
$$


and fixed seed


$$
(a_0,a_1,a_2)=(1,1-n,(n-1)^2)
$$


are consistent with


$$
\phi A_n'=(\phi+n\phi')A_n,
\qquad A_n=e^z\phi^n.
$$



For A3’s transfer matrix,


$$
\det\mathsf C_n
=\chi_n
=\frac{(n-1)!\,n!}{2^{n-1}}.
$$


The stated map from the terminal moment state to $(P,Q,F)$ has


$$
\det\mathsf L_n=4m^3nN.
$$


Both determinants are units at every $p>N$.

The exterior pullback is also correct:


$$
\mathsf C_n^T(s_n\times v_n^{\rm ref})
=s_1\times\operatorname{adj}(\mathsf C_n)v_n^{\rm ref}.
$$


For the actual observation matrix


$$
\mathsf O_n=\mathsf U_n\operatorname{adj}(\mathsf C_n)\mathsf V_n,
$$


the cross-product calculation gives


$$
\det\mathsf O_n
=
\chi_n\,s_n\cdot(v_h\times v_\ell),
$$


where


$$
v_h\times v_\ell
=
2nN
\begin{pmatrix}
mn\\m(n-3)\\-2(n-1)
\end{pmatrix}.
$$


Since


$$
F=2m\bigl(mn\,a_{n-1}+m(n-3)a_n-2(n-1)a_{n+1}\bigr),
$$


one obtains


$$
\boxed{
\det\mathsf O_n=\frac{nN}{m}\chi_nF.
}
\tag{6.1}
$$



The sign and normalization are correct. At $p>N$,


$$
v_p(\det\mathsf O_n)=v_p(F)
$$


when $F\ne0$. If $F=0$, the observation is singular.

Thus the proposed automatic-primitivity argument fails at the **actual evaluated observation**, not at the invertible moment transfer. This is a target-specific obstruction, not an arbitrary-companion example.

## 6.2 Third force identity and coordinate content

Retain A3’s notation


$$
P\alpha+Q\beta+F\gamma=0,
$$




$$
\mathcal E=A\alpha+B\beta+C\gamma,\qquad C=mZ,
$$




$$
M=Q\widehat h-P\widehat\ell,
$$




$$
\Theta
=CM-F(\widehat hB-\widehat\ell A)+\kappa F,
\qquad
\kappa=2L(n!)^2,
$$




$$
\widehat R=\alpha\widehat h+\beta\widehat\ell.
$$



The third identity is


$$
\boxed{
\gamma(\Theta-\kappa F)
=
M\mathcal E-(QA-PB)\widehat R.
}
\tag{6.2}
$$


Expanding both sides and using the syzygy verifies the sign.

For an actual primitive integral contact row $r_j$, multiplication by the coordinate matrix of determinant $2N^2$ gives


$$
\eta_j=\gcd(\alpha_j,\beta_j,\gamma_j)\mid2N^2.
$$


This follows by multiplying back by the adjugate and using the primitiveness of $r_j$. It does **not** assert $\eta_j=1$ over $\mathbb Z$.

The three identities, combined with a Bézout relation for $\eta_j$, imply


$$
\eta_j(\Theta-\kappa F)\in(\widehat R_j,\mathcal E_j).
$$


Since $\eta_j$ and $\kappa$ are units at $p>N$,


$$
\boxed{
(\Theta,\widehat R_j,\mathcal E_j)
=
(F,\widehat R_j,\mathcal E_j)
\quad\text{in }\mathbb Z_p.
}
\tag{6.3}
$$


Consequently,


$$
\boxed{
\gcd(\Delta_j,|\mathcal E_j|)
=
\gcd(F,\widehat R_j,\mathcal E_j)_{>N}.
}
$$



The claim is exact at all depths, not just modulo $p$.

## 6.3 The divisibility chain and filtered certificate

A3’s proof of


$$
\boxed{
\mathcal Z_j\mid\mathcal K_j\mid\mathcal J_j
\mid\mathcal I_n\mathcal Z_j,
\qquad
\operatorname{lcm}(\mathcal I_n,\mathcal Z_j)\mid\mathcal J_j
}
\tag{6.4}
$$


is valid, where


$$
\mathcal Z_j=\gcd(Z,\alpha_j,\beta_j)_{>N},
\quad
\mathcal K_j=\gcd(\Delta_j,|\mathcal E_j|),
\quad
\mathcal J_j=\gcd(\Delta_j,|F|).
$$



The primitive reference pair and the primitive moment state are essential to the transverse-content step. Their large-prime primitiveness follows from the stated invertible recurrences and fixed seeds; it is not inferred from a generic companion.

Also,


$$
\mathcal W^{\rm ref}\mid\mathcal W,
\qquad
\mathcal W^{\rm ref}\mid\Delta_0\Delta_3
\mid|\widehat R_0\widehat R_3|
$$


does imply


$$
\boxed{\mathcal W^{\rm ref}\mid\mathcal G.}
$$


This is a divisibility conclusion, not a height estimate.

---

# 7. New endpoint theorem: excess affine depth requires saturation

The following strengthens the clipped-overlap result to a full-depth statement off a precisely described locus.

Fix an original endpoint $j$ and a prime $p>N$. Suppress $j$ temporarily. Write


$$
f=v_p(F),\quad \mu=v_p(M),\quad
e=v_p(\mathcal E),\quad r=v_p(\widehat R),
$$




$$
a=v_p(\mathcal I_n)=\min(f,\mu),
\quad
\zeta=v_p(\mathcal Z_j),
\quad
k=v_p(\Delta_j)=\min(v_p(\Theta),r).
$$



If $F=0$, then $\mathcal J_j=\Delta_j$, so (6.4) already bounds the full depth:


$$
k\le a+\zeta.
$$


The new excess analysis is needed only when $F\ne0$, so $f<\infty$.

## 7.1 Necessary saturation

### Theorem 7.1 — Saturation of every depth beyond $F$

If


$$
k>f,
$$


then


$$
\boxed{
f=a+\zeta,\qquad e=\zeta.
}
\tag{7.1}
$$



#### Proof

The first two integral identities can be written


$$
\alpha\Theta
=\mathcal T\widehat R+F(\widehat\ell\mathcal E+\kappa\alpha),
$$




$$
\beta\Theta
=\mathcal S\widehat R+F(-\widehat h\mathcal E+\kappa\beta).
$$


Since $p^k\mid\Theta,\widehat R$, division by the paid factor $p^f$ gives


$$
\widehat\ell\mathcal E+\kappa\alpha
\equiv0\pmod{p^{k-f}},
$$




$$
-\widehat h\mathcal E+\kappa\beta
\equiv0\pmod{p^{k-f}}.
\tag{7.2}
$$



First suppose $e>0$. Then (7.2) implies $p\mid\alpha,\beta$. Since the actual coordinate row is primitive at $p>N$, $\gamma$ is a unit.

The third identity gives


$$
\gamma\Theta
=-(QA-PB)\widehat R+M\mathcal E+\kappa F\gamma.
$$


Hence


$$
M\mathcal E+\kappa F\gamma\equiv0\pmod{p^k}.
$$


Because $k>f$ and $\gamma,\kappa$ are units, its two summands must have equal valuation:


$$
\mu+e=f.
$$


In particular, $\mu<f$, so $a=\mu$.

The exact elimination gives


$$
v_p(\mathcal K_j)=\min(k,e)=e,
$$


while $v_p(\mathcal J_j)=f$. The chain (6.4) therefore yields


$$
\zeta\le e,\qquad f\le a+\zeta=\mu+\zeta.
$$


Together with $f=\mu+e$, this forces


$$
\zeta=e,\qquad f=a+\zeta.
$$



Now suppose $e=0$. Then $v_p(\mathcal K_j)=0$, so $\zeta=0$. Since $v_p(\mathcal J_j)=f$, (6.4) gives


$$
f\le a+\zeta=a\le f.
$$


Thus $a=f$, proving (7.1). ∎

### Corollary 7.2 — Full-depth bound off saturation

If either


$$
f\ne a+\zeta
\quad\text{or}\quad
e\ne\zeta,
$$


then


$$
\boxed{
k\le f,\qquad k=v_p(\mathcal J_j)\le a+\zeta.
}
\tag{7.3}
$$



This bounds the **whole affine depth** at such a prime. It is not merely a bound on $\min(k,e)$.

For example, if $\mathcal E$ is a unit and $\mu<f$, then $\zeta=0$, $a=\mu<f$, and


$$
\boxed{k=a.}
\tag{7.4}
$$


This controls an actual unit-force case left unbounded by the clipped force-overlap quantity alone.

## 7.2 Exact unit chart on the positive-force saturation locus

Suppose


$$
e=\zeta>0,\qquad f=a+\zeta.
$$


Then $\gamma$ is a unit, $a=\mu$, and $\mu+e=f$. Define the actual unit


$$
\Omega_\gamma
=
\frac{M\mathcal E}{\kappa F\gamma}\in\mathbb Z_p^\times.
$$


The third identity and the unit $\gamma$ give equality of ideals


$$
(\Theta,\widehat R)
=
(\widehat R,M\mathcal E+\kappa F\gamma).
$$


Thus


$$
\boxed{
k=
\min\left\{
r,\,
f+v_p(1+\Omega_\gamma)
\right\}.
}
\tag{7.5}
$$


In particular,


$$
\boxed{
(k-f)_+
=
\min\left\{
(r-f)_+,\,
v_p(1+\Omega_\gamma)
\right\}.
}
\tag{7.6}
$$



The remaining depth is an explicit resonance of the complete evaluated force against the actual factorial scalar $\kappa$.

## 7.3 Unit-force saturation

Suppose


$$
e=\zeta=0,\qquad a=f.
$$


If $p\mid\alpha,\beta$, then $k>f$ is impossible by (7.2), since $(\widehat h,\widehat\ell)$ is primitive. Since $a=f$ already divides $\Delta_j$, in this case


$$
\boxed{k=f.}
$$



Otherwise choose a unit coordinate.

If $\alpha$ is a unit, define


$$
\Omega_\alpha=\frac{\widehat\ell\mathcal E}{\kappa\alpha}\in\mathbb Z_p.
$$


The first identity gives


$$
\boxed{
k=\min\{r,f+v_p(1+\Omega_\alpha)\}.
}
\tag{7.7}
$$



If $\beta$ is the chosen unit, define


$$
\Omega_\beta=-\frac{\widehat h\mathcal E}{\kappa\beta}.
$$


The second identity gives


$$
\boxed{
k=\min\{r,f+v_p(1+\Omega_\beta)\}.
}
\tag{7.8}
$$



If the chosen $\Omega$ is not a unit, then $v_p(1+\Omega)=0$ and there is no excess. Thus positive excess necessarily comes from a genuine unit resonance.

## 7.4 What is sharper, and what remains open

The new theorem supplies more than another description of $\Delta_j$:

* excess is impossible unless the upper bound in the old chain is **exactly saturated**;
* the force valuation must equal the moment/contact overlap valuation;
* positive-force excess forces the precise equality $\mu+e=f$;
* several unit-force cases now have their full depth determined;
* on the surviving locus, the excess is exactly a paid unit-cancellation depth.

It does **not** prove a uniform bound for


$$
v_p(1+\Omega_\gamma),\quad
v_p(1+\Omega_\alpha),\quad
v_p(1+\Omega_\beta).
$$


Those quantities involve the actual complete force. They cannot be bounded by replacing the force with a homogeneous reference.

A sharpened sufficient follow-on lemma is therefore:

> **Saturated affine-resonance lemma.** On an infinite original endpoint subsequence, prove
> 

$$
> 2\log\mathcal I_n+\log(\mathcal Z_0\mathcal Z_3)=o(n\log n),
>
$$


> and, only over the saturated primes and the actual charts above,
> 

$$
> \sum_{j=0,3}\sum_{p>N}
> \min\!\left\{
> (v_p(\widehat R_j)-v_p(F))_+,\,
> v_p(1+\Omega_{j,p})
> \right\}\log p
> =o(n\log n).
> \tag{7.9}
>
$$


> Primes with no admissible excess chart contribute zero.

Equations (7.3)–(7.8) then give


$$
\log(\Delta_0\Delta_3)=o(n\log n).
$$



This is a narrower outstanding arithmetic target than an unrestricted affine-depth sum. It is still an unproved lemma.

---

# 8. Receipts, filters, row contents, and the final endpoint pair

## 8.1 Accepted alignment receipts

The two completed alignment calculations are now retained as finite results:


$$
\boxed{
\gcd(F,M)=128,\quad \mathcal I_{3375}=1,
}
$$




$$
\boxed{
\gcd(F,M)=8,\quad \mathcal I_{11025}=1.
}
$$



A3 turn 12’s description of the $11025$ calculation as unevaluated is superseded by the supplied completion. Its old specification is not a request to run it again.

At $3375$, the accepted filters imply


$$
\Delta_0=\Delta_3=\mathcal G=1.
$$


At $11025$, the alignment receipt alone does **not** supply complete-force, contact, endpoint-content, primitive-denominator, or whole-error evaluations.

Neither receipt proves an infinite alignment bound.

## 8.2 Source, collision, filter, and row depth remain distinct

The new saturation theorem concerns the canonical scalar/reference gcds. It does not change:

* source-content removal;
* complete collision depth;
* defect-support stripping;
* removal of the full collision depth from each reference before the exclusive gcd;
* the actual primitive contact-row normalization;
* the later two-entry reconstructed row contents.

In particular, $\eta_j$, $\mathcal Z_j$, collision depth, and final row content are different quantities.

The accepted $3375$ reconstructed row contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$


They are not replaced by the contact-coordinate content $\eta_j$.

## 8.3 Complete endpoint producer and all-prime normalization

The original endpoint force remains


$$
F_k=(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3}
$$


through the original cutoff $2n+2$, including the complete terminal return.

Both corrected columns remain


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w.
$$


The reconstructed second column retains its exterior $+1$:


$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$



The least clearer is still over all eight reconstructed entries, followed by the actual two-entry row-content divisions.

For the retained reduced weight $\lambda=a/k_{\rm wt}$, the final primitive pair remains


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
}
$$




$$
\boxed{
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
$$


Every prime remains in these final gcds.

The whole same-index evaluated error is still


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
$$


The five accepted original $3375$ whole forms remain nonzero and have absolute value greater than $1$. No new structural identity changes those evaluations.

---

# 9. The remaining binary target in its narrowed form

There are now two complementary original-source approaches.

### A. A low observation can exclude an index without controlling its norm

Theorem 5.1 asks for a nonzero digit in the paid half-length factorial observation. If such a digit is proved uniformly or on a specified infinite original subsequence, the actual primitive whole error diverges there.

This approach bypasses—not solves—the deep-norm branch.

### B. If the low observation vanishes, compare two actual observations

The norm is


$$
\mathcal U=\sum_{j=0}^{M}!j\,\theta_j,
$$


with exact valuation (4.4), while the exponential contraction is the factorial observation (4.5). The residual is their exact difference (4.6).

The outstanding relative theorem must control these **same-index, same-adjoint** observations. In particular, it must not:

* truncate the derangement observation using factorial payments;
* infer a bound for $\nu$ from primitiveness alone;
* replace the corrected column by a freely chosen lattice vector;
* replace the complete residual by a selected source term.

At a target gap $k$, the exact complete condition remains


$$
\delta_2\ge k
\iff
E+2^BL\equiv0\pmod{2^{a+\nu+k}}.
$$


If $a+\nu+k>B$, the logarithmic matching remains compulsory.

Even a favorable binary result must still satisfy the unchanged all-prime budget


$$
\log|q_n\epsilon_n|
=
(\kappa_{\rm rate}-\beta)n
-\min(\delta_2,C_n)\log2
+\sum_{p\ne2,3}v_p(q_n)\log p
+o(n).
$$


The nonnegative other-prime contribution cannot be discarded.

---

# 10. Proof ledger and arithmetic status

| Statement | Status |
|---|---|
| Original source is $m![z^m]F/(1-z)$ | **Verified from the complete excerpt and recurrence** |
| A4 turn 16’s $e^zF$ identification | **Erroneous historical label; explicitly corrected** |
| $B_{\rm new}$ for the actual source | **Proof verified** |
| Refined guard $B_*$ for the actual source | **Proof verified** |
| Actual first-column content $a=O(\log n)$ | **Closed common theorem, reused** |
| A5 complete factorial moment identity | **Independently verified** |
| Integer scalar $c_n$, its sign and exact depth | **Independently verified** |
| Complete residual and actual $4b!$-division | **Verified as whole identities** |
| A5 nonresonance theorem | **Valid with explicit hypotheses** |
| Nonresonant primitive-error divergence | **Deduction using the retained whole-error theorem** |
| Complete derangement observation of the actual norm | **New exact identity** |
| Norm-independent half-length exclusion certificate | **New conditional theorem** |
| Uniform nonvanishing of that certificate | Open |
| Uniform original forced-norm bound | Open |
| A3 fixed-seed determinant | **Independently verified** |
| Third-force identity, $\eta_j$, local ideal equality | **Independently verified** |
| $\mathcal Z_j\mid\mathcal K_j\mid\mathcal J_j\mid\mathcal I_n\mathcal Z_j$ | **Proof verified** |
| $\mathcal W^{\rm ref}\mid\mathcal G$ | **Valid consequence of retained divisibilities** |
| Full-depth saturation necessity $k>f\Rightarrow f=a+\zeta,\ e=\zeta$ | **New theorem** |
| Explicit saturated affine unit charts | **New exact full-depth formulas** |
| Uniform/subfactorial bound for their resonance depths | Open |
| Alignment gcds $128$ and $8$ | **Accepted finite results only** |
| Favorable infinite sequence of whole primitive errors | Not established |
| Irrationality or rationality of $e+\pi$ | Unresolved |

## Bounded exact arithmetic

**No new bounded computation is needed to establish the results proved in this report.**

In particular, none of the following is requested:

* either completed alignment calculation;
* the accepted original producer or five complete forms;
* the accepted binary or $29$-adic calculations;
* the optional $b=9$, high-precision logarithmic zero.

The new prefix theorem is an unevaluated mathematical certificate, not a claimed receipt or an instruction to regenerate an original producer. Its exact verification inputs, if already-available original data are used in future work, would be


$$
n,b,a,x_0,\quad
w=A^{-T}\mathcal R^Tx_0,\quad
\theta_j=w^T\mathbf a_j,
$$


together with


$$
S=a+d+1,\qquad
v_2((J+1)!/b!)\ge S+2
$$


unless $J=M$. The verifiable output would be the residue


$$
P_J\bmod 2^{S+2}
$$


and, if nonzero, its first nonzero binary digit. Theorem 5.1 then supplies the denominator conclusion. No such residue is asserted here.

---

# Conclusion

The source correction is now explicit and complete: the logarithmic source is $F/(1-z)$, and both audited guards survive for that original source. A5’s factorial alignment and residual decomposition are correct, including the integer scalar, its exact binary depth, the complete summation ranges, and the physical terminal.

The new binary advance is a sharper separation of the two actual observations:


$$
\boxed{
\text{exponential contraction: factorial weights;}
\qquad
\text{primitive norm: complete derangement weights.}
}
$$


This explains exactly why paid exponential truncation does not automatically bound the norm. It also yields a half-length, norm-independent nonzero-residue certificate that would exclude an original index even in the deep-norm regime.

The new endpoint advance is the full-depth saturation theorem:


$$
\boxed{
v_p(\Delta_j)>v_p(F)
\ \Longrightarrow\
v_p(F)=v_p(\mathcal I_n)+v_p(\mathcal Z_j),
\quad
v_p(\mathcal E_j)=v_p(\mathcal Z_j).
}
$$


Off this locus, the whole affine depth is bounded by the existing alignment/contact cost. On it, the remaining depth is an explicit unit resonance involving the actual complete force and factorial scalar—not an unidentified or support-stripped remainder.

The exact bottlenecks are therefore:

1. prove a nonzero paid exponential observation, or control the actual complete derangement norm observation and its relative cancellation;
2. bound the saturated endpoint unit-resonance depths on an infinite original family;
3. retain and control every prime in the actual final denominator;
4. compare that denominator with the whole nonzero same-index error.

These obligations remain open. **No unconditional proof or disproof of the irrationality of $e+\pi$ has been obtained.**
