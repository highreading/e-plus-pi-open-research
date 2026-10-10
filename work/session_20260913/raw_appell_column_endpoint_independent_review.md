> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit: all inverse-column hooks and the primitive endpoint bridge

Date: 2026-09-13. Reviewer: audit_results. **FULL PASS after two source
corrections recorded below.** Reviewed raw_appell_all_cofactors_and_endpoint_units.md
in full. The source now incorporates the corrections.
No canonical degree or prime scan was used. The rate comparison below is
certified by elementary rational inequalities.

## 1. Corrections found and repaired

1. In Section 3 the displayed binomial vector is the high-coefficient vector
   of $t^{2n}(t-1)^nV(1)$, corresponding to $V(t)=V(1)t^n$.
   The original explanatory sentence omitted the second factor $t^n$.
   Its displayed coefficient formula and monomial conclusion were correct.

2. The exact Section 5 endpoint identity has **no** factor $(-1)^n$:
   

$$
\widehat P_e(1)=\sum_{r=0}^n V_rD_{n,r},\qquad
    \widehat P_e(1)\equiv V(1)\pmod{2n}.
$$


   In the fixed original cofactor orientation the relation is
   $V_r=(-1)^{n+r}c_r\delta_r/h$, not
   $(-1)^rc_r\delta_r/h$. The root's original unit conclusion and all
   denominator inequalities survive unchanged. An independent integral
   derivation in Section 6 below settles the sign without relying on a
   cofactor orientation convention.

The source also now notes that the prime-two endpoint unit needs no
factorial-versus-logarithm threshold.

## 2. All cofactors: partitions, signs, and hooks

Let $C_j$ be the minor obtained by deleting row zero and column $j$
of $A=(a_{n+i-j})_{0\le i,j\le n}$.
After transposition its row indices come from
$k_l=l-1$ for $l\le j$ and $k_l=l$ for $l>j$.
Its entry is $h_{n+i-k_l}=h_{\lambda_l-l+i}$, so this is the ordinary
Jacobi--Trudi determinant for


$$
\lambda_j=((n+1)^j,n^{n-j}),\qquad |\lambda_j|=n^2+j.
$$


The inverse column uses cofactor $(0,j)$, hence the sign is $(-1)^j$.
No row permutation changes that sign.

For an independent hook calculation, the degree set
$\{\lambda_l+n-l:1\le l\le n\}$ is
$\{n,\ldots,2n\}\setminus\{2n-j\}$.
The factorial-over-Vandermonde hook formula gives


$$
H_j/H_D=\frac{j!(n-j)!}{(2n-j)!},\qquad
 r_j=H_D/H_j=\frac{(2n-j)!}{j!(n-j)!}.
$$


This includes both endpoints $j=0,n$. Each $r_j$ is an integer and
$r_n=1$.

The universal augmented-Schur theorem was independently checked in
raw_appell_hook_congruence_independent_review.md, including its
complete-function power-sum convention. Applying it to these exact
partitions gives


$$
M_j(x)\equiv x^{n^2+j},\quad
 M_D(x)\equiv x^{n(n+1)}\pmod{2n},\qquad M_j,M_D\in\mathbb Z[x].
$$


At one these integers are nonzero and prime to $2n$. Thus


$$
v_j=(-1)^jr_jM_j(1)/M_D(1)
$$


is valid for every index and every degree. Each normalized quotient is
one modulo $2n$ in every localization at $p\mid2n$, with full
depth $v_p(2n)$.

In particular $v_n\ne0$. The incidental statement about the even
two-function accessory degree is valid directly: for its monic degree-$n$
numerator $C$, the term $z^2Cv$ is uniquely highest in
$D(Cv'-C'v)+(D+2nz)Cv$, with coefficient $v_n$ at degree $2n+2$.
Its established origin factor is $z^{2n}$, leaving degree exactly two.
No further property of that accessory equation is needed here.

## 3. The primitive integral vector is really primitive

The existing dual construction gives primitive
$V\in\mathbb Z[t]$, $W=t^n(t-1)^nV$, and the exact divided coefficients


$$
b_j=\frac{U_j}{(n+j)!}
 =w_{2n+j}+
 \sum_{\substack{h\ge1\\j+2h\le n}}
 (-1)^h\binom{n+h-1}{h}
 \frac{(n+j+2h)!}{(n+j)!}w_{2n+j+2h}.
$$


The map from the $n+1$ coefficients of $V$ to
$(w_{2n},\ldots,w_{3n})$ is triangular with diagonal one over the
integers. So is the displayed map to $b$. Both have integral inverses.
This proves $\gcd(b_0,\ldots,b_n)=1$ globally, rather than merely
showing one rational scaling can be chosen primitive.

For an off-diagonal term use


$$
\binom{n+h-1}{h}=\frac nh\binom{n+h-1}{h-1}.
$$


The product of $2h$ consecutive integers appearing in the factorial
ratio is divisible by $(2h)!$, hence by $2h$. Its product with
$n/h$ is an integer multiple of $2n$. Therefore the transformation
to $b$ is the identity modulo $2n$. This proof includes every
allowed $h,j$; when no such $h$ exists the assertion is empty.

The reversed dual identity is
$z^nU(1/z)=n!V(1)v(z)$. Its $j$-th unreversed coordinate therefore gives


$$
b_j=(-1)^{n-j}\binom nj V(1)
             \frac{M_{n-j}(1)}{M_D(1)}.
$$


For $p\mid2n$ this has exact valuation


$$
v_p(b_j)=v_p(V(1))+v_p\binom nj.
$$


Taking the minimum and using either endpoint binomial coefficient proves
$v_p(V(1))=0$. The already reviewed corner quotient gives the same
unit statement for $V_{\rm lead}$. There is no unaccounted common
primitive scale.

## 4. Global monomial congruence and factorial content

The preceding coordinate equality, followed by the integral triangular
inverse, proves at the full depth of each prime power dividing $2n$
that the coefficient vector of $V$ equals that of $V(1)t^n$.
Combining these prime powers yields the integer-polynomial congruence


$$
\boxed{V(t)\equiv V(1)t^n\pmod{2n},\qquad
        \gcd(V(1),2n)=\gcd(V_{\rm lead},2n)=1.}
$$


This conclusion does not assert anything modulo a larger prime power.

For $p\mid2n$,
$U_{n-j}=n!V(1)(-1)^jr_jM_j(1)/M_D(1)$.
The integers $r_j$ all have nonnegative valuation and $r_n=1$.
Thus


$$
v_p(\operatorname{cont}U)=v_p(n!).
$$


Multiplication by the primitive integer polynomial $(1+t^2)^n$
preserves content. If $S=(1+t^2)^nU$, then the exact actual identity is


$$
\widehat Q(z)=z^{2n}S^{(n)}(1/z)/n!.
$$


The contribution from $S_k$ is $\binom kn S_k$, an integer multiplier.
Consequently $\operatorname{cont}U\mid\operatorname{cont}\widehat Q$
globally. In particular,


$$
v_p(Z)\ge v_p(\operatorname{cont}\widehat Q)\ge v_p(n!)
 \quad(p\mid2n).
$$


This argument uses the correct divided derivative, not the false
principle that ordinary differentiation preserves primitive content.

## 5. Independent check of the cofactor orientation

The already reviewed original primitive transport is


$$
w_{n+t}=\frac{(-1)^t}{h}
       \sum_r\binom n{t-r}c_r\delta_r.
$$


Summing in $t=r+s$ gives


$$
W(t)=\frac{t^n(1-t)^n}{h}\sum_r(-1)^rc_r\delta_rt^r.
$$


Since $W=t^n(t-1)^nV$, this proves exactly


$$
V_r=(-1)^{n+r}c_r\delta_r/h.
$$


The existing border formula
$h\widehat P_e(1)=\sum_r(-1)^{n+r}c_r\delta_rD_{n,r}$
therefore becomes $\widehat P_e(1)=\sum_rV_rD_{n,r}$.
Both the cofactor and integral routes agree after the correction.

## 6. Independent direct exponential endpoint identity

Let $E_s=\sum_{j=0}^s1/j!$. The integral representation
$E_s=(1/s!)\int_0^\infty e^{-t}(1+t)^s\,dt$ gives


$$
\widehat P_e(1)
  =\frac1{n!}\sum_{k=n}^{3n}k!w_kE_{k-n}
  =\frac1{n!}\int_0^\infty e^{-t}W^{(n)}(1+t)\,dt.
$$


Each integration by parts has zero boundary term: at zero the relevant
derivative of $W$ vanishes at one; at infinity it is a polynomial
times an exponential. Because the derivative of the exponential is
negative, the integration by parts introduces a plus sign each time.
Therefore


$$
\widehat P_e(1)=\frac1{n!}\int_0^\infty
       e^{-t}t^n(1+t)^nV(1+t)\,dt
 =\sum_{r=0}^nV_r\sum_{j=0}^{n+r}\binom{n+j}{j}(n+r)_j.
$$


The last equality follows by expanding $(1+t)^{n+r}$ and reversing
the finite index. It includes every factorial in $D_{n,r}$.

Every summand of $D_{n,n}$ except its constant term contains $2n$.
The monomial congruence now proves


$$
\boxed{\widehat P_e(1)\equiv V(1)\pmod{2n}.}
$$


This endpoint is a unit at every prime dividing $2n$, despite possible
cancellation in general cofactor sums.

For the frozen $n=1$ control,
$w=(-2,3,-1)$, $V(t)=2-t$, and
$\widehat P_e(1)=-5$.
Here $D_{1,0}=3,D_{1,1}=11$, and $2\cdot3-11=-5$.
This catches the removed sign and uses no new canonical solve.

## 7. Actual reduction, threshold, and its prime-two exception

The integral numerator $\widehat P_a$ is obtained by truncating
$\widehat Q\arctan$ through degree $2n$. All rational coefficients
of that multiplier have denominators dividing
$\operatorname{lcm}(1,\ldots,2n)$. Hence


$$
v_p(\widehat P_a(1))\ge
 v_p(n!)-\lfloor\log_p(2n)\rfloor\quad(p\mid2n).
$$


If this is positive, the already proved exponential unit forces
$N=\widehat P_e(1)+4\widehat P_a(1)$ to be a $p$-unit. Since the
actual reduced denominator is exactly
$q=|Z|/\gcd(|Z|,|N|)$, it follows that


$$
v_p(q)=v_p(Z)\ge v_p(n!).
$$


At $p=2$, integrality of $\widehat P_a(1)$ already makes
$4\widehat P_a(1)$ even, so this conclusion needs no threshold.

For each fixed odd prime $p$, the threshold is eventually satisfied
and Legendre's factorial formula supplies


$$
v_p(q_n)\ge \frac{n}{p-1}-O_p(\log n)
$$


on the actual family $p\mid n$. This proves the indicated restricted
family. It is not an all-degree theorem for a fixed odd prime.

## 8. Numerical-free certificate for the degree-2310 exclusion

The required logarithm comparison can be proved with short rational
bounds, without floating-point evaluation. For $0<u<1$,


$$
\log\frac{1+u}{1-u}
   =2\sum_{k\ge0}\frac{u^{2k+1}}{2k+1}.
$$


Put $L_2=2(1/3+1/81+1/1215)=842/1215$.
The following lower bounds follow by truncation, except for the
displayed upper bound used in the fourth row:


$$
\begin{array}{c|c|c}
 &\text{rational lower bound}&\text{simpler lower bound}\\
 \log2&L_2&69/100\\
 \log3&L_2+2/5+2/375&109/100\\
 \log5&2L_2+2/9&160/100\\
 \log7&3L_2-15/112&194/100\\
 \log11&3L_2+6/19&239/100
\end{array}
$$


For the fourth row,
$\log(8/7)<2(1/15)/(1-1/225)=15/112$.
Every comparison in the table is a strict rational inequality.

Also $\phi=(1+\sqrt5)/2<13/8$. With $u=5/21$, bounding every
denominator in the logarithm's tail by three gives


$$
\log\phi<\log(13/8)
 \le 2u+\frac{2u^3}{3(1-u^2)}<49/100.
$$


For example the final rational margin is $1399/327600>0$.
Consequently


$$
\frac32\log2+\frac{\log3}{2}+\frac{\log5}{4}
        +\frac{\log7}{6}+\frac{\log11}{10}
 >\frac{7627}{3000}
 >5\log\phi+\frac{277}{3000}.
$$


These inequalities were also checked using exact rational arithmetic.

For $n$ divisible by $2310$, the established exact dyadic rate
$v_2(q_n)=n+2\lfloor(n+2)/4\rfloor$, together with Section 7
at $3,5,7,11$, proves that $q_n\rho^{5n}$ grows exponentially.
The accepted even relative-error asymptotic has a positive, nonzero
constant, so the absolute primitive forms themselves tend to infinity
along this family.

Thus the sequence over **all** even degrees cannot tend to zero.
This does not exclude other even subsequences, prove irrationality,
or bound the denominator at primes not dividing the degree.

## 9. Dependency and scope check

The argument uses only the already reviewed universal Appell theorem,
the original primitive dual identities and integral Rodrigues division,
and the actual endpoint reduction formula. It does not assume a
finite-field rank theorem, a saturation condition, a sign for an
indefinite Hankel matrix, or a conjectural bound for the weighted
cofactor content. The analytic input enters only in the final
nonshrinking consequence, after all arithmetic statements are proved.

