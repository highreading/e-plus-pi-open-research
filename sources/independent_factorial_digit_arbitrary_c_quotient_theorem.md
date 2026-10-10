> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact integral quotient for every polynomial-$C$ degree

## 1. Scope and verdict

This note gives a self-contained reduction of the square high-jet block in
the factorial-digit Hermite--Padé family with degrees $(a,b,c)$, for every
$c\geq1$.  An $(b+c)\times(b+c)$ determinant is reduced to a
$c\times c$ determinant with integer entries.  The same transformation
gives exact rank criteria for both the high block and the full
endpoint-constrained Hermite--Padé matrix.

The result is an all-degree algebraic identity.  It does **not** prove that
the quotient determinant is always nonzero.  Indeed, the canonical digits
of $\pi$ already give quotient-determinant zeros in small degrees.  The
finite computations below are checks and diagnostics, not an extrapolation
to all degrees.  In particular, this result does not settle the arithmetic
nature of $e+\pi$.

## 2. The endpoint-constrained high block

Let $(g_n)_{n\geq0}$ be any integer sequence and write, formally,



$$
G(z)=\sum_{n\geq0}g_n\frac{z^n}{n!}.
\tag{1}
$$



The canonical specialization used in the finite audit is



$$
g_0=3,\qquad g_1=0,\qquad
 g_n=\lfloor n!\pi\rfloor-n\lfloor(n-1)!\pi\rfloor
 \quad(n\geq2).
\tag{2}
$$



The telescoping identity



$$
3+\sum_{n=2}^M\frac{g_n}{n!}
   =\frac{\lfloor M!\pi\rfloor}{M!}
\tag{3}
$$



shows that this entire function satisfies $G(1)=\pi$.

Consider polynomials $A,B,C$ of degrees at most $a,b,c$,
respectively, subject to



$$
(A+Be^z+CG)^{(k)}(0)=0
 \quad(0\leq k\leq a+b+c),
 \qquad B(1)=C(1).
\tag{4}
$$



Put $N=b+c$ and denote the common endpoint coefficient by
$\beta=B(1)=C(1)$.  Division by $z-1$ gives uniquely



$$
B(z)=\beta+(z-1)T(z),\qquad
 C(z)=\beta+(z-1)S(z),
\tag{5}
$$



where



$$
T(z)=\sum_{j=0}^{b-1}t_jz^j,\qquad
 S(z)=\sum_{j=0}^{c-1}s_jz^j.
\tag{6}
$$



An empty sum is understood when a degree is zero.  For nonnegative $k,j$,
set $k^{\underline j}=k!/(k-j)!$ when $j\leq k$ and zero otherwise,
and put $g_{-1}=0$.  Define



$$
u_j(k)=k^{\underline j}(k-j-1)
       \quad(0\leq j<b),
\tag{7}
$$





$$
v_j(k)=k^{\underline j}
 \bigl((k-j)g_{k-j-1}-g_{k-j}\bigr)
       \quad(0\leq j<c).
\tag{8}
$$



These are exactly the derivatives at zero of $z^j(z-1)e^z$ and
$z^j(z-1)G(z)$, respectively.  Since the $A$-column vanishes above
degree $a$, the high equations, at the nodes
$k=a+1,\ldots,a+N$, are



$$
\mathcal H_{a,b,c}\theta+\beta y=0,
\tag{9}
$$



where



$$
\mathcal H_{a,b,c}
 =\left(u_0,\ldots,u_{b-1},v_0,\ldots,v_{c-1}\right)
   \big|_{k=a+1}^{a+N},
\tag{10}
$$





$$
\theta=(t_0,\ldots,t_{b-1},s_0,\ldots,s_{c-1})^{\mathsf T},
 \qquad y(k)=1+g_k.
\tag{11}
$$



## 3. The integral quotient matrix

For $m\geq0$, define



$$
D_{a,m}
 =\frac{1}{a!}\left.\Delta^m(n!)\right|_{n=a}
 =\sum_{\ell=0}^m(-1)^{m-\ell}\binom m\ell
   (a+1)^{\overline\ell}.
\tag{12}
$$



Thus every $D_{a,m}$ is an integer.  Equivalently,



$$
D_{a,0}=1,\qquad D_{a,1}=a,\qquad
 D_{a,m}=(a+m-1)D_{a,m-1}+(m-1)D_{a,m-2}.
\tag{13}
$$



For a column of integer samples $h(a+1),\ldots,h(a+N)$, write



$$
\delta_m(h)=\Delta^mh(a+1)
 =\sum_{\ell=0}^m(-1)^{m-\ell}\binom m\ell
   h(a+1+\ell).
\tag{14}
$$



For $c\geq1$, define the integral quotient column



$$
\widetilde{\mathcal Q}_{a,b,c}(h)=
 \begin{pmatrix}
 \displaystyle
 \sum_{m=0}^b(-1)^m\frac{b!}{m!}D_{a,m}\delta_m(h)\\[6pt]
 \delta_{b+1}(h)\\
 \delta_{b+2}(h)\\
 \vdots\\
 \delta_{b+c-1}(h)
 \end{pmatrix}.
\tag{15}
$$



When $c=1$, only the first row is present.  Finally put



$$
\widetilde Q_{a,b,c}
 =\left(
 \widetilde{\mathcal Q}_{a,b,c}(v_0),\ldots,
 \widetilde{\mathcal Q}_{a,b,c}(v_{c-1})
 \right),
 \qquad
 \widetilde q_y=\widetilde{\mathcal Q}_{a,b,c}(y).
\tag{16}
$$



All entries in (15)--(16) are integers: the samples and their forward
differences are integers; (12) is integral; and $b!/m!\in\mathbb Z$
for $0\leq m\leq b$.  No unrecorded denominator-clearing convention
is being used.

## 4. Determinant theorem, including the sign

Let



$$
\kappa_b=\prod_{j=0}^{b-1}j!,
\tag{17}
$$



with an empty product equal to one.  Then, for every integer sequence
$(g_n)$, every $a,b\geq0$, and every $c\geq1$,



$$
\boxed{
 \det\mathcal H_{a,b,c}
   =(-1)^b\kappa_b\det\widetilde Q_{a,b,c}.}
\tag{18}
$$



Here is the complete basis calculation.

On polynomials written in the falling-factorial basis, define



$$
\mathscr L\!\left(\sum_jr_jk^{\underline j}\right)=\sum_jr_j.
\tag{19}
$$



Then $\mathscr L(1)=1$, while



$$
u_j=k^{\underline{j+1}}-k^{\underline j}
 \quad\Longrightarrow\quad \mathscr L(u_j)=0.
\tag{20}
$$



Because $u_j$ is monic of degree $j+1$, the ordered list
$(1,u_0,\ldots,u_{b-1})$ is a basis of the polynomials of degree at
most $b$; the $u_j$'s are therefore a basis of the kernel of
$\mathscr L$ on that space.

Set



$$
w_m(k)=(k-a-1)^{\underline m}.
\tag{21}
$$



Applying the Poisson realization



$$
\mathscr L(p)=e^{-1}\sum_{n\geq0}\frac{p(n)}{n!}
\tag{22}
$$



to $(1+z)^{k-a-1}$ gives



$$
\sum_{m\geq0}\mathscr L(w_m)\frac{z^m}{m!}
 =e^z(1+z)^{-a-1}
 =\sum_{m\geq0}(-1)^mD_{a,m}\frac{z^m}{m!}.
\tag{23}
$$



Hence



$$
\mathscr L(w_m)=(-1)^mD_{a,m}.
\tag{24}
$$



For the samples of a column $h$, let $p_h$ be their unique
interpolating polynomial of degree at most $N-1$.  Newton interpolation
says



$$
p_h=\sum_{m=0}^{N-1}\frac{\delta_m(h)}{m!}w_m.
\tag{25}
$$



Now use the ordered, graded, monic basis



$$
\mathcal B=
 (1,u_0,\ldots,u_{b-1},w_{b+1},\ldots,w_{N-1})
\tag{26}
$$



of the polynomials of degree at most $N-1$.  The apparently missing
$w_b$ is not missing a dimension: degrees zero through $b$ are already
represented by $1,u_0,\ldots,u_{b-1}$.  Removing the terms $w_m$ with
$m>b$ from (25) leaves a polynomial in that degree-$b$ subspace.  Its
coordinate along $1$ in the basis
$(1,u_0,\ldots,u_{b-1})$ is, by (20) and (24),



$$
\lambda(h)=\sum_{m=0}^b(-1)^m
 \frac{D_{a,m}}{m!}\delta_m(h).
\tag{27}
$$



Its other coordinates need not be written.  The coordinates along
$w_{b+r}$, for $1\leq r<c$, are exactly
$\delta_{b+r}(h)/(b+r)!$.

Let $E_{\mathcal B}$ be the evaluation matrix of (26) at the consecutive
nodes $a+1,\ldots,a+N$.  Because (26) is graded and monic, its determinant
equals the consecutive-node Vandermonde determinant: the change from
(26) to the ordered monomial basis is unit triangular and contributes
neither a factor nor a sign.  Thus



$$
\det E_{\mathcal B}
 =\kappa_N=\prod_{m=0}^{N-1}m!.
\tag{28}
$$



The coordinate matrix of the columns
$(u_0,\ldots,u_{b-1},v_0,\ldots,v_{c-1})$ in (26) has the block shape



$$
\begin{pmatrix}
 0&\lambda(v_0)\ \cdots\ \lambda(v_{c-1})\\
 I_b&*\\
 0&R
 \end{pmatrix},
 \qquad
 R_{rj}=\frac{\delta_{b+r}(v_j)}{(b+r)!}
 \quad(1\leq r<c).
\tag{29}
$$



Moving the first row past the $b$ identity rows uses exactly $b$
adjacent transpositions.  The resulting matrix is block upper triangular,
so its determinant is the determinant of the rational quotient matrix
$Q^{\mathrm{rat}}$ whose first row is (27) and whose remaining rows are
$R$.  Therefore



$$
\det\mathcal H_{a,b,c}
 =(-1)^b\kappa_N\det Q^{\mathrm{rat}}.
\tag{30}
$$



Multiplying the quotient rows, in order, by



$$
b!,\ (b+1)!,\ldots,(b+c-1)!
\tag{31}
$$



turns $Q^{\mathrm{rat}}$ into $\widetilde Q$.  Finally,



$$
\frac{\kappa_N}{b!(b+1)!\cdots(b+c-1)!}
 =\prod_{m=0}^{b-1}m!=\kappa_b,
\tag{32}
$$



which proves (18), including its sign and every factorial cancellation.

## 5. Exact rank and full-nullity criteria

The same calculation proves more than the determinant formula.  Evaluation
in (28), the row permutation in (29), and the row scalings in (31) are all
invertible over $\mathbb Q$.  Consequently,



$$
\boxed{\operatorname{rank}\mathcal H_{a,b,c}
 =b+\operatorname{rank}\widetilde Q_{a,b,c},}
\tag{33}
$$



and, after adjoining the column $y$,



$$
\boxed{\operatorname{rank}[\mathcal H_{a,b,c}\mid y]
 =b+\operatorname{rank}[\widetilde Q_{a,b,c}\mid\widetilde q_y].}
\tag{34}
$$



For any $(\theta,\beta)$ satisfying the high system (9), the jet equations
with $0\leq k\leq a$ determine the coefficients of $A$ uniquely: the
coefficient of $z^k$ in $A$ occurs with the nonzero diagonal factor
$k!$.  Thus restriction to the high variables gives an isomorphism
between the kernel of the full bordered matrix in (4) and the kernel of
$[\mathcal H\mid y]$.  It follows that



$$
\boxed{
 \operatorname{nullity}(M^{\mathrm{full}}_{a,b,c})
 =c+1-\operatorname{rank}
 [\widetilde Q_{a,b,c}\mid\widetilde q_y].}
\tag{35}
$$



In particular:

* $\mathcal H_{a,b,c}$ is nonsingular if and only if
  $\det\widetilde Q_{a,b,c}\neq0$.
* The full bordered matrix has full row rank, equivalently nullity one, if
  and only if
  $\operatorname{rank}[\widetilde Q\mid\widetilde q_y]=c$.
* If $\det\widetilde Q\neq0$, then the full matrix has nullity one and its
  kernel line has $\beta\neq0$.
* If $\det\widetilde Q=0$ but the augmented quotient has rank $c$, then
  the full matrix still has nullity one, but its unique kernel line has
  $\beta=B(1)=C(1)=0$.
* If the augmented quotient has rank below $c$, the full nullity is
  greater than one.

For the fourth item, if a kernel vector had $\beta\neq0$, then
$\widetilde q_y$ would lie in the column space of $\widetilde Q$;
the augmented rank would equal $\operatorname{rank}\widetilde Q<c$, a
contradiction.  This also makes the distinction between the two rank tests
explicit.

The fourth item says nothing by itself about $A(1)$.  Vanishing of the
common target coefficient must not be conflated with vanishing of the
entire endpoint pair.

## 6. Recovery of the known edge cases

When $c=1$, (15) has one entry and (16) is the one by one matrix



$$
\widetilde Q_{a,b,1}=(F_{a,b}),\qquad
 F_{a,b}=\sum_{m=0}^b(-1)^m\frac{b!}{m!}
 D_{a,m}\Delta^mv_0(a+1).
\tag{36}
$$



Therefore (18) becomes exactly



$$
\det\mathcal H_{a,b,1}=(-1)^b\kappa_bF_{a,b}.
\tag{37}
$$



Separating the last forward-difference term gives the previously audited
recurrence



$$
F_{a,0}=v_0(a+1),\qquad
 F_{a,b}=bF_{a,b-1}+(-1)^bD_{a,b}\Delta^bv_0(a+1).
\tag{38}
$$



The case $c=0$ has no quotient rows and is not covered by (15).  Directly
applying the same Poisson/Vandermonde basis argument gives the separate
identity



$$
\det\mathcal H_{a,b,0}=\kappa_bD_{a,b}.
\tag{39}
$$



For completeness, apply the $b+1$ linear functionals
$\mathscr L,\operatorname{ev}_{a+1},\ldots,\operatorname{ev}_{a+b}$
to either graded monic basis
$(1,u_0,\ldots,u_{b-1})$ or $(w_0,\ldots,w_b)$.  In the first basis
the determinant is $\det\mathcal H_{a,b,0}$.  In the second, the last
column is $((-1)^bD_{a,b},0,\ldots,0)^{\mathsf T}$, while the remaining
evaluation minor is lower triangular with determinant $\kappa_b$.
The cofactor sign cancels $(-1)^b$, proving (39).

Thus no empty $0\times0$ determinant convention is being used to extend
(18) outside its stated range.

## 7. Independent exact finite checks

The companion script independently generated the canonical jets through
degree 18 from



$$
\pi=4\bigl(\arctan(1/2)+\arctan(1/3)\bigr).
\tag{40}
$$



It used the alternating series through indices 100 and 70, respectively,
with the first omitted term as the rigorous remainder bound.  For a partial
sum through index $L$, the implemented next-term magnitude is



$$
|t_L|\frac{2L+1}{(2L+3)q^2},
\tag{41}
$$



which is the exact ratio required for $\arctan(1/q)$.  The resulting
rational interval certifies every floor used in (2).  The resulting jet
vector is



$$
(g_0,\ldots,g_{18})=
 (3,0,0,0,3,1,5,6,5,0,1,4,7,8,0,6,7,10,7).
\tag{42}
$$



It agrees entry by entry with both independent reference computations:
the corrected $c=1$ script/result have SHA-256 hashes
$da614228b3a97ad1330d452a63690f075354f91c52e5b4029c745c2c650c87fe$
and
$80f163658ab10039364f256cbc6439f9ba0cc3e650f6613c38579206f07824fb$;
the full polynomial-$C$ script/result have hashes
$547ab656935dade778720c1f08f00c84eb913f26bc44159a71ac83099c4794fc$
and
$2f527c542af6f6ed4b06864e2c063443462ee781e911a387ff0776704b6ea470$.

For every one of the 1,140 triples with $a,b,c\geq0$, $c>0$, and
$a+b+c\leq18$, the script constructed both the original high matrix and
the quotient from scratch.  It checked (18), (33), (34), and (35) by exact
rational/integer linear algebra.  It also checked (38) for all 171
admissible $c=1$ pairs.  Some exact determinant comparisons, included to
expose the sign and factorial normalization, are

| $(a,b,c)$ | $\det\widetilde Q$ | $(-1)^b\kappa_b$ | $\det\mathcal H$ |
|---:|---:|---:|---:|
| $(0,0,1)$ | $3$ | $1$ | $3$ |
| $(4,2,3)$ | $469354248$ | $1$ | $469354248$ |
| $(5,4,2)$ | $-135791056$ | $12$ | $-1629492672$ |
| $(8,3,1)$ | $35192$ | $-2$ | $-70384$ |

The quotient determinant was nonzero in 1,135 cases and zero in exactly
five:



$$
(1,0,1),\ (1,0,2),\ (1,1,1),\ (2,0,1),\ (2,0,2).
\tag{43}
$$



In each of these five finite cases the augmented quotient still had rank
$c$, so every full bordered matrix in the scan had full row rank and
nullity one.  The common target coefficient was zero in (43); direct kernel
reconstruction happened also to give $A(1)=0$ in all five cases.  Only
the first statement follows from the general rank theorem.

As a convention-independent check, the script repeated the determinant
and rank identity on all 220 positive-$c$ triples of total degree at most
10 for a deterministic integral sequence unrelated to $\pi$.  All checks
passed.  This supports the universal algebraic reduction; it does not add
a nonvanishing theorem.

## 8. Reproduction and frozen-artifact policy

From the archive root, run

    python -m py_compile scripts/independent_factorial_digit_arbitrary_c_quotient_certificate.py
    python scripts/independent_factorial_digit_arbitrary_c_quotient_certificate.py

For a byte-for-byte rerun without overwriting the archived result, use

    python scripts/independent_factorial_digit_arbitrary_c_quotient_certificate.py \
      --max-total 18 \
      --output /tmp/independent_factorial_digit_arbitrary_c_quotient_T18.json
    cmp results/independent_factorial_digit_arbitrary_c_quotient_T18.json \
      /tmp/independent_factorial_digit_arbitrary_c_quotient_T18.json

The script and JSON hashes are recorded in the final audit report alongside
the hash of this note.  Once those hashes are reported, the three files are
treated as frozen.  Any later correction must create an explicitly
superseding artifact rather than silently changing one of them.
