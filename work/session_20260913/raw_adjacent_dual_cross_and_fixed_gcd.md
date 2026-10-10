> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent simultaneous approximants and fixed-endpoint cancellation

Date: 2026-09-13. Original bounded arithmetic continuation by audit_sources.
Independent review: FULL PASS by audit_results; see raw_adjacent_dual_cross_independent_review.md.

This note concerns actual adjacent degrees, not different endpoint parameters at one degree. Retain


$$
Y_n=(Q_n,P_n,T_n)
=(\widehat Q_n,\widehat P_{e,n},\widehat P_{a,n}),\quad
Z_n=Q_n(1),\quad N_n=P_n(1)+4T_n(1),\quad
G_n=\gcd(|Z_n|,|N_n|).
$$


The new integral neighboring object is


$$
\boxed{\mathcal U_n(z)=z^{-(3n+1)}(Y_n(z)\times Y_{n+1}(z)).}
\tag{1}
$$


It is a nonzero polynomial triple of degree at most $n+1$ and is an actual next-degree high type-I approximant. If $c_n>0$ is its full coefficient content, then


$$
\boxed{
\min\{v_p(G_n),v_p(G_{n+1})\}
\le v_p(c_n)+v_p(F_{n+1}),\qquad p>3n+3.
}
\tag{2}
$$


The content $c_n$ is not assumed to be a unit. A two-integer first-error carrier below measures its exceptional prime support.

There is also an unconditional explicit determinant carrier. Let
$\Delta^0_r$ denote the determinant of the integer extremal $X_r$ with its last row $3r$ removed. The note proves $\Delta^0_r\ne0$ in every degree. It defines a positive integer $A_n^{\rm err}$, linear-cofactor error data with denominators cleared only at primes at most $3n+1$, and proves


$$
\boxed{
(A_n^{\rm err})_{>3n+3}\mid|\Delta^0_{n+1}|_{>3n+3},
}
\tag{3}
$$




$$
\boxed{
\gcd(G_n,G_{n+1})_{>3n+3}
\mid\bigl(|\Delta^0_{n+1}|A_n^{\rm err}\bigr)_{>3n+3}
\mid\bigl(|\Delta^0_{n+1}|_{>3n+3}\bigr)^2.
}
\tag{4}
$$


These are full prime-power statements, with the explicit normalizations below. They supply an actual contiguous restriction. The crude height of the carrier in (4) does not yet improve the trivial single-index bound $G_n\le |Z_n|$.

## 1. Archive comparison and retained hypotheses

The inspected adjacent results are raw_adjacent_high_content_condensation.md, raw_shared_core_large_prime_saturation.md, raw_contiguous_extremal_content_inequality.md, and literature_hp_dvr_content_and_obstruction.md. They give shared-core saturation, local Schur carriers, and
$\gcd(F_n,F_{n+1})\mid D_n$ after localization, where $D_n$ is the unbordered high content. They do not identify the adjacent simultaneous cross product (1), or control its actual fixed-4 endpoint values.

The inputs used here are independently reviewed:

- $Y_n\in\mathbb Z[z]^3$, all degrees at most $2n$, with
  $Q_ne^z-P_n,\ Q_n\arctan z-T_n=O(z^{3n+1})$.
- The simultaneous denominator space at each degree is one-dimensional over $\mathbb Q$, with $Z_n\ne0$.
- The exact reduced endpoint is $-N_n/Z_n$, and its denominator has
  

$$
v_2(q_n)=\kappa_n:=n+2\lfloor(n+2)/4\rfloor.
$$


  In particular adjacent rational endpoints are distinct.
- For $p>2n$, $Y_n$ has no common nonzero algebraic root after reduction, and its coefficient vector at degree $2n$ is nonzero. These are the new dual-quadratic theorems in raw_dual_quadratic_and_endpoint_separation.md.
- $F_r$ is the positive maximal-minor content of the actual integer $X_r$, with rows $k=r,\ldots,3r$ and columns $B_j,C_j,\ 0\le j<r$. Its entries are $(k)_j$ and $k!\tau_{k-j}$, where $\tau_s=[z^s]\arctan z$.

No field-perfectness assertion beyond these proved statements is used. The prime bound $p>3n+3$ ensures that every Taylor coefficient and factorial through the next high row is a unit.

## 2. The adjacent cross product is an actual next-degree type-I triple

Put $M=3n+1$, and define full formal errors


$$
R_{e,n}=Q_ne^z-P_n,\qquad
R_{a,n}=Q_n\arctan z-T_n.
$$


Every component of $Y_n\times Y_{n+1}$ is a polynomial of degree at most $4n+2$. Writing $f=(1,e^z,\arctan z)$, the identity
$Y_r=Q_rf-(0,R_{e,r},R_{a,r})$ shows that each component of the cross product has order at least $M$. Its coefficients are integers, so division by $z^M$ introduces no denominator. Hence (1) is an integer triple of degree at most $n+1$.

The exact scalar identity is


$$
(Y_n\times Y_{n+1})\cdot f
=R_{e,n}R_{a,n+1}-R_{a,n}R_{e,n+1}.
\tag{5}
$$


The right side has order at least $M+(M+3)$. Dividing by $z^M$ gives


$$
\boxed{\mathcal U_n\cdot(1,e^z,\arctan z)=O(z^{3n+4}).}
\tag{6}
$$


This is exactly the high Taylor order for degree $n+1$. It does not assert endpoint matching for $\mathcal U_n$.

Write $\mathcal U_n=(\mathcal A_n,\mathcal B_n,\mathcal C_n)$.
At $z=1$,


$$
\boxed{
\mathcal C_n(1)-4\mathcal B_n(1)
=\mathscr D_n:=Z_nN_{n+1}-N_nZ_{n+1}.
}
\tag{7}
$$


If this integer were zero, the rational endpoints $N_n/Z_n$ and $N_{n+1}/Z_{n+1}$ would agree. Their reduced denominators have different valuations $\kappa_n<\kappa_{n+1}$, a contradiction. Thus $\mathscr D_n\ne0$, and in particular $\mathcal U_n\ne0$.

There is an immediate global determinant divisor


$$
\boxed{G_nG_{n+1}\mid|\mathscr D_n|.}
\tag{8}
$$


Both products in (7) are divisible by $G_nG_{n+1}$. Identity (7) exposes the same determinant as the endpoint mismatch of a low-degree neighboring approximant. It does not by itself make that mismatch small.

For completeness, with $\Lambda_n=Z_n(e+\pi)-N_n$, the exact signed form is


$$
\mathscr D_n=Z_{n+1}\Lambda_n-Z_n\Lambda_{n+1}.
\tag{9}
$$


Any useful analytic upper bound from (9) must control the actual complete errors and their signs; replacing them by numerical evidence is not justified.

## 3. Full-depth endpoint divisibility and the necessary content term

Fix $p>3n+3$, and put


$$
h=\min(v_p(G_n),v_p(G_{n+1})),\qquad
s=v_p(c_n),\qquad f=v_p(F_{n+1}).
$$


Modulo $p^h$, both simultaneous endpoint triples lie on the same fixed line


$$
Y_r(1)\equiv T_r(1)(0,-4,1),\qquad r=n,n+1.
$$


Therefore all three coordinates of their cross product, equivalently of $\mathcal U_n(1)$, vanish modulo $p^h$.

If $h\le s$, (2) is immediate. Otherwise divide $\mathcal U_n$ by its integer content. The resulting primitive integer triple has degree at most $n+1$, high order (6), and all endpoints zero modulo $p^{h-s}$. Over $\mathbb Z/p^{h-s}\mathbb Z$, each polynomial is divisible by $z-1$. Their divided triple has degree at most $n$, still has high order $3n+4$, and is primitive modulo $p$. Multiplication by $z-1$ preserves coefficient primitivity modulo $p$; at the origin it is a unit and therefore does not lower Taylor order.

Its $B,C$ coefficient vector is primitive as well: if those coefficients all vanished modulo $p$, the low Taylor equations would force the $A$ coefficients to vanish, since their denominators through degree $n+1$ are units. Consequently this vector is a primitive approximate kernel of $X_{n+1}$ modulo $p^{h-s}$.

Every square maximal submatrix of $X_{n+1}$ annihilates that vector modulo $p^{h-s}$. Its adjugate identity, applied to a unit coordinate of the vector, shows that its determinant is divisible by $p^{h-s}$. Thus every maximal minor has that divisibility, giving $f\ge h-s$. This proves (2), including every prime-power exponent.

This proof neither sets $c_n=1$ nor identifies it with $F_{n+1}$. Removing $c_n$ without a separate primitive-content argument would lose precisely the obstruction at issue.

## 4. An all-index nonzero deleted-row determinant

Let $\phi(k)=v_2(k!)$, and $S(r)=\sum_{j=0}^{r-1}\phi(j)$. Then


$$
\boxed{
v_2(\Delta^0_r)
=3S(r)+\sum_{k=r}^{2r-1}\phi(k).
}
\tag{10}
$$


In particular $\Delta^0_r\ne0$ for every $r\ge1$.

Here is a direct proof using the already established dyadic raw Legendre basis. Divide the rows $k=r,\ldots,3r-1$ by $k!$. For an $r$-element set $E$ of rows assigned to the exponential columns, its determinant has valuation at least


$$
S(r)-\sum_{k\in E}\phi(k),
$$


because $1/(k-j)!=(j!/k!)\binom kj$, with an integer binomial matrix. Equality holds for consecutive $E$, whose binomial determinant is 1.

For every complementary $r$-row set, the arctangent determinant has valuation at least $2S(r)$. Reverse its columns and use the moment functional
$\mathcal L(t^a)=\tau_{a+1}$. Its rows are test monomials $t^{k-r}$, all of nonnegative degree, against columns $1,t,\ldots,t^{r-1}$. Change the latter columns to monic raw Legendre polynomials. They and the inverse triangular basis change are dyadically integral; their norms have valuations $2\phi(j)$. Expansion of each row polynomial in that orthogonal basis therefore gives the bound $2S(r)$. For the consecutive complementary rows $k=r,\ldots,2r-1$, equality holds, because the coefficient matrix is triangular with unit diagonal.

The assignment


$$
E_0=\{2r,\ldots,3r-1\}
$$


attains both bounds. Every other assignment loses at least
$\phi(2r)-\phi(2r-1)=v_2(2r)>0$ in the factorial sum: an omitted top row must be replaced by a row at most $2r-1$. It therefore has strictly greater valuation. The unique least Laplace term cannot cancel. Restoring all row factorials gives (10).

The primitive cofactor convention fixes


$$
\boxed{
Q_r(0)=\frac{(3r)!}{r!}\frac{\Delta^0_r}{F_r}\ne0.
}
\tag{11}
$$


The last cofactor sign is positive because its row position is $2r$. This proves actual constant-coefficient nonvanishing without assuming a perfect Padé table.

## 5. Two linear first-error functionals

Let


$$
a_n=[z^{3n+1}]R_{e,n},\qquad
b_n=[z^{3n+1}]R_{a,n}.
\tag{12}
$$


With the original primitive vector $w_k$, their exact expressions are


$$
a_n=\frac1{n!}\sum_{k=n}^{3n}\frac{w_k}{k+1},\qquad
b_n=\frac1{n!}\sum_{k=n}^{3n}k!w_k\tau_{k+1}.
\tag{13}
$$


Put $L_n=\operatorname{lcm}(1,\ldots,3n+1)$ and define integers


$$
I_n=L_n\sum_{k=n}^{3n}\frac{w_k}{k+1},\qquad
J_n=L_n\sum_{k=n}^{3n}k!w_k\tau_{k+1},\qquad
A_n^{\rm err}=\gcd(|I_n|,|J_n|).
\tag{14}
$$


These are **linear**, not cubic, functions of the primitive cofactor vector.

The two errors in (12) cannot both vanish over $\mathbb Q$. If they did, $z^2Y_n$ would meet every next simultaneous condition at degree $2n+2$ and order $3n+4$. The next simultaneous solution space is one-dimensional, so $Y_{n+1}$ would be proportional to $z^2Y_n$. This would make their cross product zero, contradicting (7); alternatively it contradicts (11) at $r=n+1$. Hence $A_n^{\rm err}>0$.

The first coefficient of the neighboring cross product is exact:


$$
\boxed{
\mathcal U_n(0)=Q_{n+1}(0)(b_n,-b_n,a_n).
}
\tag{15}
$$


Indeed the leading error vector of $Y_n$ is $(0,a_n,b_n)z^M$, while the next error begins three degrees later. The value of $f$ at the origin is $(1,1,0)$; its cross product with $(0,a_n,b_n)$ is $(b_n,-b_n,a_n)$. This proves (15) with the sign in (1).

For $p>3n+3$, the clearer $n!L_n$ is a unit, so (15) gives


$$
\boxed{v_p(c_n)\le v_p(Q_{n+1}(0))+v_p(A_n^{\rm err}).}
\tag{16}
$$



## 6. The error carrier divides the next deleted-row determinant

Fix $p>3n+3$, and suppose $a_n,b_n$ vanish modulo $p^t$. The triple $z^2Y_n$ satisfies the next simultaneous Taylor conditions modulo $p^t$, as in §5. Its denominator polynomial is primitive modulo $p$: $Q_n$ is primitive by the reviewed content theorem, and multiplication by $z^2$ preserves that property.

Under the exact reversal and factorial identification with the left kernel of $X_{n+1}$, this yields a primitive left approximate annihilator modulo $p^t$. Its last coordinate is zero because the new denominator has zero constant coefficient. All factorial weights are units at the stated prime. Deleting that zero coordinate leaves a primitive left annihilator of the square matrix defining $\Delta^0_{n+1}$.

The square adjugate identity forces
$p^t\mid\Delta^0_{n+1}$. Since $v_p(A_n^{\rm err})=\min(v_p(a_n),v_p(b_n))$, this proves (3) at every depth.

Combining (2), (16), and the exact scalar identity (11), whose factorial ratio is a $p$-unit, gives


$$
\begin{aligned}
\min(v_p(G_n),v_p(G_{n+1}))
&\le v_p(F_{n+1})+v_p(Q_{n+1}(0))
       +v_p(A_n^{\rm err})\\
&=v_p(\Delta^0_{n+1})+v_p(A_n^{\rm err})\\
&\le2v_p(\Delta^0_{n+1}).
\end{aligned}
\tag{17}
$$


This is exactly the full-depth divisor (4). The complete cofactor factor $F_{n+1}$ has been retained and then combined using its proved identity; it has not been discarded as a generic unit.

## 7. The exceptional support of the cross-product content is smaller

For $p>3n+3$,


$$
\boxed{p\mid c_n\ \Longrightarrow\ p\mid A_n^{\rm err}.}
\tag{18}
$$


To prove it, reduce both actual simultaneous triples modulo $p$. They are nonzero; each has no common nonzero algebraic root and has full maximum degree $2n$ or $2n+2$, respectively. If $p\mid c_n$, their cross product is zero, so they are proportional over $\mathbb F_p(z)$.

The gcd of the components of either triple is a power of $z$, because all other common roots are excluded. After removing those powers, the primitive polynomial triples are constant multiples of one another. Comparing their maximum degrees therefore gives the exact field relation


$$
Y_{n+1}=\gamma z^2Y_n,\qquad\gamma\in\mathbb F_p^\times.
\tag{19}
$$


The next simultaneous Taylor equations, through degree $3n+3$, then force both first omitted old errors in (12) to vanish modulo $p$. Every coefficient used lies below $p$. This proves (18).

Consequently, outside the explicitly measured error support,


$$
\boxed{
p>3n+3,\ p\nmid A_n^{\rm err}
\quad\Longrightarrow\quad
\min(v_p(G_n),v_p(G_{n+1}))\le v_p(F_{n+1}).
}
\tag{20}
$$


If $F_{n+1}$ is also a unit, the two actual fixed-4 gcds cannot share that prime. Equation (18) is a support assertion, not the stronger unproved claim $c_n\mid A_n^{\rm err}$. Full valuations remain governed by (16).

## 8. Normalized determinant form and honest height consequence

Let $\mathsf Z_r$ be the integer finite-difference matrix from raw_endpoint_scalar_cauchy_restriction.md:


$$
(\mathsf Z_r)_{ij}
=\frac{L_r'}{(r+i)!}
\sum_{s=0}^r(-1)^{r-s}\binom rs
(r+i+s)!\tau_{r+i+s-j},
\quad
L_r'=\operatorname{lcm}(1,\ldots,3r).
$$


Let $B_r=\det\mathsf Z_r[0,\ldots,r-1;\,0,\ldots,r-1]$, the minor obtained by deleting its last row. The exact block elimination gives


$$
\Delta^0_r
=\left(\prod_{j=0}^{r-1}j!\right)
 \frac{\prod_{i=0}^{r-1}(r+i)!}{(L_r')^r}\,B_r.
\tag{21}
$$


All omitted scalar prime factors are at most $3r$. Hence (4) equivalently uses the **single normalized determinant** $B_{n+1}$ at primes above $3n+3$.

The established finite-difference entry bounds give


$$
\log|B_r|\le r^2\log r+O(r^2).
\tag{22}
$$


Also (14) gives the elementary explicit estimate


$$
A_n^{\rm err}
\le L_n(3n)!\sum_{k=n}^{3n}|w_k|.
\tag{23}
$$


At least one entry of the gcd is nonzero, and each is bounded by the right side. The exact cofactor-transport formula and the same normalized-minor bounds imply


$$
\log\sum_k|w_k|\le n^2\log n+O(n^2).
$$


Thus the carrier $B_{n+1}A_n^{\rm err}$ has logarithmic height at most
$2n^2\log n+O(n^2)$.

This does not beat the already available $n^2\log n+O(n^2)$-scale bound for a single $|Z_n|$. The value of (3), (4), and (20) is their actual contiguous prime-power restriction and their explicit origin-error obstruction, not a falsely claimed improvement of the asymptotic height exponent.

## 9. Frozen degree-1-to-2 normalization control

Using only the already saved $Y_1,Y_2$, with no new degree system solved,


$$
\mathcal U_1=
\begin{pmatrix}
-8142z^2-20838z-35280\\
456z^2-10032z+35280\\
-2790z^2+78z-4410
\end{pmatrix}.
$$


Its content is 6, its origin vector is
$(-35280,35280,-4410)=17640(-2,2,-1/4)$, and
$\mathscr D_1=-109938$.
Here $a_1=-1/4,\ b_1=-2,\ I_1=-3,\ J_1=-24$, so $A_1^{\rm err}=3$.
The next deleted-row determinant is $\Delta^0_2=196$.
All prime localizations in (3)–(4) use $p>6$, so the factor 3 in $A_1^{\rm err}$ is correctly outside their scope.

## 10. Exact next step

The neighboring cross product supplies the requested actual determinant relation, and its full coefficient content remains explicit. Shared fixed-4 cancellation is confined to the next unbordered determinant and the two linear first-error functionals. To turn this into a useful global growth estimate, one must control the overlap of $G_n,G_{n+1}$ with these particular factors, or show that the origin-error content $A_n^{\rm err}$ is small on a useful sequence.

No unit theorem for $B_{n+1}$, no generic perfectness assumption, and no transfer from parameter dispersion at a single index is used. The present results do not exclude isolated large fixed-4 cancellation at one degree, nor do they supply the signed-error estimate needed for an irrationality proof.
