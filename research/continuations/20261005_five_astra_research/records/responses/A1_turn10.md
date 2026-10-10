> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 result: the vanishing of $u\bmod3$ has an exact uniform domain

I obtain two uniform simplifications of the Pascal certificate:


$$
\boxed{u\equiv0\pmod3\quad\Longleftrightarrow\quad 3\mid M}
\qquad(M\ge1),
$$


and


$$
\boxed{X\equiv2+3M\pmod9.}
$$


Thus the $n=65$ vanishing is not accidental: $M=21$ lies in precisely the uniform vanishing class.

I also reduce $R/3\bmod9$ to a **fixed-size rational-polynomial evaluation**, independent of the length of the Pascal sums. On $3\mid M$, this gives a bounded residue rule for the locally normalized polynomial modulo $9$. Its input can be restricted to $M\bmod243$; no higher digits enter this rule.

This does **not yet determine the polynomial modulo $27$**. I prove below that on the entire class $3\mid j$, all lower factorial terms vanish modulo $27$, so the remaining polynomial obstruction is exactly one scalar:


$$
3\eta_{\rm last}\pmod{27}.
$$



The independent audit of A4’s cofactor assertion passes, conditional on the stated actual-lift and endpoint-projection identifications. I give a determinant identity proving the independence from the last scalar, including when that scalar is zero.

---

# 1. Congruences needed for the Pascal sums

Write


$$
B(q,D)=\binom{q+D}{D},\qquad
\tau_D=(-1)^{M-D}\binom MD.
$$


All congruences below concern integers or elements of $\mathbb Z_3$.

The established moment formulas modulo $9$, inserted into the exact formula for $e_s$, give


$$
\boxed{
\begin{aligned}
e_{3t}&\equiv3,\\
e_{3t+1}&\equiv2+3t(t+1),\\
e_{3t+2}&\equiv1+3t+6t(t+1)
\end{aligned}\pmod9.}
\tag{1}
$$


For example,


$$
e_{3t+1}
=4b_{3t+1}+4(3t+2)b_{3t+2}
 +(3t+2)(3t+3)b_{3t+3}.
$$


Using the supplied $b$-residues, its three contributions reduce to


$$
0,\qquad 3t+5+3t(t+1),\qquad6(t+1),
$$


whose sum is the middle formula in (1). The last branch follows similarly:


$$
4b_{3t+2}+4(3t+3)b_{3t+3}
\equiv7+6t(t+1)+3(t+1).
$$



The classical block-of-three factorial congruence is


$$
\binom{3a}{3b}\equiv\binom ab\pmod9.
\tag{2}
$$


One direct verification separates the multiples of $3$ in the factorials. The product of the two units in block $r$ satisfies


$$
(3r+1)(3r+2)\equiv2\pmod9.
$$


The unit-factor quotient therefore equals $1\bmod9$. This argument remains valid when the binomial coefficient is divisible by $3$.

Taking the adjacent numerator factors in (2) gives


$$
\boxed{
\begin{aligned}
\binom{3(q+D)}{3D}&\equiv B(q,D),\\
\binom{3(q+D)+1}{3D}&\equiv(1+3D)B(q,D),\\
\binom{3(q+D)+2}{3D}&\equiv B(q,D)
\end{aligned}\pmod9.}
\tag{3}
$$


For the second line the extra quotient is


$$
\frac{3(q+D)+1}{3q+1}\equiv1+3D.
$$


For the third line the two extra quotients multiply to


$$
(1+3D)(1+6D)\equiv1\pmod9.
$$


All denominators used here are explicit $3$-adic units.

---

# 2. Exact finite differences determine every entry of $u\bmod3$

Define


$$
T_h(q)=\sum_{D=0}^M\tau_D(D)_h B(q,D),
$$


where $(D)_h=D(D-1)\cdots(D-h+1)$.

The exact finite-difference identity is


$$
\boxed{T_h(q)=(M)_h\binom{q+h}{M}.}
\tag{4}
$$


Indeed,


$$
(D)_h\binom MD=(M)_h\binom{M-h}{D-h},
$$


and the remaining sum is the $(M-h)$-th forward difference of
$\binom{q+D}{q}$, evaluated at $D=h$.

In particular, for $0\le q<M$,


$$
T_0(q)=0,\qquad
T_1(q)=M\binom{q+1}{M},\qquad
T_2(q)=M(M-1)\binom{q+2}{M}.
\tag{5}
$$



Recall that


$$
3u_i=\sum_{D=0}^M
\tau_D\binom{i+3D}{i}e_{i+3D}.
$$


Substitute $i=3q+r$, then use (1) and (3).

For $r=0$, the sum is $3T_0(q)\bmod9$. Thus


$$
u_{3q}\equiv0\pmod3.
$$



For $r=1$, the summand multiplier modulo $9$ is


$$
(1+3D)\bigl(2+3(q+D)(q+D+1)\bigr).
$$


After removing the constant-in-$D$ term, which contracts with $T_0(q)=0$, this gives


$$
u_{3q+1}\equiv T_2(q)+(2q+4)T_1(q)\pmod3.
$$



For $r=2$, the same calculation gives


$$
u_{3q+2}\equiv2T_2(q)+(4q+5)T_1(q)\pmod3.
$$



Consequently,


$$
\boxed{
\begin{aligned}
u_{3q}&=0,\\
u_{3q+1}&=T_2(q)+(2q+4)T_1(q),\\
u_{3q+2}&=2T_2(q)+(4q+5)T_1(q)
\end{aligned}\pmod3.}
\tag{6}
$$



This is not a growing-sum prescription. Only the last two block rows can be nonzero:

- for $q<M-2$, both $T_1(q)$ and $T_2(q)$ vanish exactly;
- for $q=M-2$,
  

$$
T_1=0,\qquad T_2=M(M-1);
$$


- for $q=M-1$,
  

$$
T_1=M,\qquad T_2=M(M-1)(M+1).
$$



The last-row residues are therefore


$$
\boxed{
u_{3M-2}\equiv M(M+1)^2,\qquad
u_{3M-1}\equiv M(2M^2+4M-1)\pmod3.}
\tag{7}
$$



### Exact vanishing domain

If $3\mid M$, every expression in (6) vanishes.

Conversely:

- if $M\equiv1\pmod3$, then $u_{3M-2}\equiv1$;
- if $M\equiv2\pmod3$, then $M\ge2$, and the $q=M-2,\ r=1$ entry equals $M(M-1)\equiv2$.

Thus


$$
\boxed{u\equiv0\pmod3\iff3\mid M.}
\tag{8}
$$



For the regular family,


$$
M=\frac{4^j-1}{3},
$$


the condition $3\mid M$ is equivalent to $3\mid j$. This follows from the order of $4$ modulo $9$, or from


$$
v_3(4^j-1)=1+v_3(j).
$$



In particular, $u=0\bmod3$ at $M=21$ follows from an infinite theorem, independently of its finite receipt.

---

# 3. The mixed quadratic sum collapses completely

Let


$$
I_{ab}=\sum_{D,E=0}^M
\tau_D\tau_E D^aE^b\binom{D+E}{D}.
$$


The basic values needed here are


$$
I_{00}=1,\quad I_{10}=I_{01}=M,\quad
I_{20}=I_{02}=M^2,\quad I_{11}=2M^2.
\tag{9}
$$



For the first five, use


$$
\sum_E\tau_E\binom{D+E}{D}=\binom DM,
$$


which vanishes for $D<M$ and equals $1$ for $D=M$.

For $I_{11}$, factor $B_{M+1}=PP^T$, where $P_{Da}=\binom Da$. Then


$$
P^T\tau=e_M,
$$


whereas $P^T\operatorname{diag}(D)\tau$ has exactly two nonzero coordinates:


$$
M\quad\text{at }a=M-1,\qquad M\quad\text{at }a=M.
$$


Its squared norm is $2M^2$.

By (1) and (3), the summand multiplier in $X$ is


$$
2+3\bigl((D+E)^2+(D+E)+2D\bigr)\pmod9.
$$


Therefore


$$
\begin{aligned}
X
&\equiv2I_{00}
 +3(I_{20}+2I_{11}+I_{02}+3I_{10}+I_{01})\\
&=2+3(6M^2+4M)\\
&\equiv2+3M\pmod9.
\end{aligned}
$$


Hence


$$
\boxed{X\equiv2+3M\pmod9,}
\tag{10}
$$


and specifically $X\equiv2\pmod9$ throughout $3\mid j$.

---

# 4. A fixed-size residue rule for $R/3\bmod9$

The following supplies an analytic reduction to bounded data, rather than another Pascal sum whose size grows with $M$.

Define the fixed rational polynomial


$$
f(s)=\sum_{\ell=0}^{8}
(-2)^{-\ell}\binom{s}{\ell}(s+1)\cdots(s+\ell).
$$


Its degree is at most $16$. Define


$$
F(t)=4f(3t)-8(3t+1)f(3t+1)
 +4(3t+1)(3t+2)f(3t+2),
$$


and


$$
\mathcal E(t)=\frac{(1-9t)F(t)}3.
\tag{11}
$$


This polynomial has degree at most $19$.

The nine-term factorial truncation and


$$
(-2)^{3t}=(-8)^t\equiv1-9t\pmod{27}
$$


give, for every integer $t\ge0$,


$$
\boxed{\mathcal E(t)\equiv e_{3t}/3\pmod9.}
\tag{12}
$$


The division by $3$ is legitimate: the numerator in (11) agrees with $e_{3t}$ modulo $27$, and $e_{3t}$ is divisible by $3$.

Write


$$
\mathcal E(t)=\sum_{h=0}^{19}\epsilon_ht^h.
$$


The denominators of the coefficients $\epsilon_h$ have $3$-depth at most $3$: the only factorial denominators are $\ell!$, with $\ell\le8$, followed by the displayed division by $3$.

For $a,t\ge0$, define the fixed polynomials


$$
C_{a,t}(M)=
\sum_{h=t}^{a}
\left\{\begin{matrix}a\\h\end{matrix}\right\}
(M)_h\binom ht,
\tag{13}
$$


using Stirling numbers of the second kind. Set


$$
\mathcal I_{ab}(M)=
\sum_{t=0}^{\min(a,b)}C_{a,t}(M)C_{b,t}(M).
\tag{14}
$$


For $M\ge19$, these equal the exact contractions $I_{ab}$ whenever $a+b\le19$.

To verify this, the generating identity is


$$
\sum_{k=0}^M
\left(\sum_D\tau_DD^a\binom Dk\right)z^k
=
\bigl((1+z)\partial_z\bigr)^a z^M.
$$


Expanding powers of the differential operator gives (13) as the coefficient at $z^{M-t}$. Taking the Pascal Gram product proves (14).

Finally define the single fixed polynomial


$$
\boxed{
\mathcal H(M)=
\sum_{h=0}^{19}\epsilon_h
\sum_{a=0}^{h}\binom ha\,
\mathcal I_{a,h-a}(M).}
\tag{15}
$$


Equations (2), (12), and (14) prove


$$
\boxed{R/3\equiv\mathcal H(M)\pmod9\qquad(M\ge19).}
\tag{16}
$$



All ranges in (11)–(15) are bounded by $19$, independent of $M$.

Moreover, $\mathcal H$ has degree at most $19$, and its coefficient denominators have $3$-depth at most $3$. Therefore


$$
\boxed{\mathcal H(M+243)\equiv\mathcal H(M)\pmod9.}
\tag{17}
$$


Indeed, the difference of each integer monomial under $M\mapsto M+243$ is divisible by $3^5$, and division by at most $3^3$ leaves divisibility by $9$.

This is a true finite residue rule. The bound $243$ is not claimed minimal.

### Consequence on the specified infinite regular class

For


$$
n=4^j+1,\qquad j\ge1,\qquad3\mid j,
$$


we have $M\ge21$ and $u=0\bmod3$. Thus


$$
\boxed{
c/3\equiv\mathcal H(M),\qquad
\xi_{\rm last}\equiv2,\qquad
3\eta_{\rm last}\equiv2\mathcal H(M)^{-1}\pmod9.}
\tag{18}
$$


The inverse exists because the established first lift gives
$\mathcal H(M)\equiv1\pmod3$.

Consequently the locally normalized primitive ray $Q^{\rm loc}=3P_n$ satisfies


$$
\boxed{
Q^{\rm loc}(y)\equiv
(y+1)(y-1)^{N-1}
\left(3(y-1)-2N\mathcal H(M)^{-1}\right)\pmod9.}
\tag{19}
$$


Its leading normalization is exactly $3$. The actual primitive polynomial remains


$$
Q_n=(L_n/3)Q^{\rm loc},
$$


with the global $3$-adic unit $L_n/3$ retained.

Thus $M\bmod243$ suffices for this digit law. The current derivation does not establish that $M\bmod9$ alone suffices.

---

# 5. A uniform modulo-$27$ truncation: no lower factorial terms survive

There is a useful strengthening of the polynomial truncation on the same class $3\mid j$.

Put $L=N-1=3M$. Since $3\mid M$,


$$
v_3(L)\ge2,\qquad v_3(L-3)\ge1.
$$


For every $d\le L-4$, the factorial ratio $N!/d!$ contains both $L$ and $L-3$, so has depth at least $3$.

The only additional indices are


$$
d=L-3,\ L-2,\ L-1.
$$


Their factorial ratios have depth at least $2$. The established first radical projection has support only at $d=3D$. Therefore the projection residues at $L-2,L-1$ vanish. At $L-3=3(M-1)$, its coefficient is a unit multiple of


$$
z_{M-1}=\binom M{M-1}=M\equiv0\pmod3.
$$


These three terms also vanish modulo $27$.

The constant term has greater depth by the established endpoint theorem. Hence, uniformly,


$$
\boxed{
Q^{\rm loc}(y)\equiv
(y+1)(y-1)^{N-1}
\left(3(y-1)-N\Theta_M\right)\pmod{27},
\quad
\Theta_M=3\eta_{\rm last}\pmod{27}.}
\tag{20}
$$



This proves the uniform disappearance of the lower terms; it does **not** evaluate $\Theta_M\bmod27$. That distinction is essential. Formula (19) is evaluated by a bounded residue rule, whereas (20) still has an unresolved scalar.

The next obstruction is concrete: upgrading $R/3$ requires the block-of-three binomial quotient modulo $27$, not merely (2). It cannot be replaced by Lucas reduction:


$$
\binom63=20\not\equiv2=\binom21\pmod{27}.
$$



---

# 6. Independent audit of A4’s cofactor-depth assertion

Here is an algebraic proof that avoids relying on cancellation of inverse poles.

Assume the actual first saturation is integrally congruent to


$$
\operatorname{diag}(E_1,3W),
$$


where $E_1$ is a unit block and $W$ is $8\times8$. Assume the actual second saturation is integrally congruent to


$$
\operatorname{diag}(J,3\tau),
$$


where $J$ is $7\times7$ and a unit block. The resulting congruent form for $S$ is


$$
D=\operatorname{diag}(E_1,3J,9\tau).
$$


Let the correspondingly transformed distinguished endpoint vector be


$$
v=(a,b,\gamma),
$$


where $\gamma\in\mathbb Z_3^\times$. This last condition is precisely the nonzero endpoint projection, not a consequence of rank alone.

Write


$$
U=\det E_1\det J\in\mathbb Z_3^\times.
$$


An exact adjugate calculation gives


$$
\begin{aligned}
v^T\operatorname{adj}(D)v
={}&3^7U\gamma^2\\
&+3^8\tau\,\det E_1\,
 b^T\operatorname{adj}(J)b\\
&+3^9\tau\,\det J\,
 a^T\operatorname{adj}(E_1)a.
\end{aligned}
\tag{21}
$$


Therefore


$$
3^{-7}v^T\operatorname{adj}(D)v
\equiv U\gamma^2\not\equiv0\pmod3.
$$


Integral unimodular congruence changes the corresponding cofactor contraction only by a square unit. Consequently,


$$
\boxed{v_3(\operatorname{adj}(S)_{00})=7}
\tag{22}
$$


under A4’s stated actual-lift identifications.

Importantly, (21) remains valid at $\tau=0$. The proof is an identity of cofactors, not an argument that multiplies two separately singular expressions.

**Audit verdict:** A4’s claimed independence from the last scalar depth is correct. Its numerical application remains conditional on the actual saturation and endpoint-vector identifications; the supplied finite receipt asserts those identifications at $n=65$. This audit does not extend them to infinitely many indices.

---

# 7. Actual normalization and whole evaluated error

None of the polynomial digit results changes the final normalization. For the complete rational-arctangent pair, retain


$$
A=t\det K-z^T\operatorname{adj}(K)z,\qquad
B=\ell Q_n(-1)\det K,
$$




$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


For the regular family $n=4^j+1$, the matrix size is


$$
k=(n+1)/2.
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete}.}
$$


All factorial terms, rational arctangent terms, and both periods remain included.

The inherited regular-family nonvanishing and distinct-center results, rather than the new polynomial calculations, supply $B\ne0$ and nonzero whole errors except possibly at one index. No decay of this whole primitive error is proved here.

## (1) New result and proof status

**Proved:**

- Exact uniform domain $u=0\bmod3\iff3\mid M$.
- Complete collapse $X=2+3M\bmod9$.
- A fixed-size rational-polynomial rule for $R/3\bmod9$, depending on at most $M\bmod243$.
- An evaluated bounded residue rule for $Q^{\rm loc}\bmod9$ on every regular index $3\mid j$.
- Uniform removal of all lower factorial terms modulo $27$ on that class.
- A4’s cofactor-depth independence, by an adjugate identity with an explicit nonzero unit.

**Not proved:** an evaluated infinite-class law for $Q^{\rm loc}\bmod27$ or modulo $81$, or irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

At the polynomial level, evaluate


$$
\Theta_M=3\eta_{\rm last}\pmod{27}.
$$


The lower factorial terms are now removed uniformly, so this is genuinely the only remaining scalar in (20). Its computation requires the next block-of-three factorial/carry correction and the corresponding higher moment contraction.

At the complete-center level, infinite actual saturation and endpoint projection remain separate obligations. A polynomial digit law cannot replace the final gcd or the whole evaluated error.

## (3) Bounded computation request

**Input:** only the fixed rational polynomials (11)–(15), with summation limits at most $19$.

**Requested verifiable output:**

1. The expanded rational polynomial $\mathcal H(M)$, with a common denominator separated into its $3$-power and unit parts.
2. Its exact reduction on $M=3T$ modulo $9$, simplifying the dependence on $T$ as far as possible.
3. An exact check
   

$$
\mathcal H(21)\equiv4\pmod9.
$$



This is a bounded symbolic contraction, not a degree table or a growing Pascal computation. Its purpose is to sharpen the proved modulus-$243$ input bound and determine whether the rule collapses to $M\bmod9$ or a constant on a smaller infinite regular class.
