> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 310 — P-recursive structure of the all-$s$ $j=1$ containers and its arithmetic limit

Date: 2026-08-31

## 1. Exact outcome and capacity

Retain Item 308's actual rows



$$
p=4h+6s+3,\qquad h,s\geq1,\qquad p\text{ prime},           \tag{1.1}
$$



its parity residue



$$
c_h^*\equiv\Lambda_s^{-1}
       (a_s+b_{s,\epsilon}w_h)\pmod p,\qquad
 \epsilon=h\bmod2,                                         \tag{1.2}
$$



and its necessary integer container



$$
D_{s,\epsilon}=2^{3s+1}a_s^2
                -\delta_{s,\epsilon}b_{s,\epsilon}^2,
\qquad
 \delta_{s,\epsilon}=(-1)^{s(s+1)/2+1+\epsilon}.            \tag{1.3}
$$



This item proves three global statements.

1. The ordinary generating functions of Item 308's exact sequences
   $A_s,U_s,V_s,a_s,b_{s,0},b_{s,1},D_{s,0},D_{s,1}$ are D-finite.
   Equivalently, every one of these sequences is P-recursive.  The proof
   uses the two explicit algebraic constant-term identities in Section 3
   and standard diagonal/Hadamard closure with all hypotheses checked.

2. The quadratic splitting condition suggested by Item 308's norm is
   automatic for every actual prime residue class.  If
   $\eta_s=1$ for odd $s$, $\eta_s=2$ for even $s$, then

   

$$
\left(\frac{\delta_{s,\epsilon}\eta_s}{p}\right)=1
                                                                  \tag{1.4}
$$



   on every actual row.  Thus the norm field excludes no candidate prime.

3. Qualitative P-recursiveness, exponential height, nonzero integer
   coefficients, and the same quadratic-norm shape cannot by themselves
   give any strict fixed-$M$ saving.  For every fixed $K\geq7$, the
   nonzero hypergeometric sequence

   

$$
P_s^{(K)}=\prod_{k=7}^{K}{ks\choose s}             \tag{1.5}
$$



   has a first-order polynomial recurrence and
   $\log P_s^{(K)}=O_K(s)$.  Every prime $6s<p\leq Ks$ divides
   $P_s^{(K)}$.  At fixed $M$, the comparison forms
   $\widetilde a_s=\widetilde b_{s,\epsilon}=P_s^{(K)}$ therefore
   permit logarithmic candidate mass

   

$$
\left(\frac{K-6}{2(3K-2)}\right)M+o(M),              \tag{1.6}
$$



   which tends to the full raw $M/6$ as $K\to\infty$.

Statement 3 is an information-class no-go.  It does not compare the
specific recurrence coefficients of the actual $D_{s,\epsilon}$ with the
comparison recurrence, and it is not a counterexample to an exact
factor-localization theorem for Item 308's sequence.

No such sequence-specific localization is proved here.  Hence



$$
\boxed{\text{new linear log rate}=0,\qquad
        \text{new fixed-}j=1\text{ capacity reduction}=0.} \tag{1.7}
$$



The fixed-$j=1$ ceiling remains $1/36$ per $6M$.

## 2. Item 308 input and the affine numerator split

Item 308 proves



$$
G_s(t)=\frac{N_s(t)}
 {(1-t)^{2s+6}(t^2-2t+2)^{2s+1}}                           \tag{2.1}
$$



and



$$
c_h^*\equiv2^{2s}[t^{2h}]G_s(t)\pmod p.  \tag{2.2}
$$



Write



$$
N_s(t)=N_0(t)+sN_1(t),             \tag{2.3}
$$



where



$$
\begin{aligned}
N_0(t)={}&4-\frac43t-\frac83t^2+\frac{16}3t^3-3t^4+t^5,\\
N_1(t)={}&\frac{80}3t-\frac{224}3t^2+\frac{256}3t^3
                         -46t^4+10t^5.                     \tag{2.4}
\end{aligned}
$$



Item 308's two exact aggregate coefficients are



$$
A_s=-[x^{2s+5}]
 \frac{(1+x)^{3s+1/2}N_s(1+x)}{(1+x^2)^{2s+1}},            \tag{2.5}
$$



and



$$
B_s=U_s+iV_s=[x^{2s}]
 \frac{(1+x)^{3s+1/2}N_s((1-i)(1+x))}
 {2^{2s+1}i^{2s+6}(1+i)^{2s+1}
  (1+(1+i)x)^{2s+6}(1+\lambda x)^{2s+1}},
\quad\lambda=\frac{1+i}{2}.                                \tag{2.6}
$$



All coefficients are taken in the expansions at $x=0$.  These are
identities for every $s\geq1$, not fitted data.

## 3. Two exact constant-term generating functions

Let $\operatorname {CT}_x$ denote constant term in $x$.  Put



$$
F_A(x)=\frac{(1+x)^{1/2}}{1+x^2},\qquad
 R_A(x)=\frac{(1+x)^3}{(1+x^2)^2},\qquad
 u_A=\frac{zR_A(x)}{x^2}.                                  \tag{3.1}
$$



Then (2.5) and the affine split (2.3) give



$$
\boxed{
\sum_{s\geq1}A_sz^s
=-\operatorname {CT}_x\,x^{-5}F_A(x)
\left[
 N_0(1+x)\frac{u_A}{1-u_A}
+N_1(1+x)\frac{u_A}{(1-u_A)^2}
\right].}                                                  \tag{3.2}
$$



Indeed,



$$
F_A(x)R_A(x)^s
       =\frac{(1+x)^{3s+1/2}}{(1+x^2)^{2s+1}},             \tag{3.3}
$$



and



$$
\sum_{s\geq1}u^s=\frac{u}{1-u},\qquad
 \sum_{s\geq1}su^s=\frac{u}{(1-u)^2}.                      \tag{3.4}
$$



For the Gaussian aggregate, set



$$
L_1(x)=1+(1+i)x,\qquad L_2(x)=1+\lambda x,                \tag{3.5}
$$





$$
F_B(x)=-\frac{(1+x)^{1/2}}
 {2(1+i)L_1(x)^6L_2(x)},\qquad
 R_B(x)=\frac{i(1+x)^3}{8L_1(x)^2L_2(x)^2},\qquad
 u_B=\frac{zR_B(x)}{x^2}.                                  \tag{3.6}
$$



Then



$$
\boxed{
\sum_{s\geq1}B_sz^s
=\operatorname {CT}_x\,F_B(x)
\left[
 N_0((1-i)(1+x))\frac{u_B}{1-u_B}
+N_1((1-i)(1+x))\frac{u_B}{(1-u_B)^2}
\right].}                                                  \tag{3.7}
$$



The only non-obvious constant in (3.7) is exact:



$$
\begin{aligned}
&\frac1{2^{2s+1}i^{2s+6}(1+i)^{2s+1}}\\
&\hspace{25mm}
=-\frac1{2(1+i)}\left(\frac{i}{8}\right)^s.                \tag{3.8}
\end{aligned}
$$



Together with



$$
\frac{(1+x)^{3s+1/2}}
 {L_1(x)^{2s+6}L_2(x)^{2s+1}}
=\frac{(1+x)^{1/2}}{L_1(x)^6L_2(x)}
 \left(\frac{(1+x)^3}{L_1(x)^2L_2(x)^2}\right)^s,          \tag{3.9}
$$



this proves (3.7) symbolically for every $s$.

## 4. Rigorous D-finite and P-recursive closure

We use the following standard characteristic-zero closure theorem.

> If $H(x,z)$ is a multivariate D-finite formal power series, then every
> well-defined diagonal, generalized diagonal, or formal constant term in
> one variable is D-finite in the remaining variables.  Algebraic series
> are D-finite.  Univariate D-finite series are closed under addition,
> scalar extension, algebraic substitution, and Hadamard product.
> A univariate series is D-finite exactly when its coefficient sequence is
> P-recursive.

The expansion hypotheses hold here: both (3.2) and (3.7) are formal series
in $z$; the coefficient of each $z^s$ is a Laurent series in $x$ with
a well-defined displayed constant term.  The only algebraic factor is the
branch $(1+x)^{1/2}$ with constant term one.  Every other factor is
rational over $\mathbb Q(i)(x,z)$.  Hence (3.2) and (3.7) are
generalized diagonals of algebraic Laurent series and are D-finite.
Equivalently, before the constant-term rewrite, they extract the
$(2s+5,s)$ and $(2s,s)$ coefficient rays from


$$
\frac{F(x)N_0(x)}{1-zR(x)}
 \quad\text{and}\quad
 \frac{F(x)N_1(x)\,zR(x)}{(1-zR(x))^2},                    \tag{4.0}
$$


which are algebraic power series at $(x,z)=(0,0)$.  This is the standard
generalized-diagonal setting, with no convergence or two-sided-Laurent
assumption.

It follows that $A_s$ and $B_s$ are P-recursive over $\mathbb Q(i)$.
Complex conjugation and rational linear combinations give



$$
U_s=\frac{B_s+\overline{B_s}}2,\qquad
 V_s=\frac{B_s-\overline{B_s}}{2i},                         \tag{4.1}
$$



so $U_s,V_s$ are P-recursive over $\mathbb Q$.

Item 308 defines



$$
\begin{aligned}
X_s&=2^{2s}A_s,\\
Y_{s,0}&=\delta_{s,0}2^{5s+2}U_s,\\
Y_{s,1}&=-\delta_{s,1}2^{5s+2}V_s,\\
a_s&=\Lambda_sX_s,\qquad
b_{s,\epsilon}=\Lambda_sY_{s,\epsilon},\qquad
\Lambda_s=3\,2^{10s+10}.                                  \tag{4.2}
\end{aligned}
$$



Exponential sequences and the period-four signs
$\delta_{s,\epsilon}$ are C-finite.  Hadamard multiplication therefore
proves $a_s,b_{s,0},b_{s,1}$ are P-recursive.  Finally, D-finite series
are closed under Hadamard product, so the pointwise squares $a_s^2$ and
$b_{s,\epsilon}^2$ are P-recursive.  Equation (1.3) proves



$$
\boxed{(D_{s,0})_{s\geq1}\text{ and }(D_{s,1})_{s\geq1}
        \text{ are P-recursive integer sequences}.}        \tag{4.3}
$$



Equivalently, for each parity there exist an order $r$ and polynomials
$q_0(s),\ldots,q_r(s)\in\mathbb Z[s]$, not all zero, such that



$$
\sum_{j=0}^{r}q_j(s)D_{s+j,\epsilon}=0       \tag{4.4}
$$



for all sufficiently large $s$.  Clearing finitely many initial
singularities gives an integral recurrence on its regular tail.

This proves existence and effective holonomicity.  It does **not** identify
a minimal operator, prove favorable recurrence coefficients, or assert that
the generating functions are algebraic.  Those stronger statements remain
open.

## 5. The norm splitting condition is automatic

Item 308 puts



$$
\eta_s=\begin{cases}1,&s\text{ odd},\\2,&s\text{ even},\end{cases}
\qquad
 D_{s,\epsilon}=-\delta_{s,\epsilon}
 \operatorname N_{K_{s,\epsilon}/\mathbb Q}
 (b_{s,\epsilon}+z_s\theta),                               \tag{5.1}
$$



where



$$
K_{s,\epsilon}=
 \mathbb Q[T]/(T^2-\delta_{s,\epsilon}\eta_s),\qquad
 z_s=2^{\lfloor(3s+1)/2\rfloor}a_s.                        \tag{5.2}
$$



The complete actual-prime residue audit is



$$
\begin{array}{c|c|c|c|c|c|c}
s\bmod4&\epsilon&p\bmod8&\delta&\eta&d=\delta\eta&
                              \left(\frac d p\right)\\ \hline
0&0&3&-1&2&-2&1\\
0&1&7& 1&2& 2&1\\
1&0&1& 1&1& 1&1\\
1&1&5&-1&1&-1&1\\
2&0&7& 1&2& 2&1\\
2&1&3&-1&2&-2&1\\
3&0&5&-1&1&-1&1\\
3&1&1& 1&1& 1&1.
\end{array}                                                 \tag{5.3}
$$



This follows from



$$
p\equiv4\epsilon+6s+3\pmod8,\qquad
 \delta_{s,\epsilon}=\left(\frac2p\right),                 \tag{5.4}
$$



and the standard symbols for $-1,2,-2$.  Since $p\geq13$, no actual
prime ramifies in these quadratic algebras.

If $p\mid D_{s,\epsilon}$ and neither norm coordinate vanishes modulo
$p$, quadratic splitting is necessary.  Table (5.3) proves that condition
is already automatic.  If either coordinate vanishes on a norm-zero row,
both do; that is a coefficient-gcd condition, not a quadratic residue-class
obstruction, and the norm identity supplies no theorem controlling it.
Thus the norm identity alone gives exactly zero residue-class saving on the
actual support.

## 6. A nonzero first-order P-recursive comparison family

Fix an integer $K\geq7$ and define (1.5).  Every term is a positive
integer.  Factorial cancellation gives the exact ratio



$$
\frac{P_{s+1}^{(K)}}{P_s^{(K)}}=
\prod_{k=7}^{K}
\frac{\prod_{j=1}^{k}(ks+j)}
{(s+1)\prod_{j=1}^{k-1}((k-1)s+j)}.                        \tag{6.1}
$$



Put



$$
\begin{aligned}
R_K(s)&=\prod_{k=7}^{K}\prod_{j=1}^{k}(ks+j),\\
S_K(s)&=(s+1)^{K-6}
        \prod_{k=7}^{K}\prod_{j=1}^{k-1}((k-1)s+j).
\end{aligned}                                               \tag{6.2}
$$



Then



$$
S_K(s)P_{s+1}^{(K)}-R_K(s)P_s^{(K)}=0,   \tag{6.3}
$$



a first-order P-recursive relation with



$$
\deg R_K=\deg S_K
                  =\sum_{k=7}^{K}k=\frac{K(K+1)}2-21.      \tag{6.4}
$$



Stirling's formula gives the exact exponential rate



$$
\begin{aligned}
\log P_s^{(K)}
 &=s\sum_{k=7}^{K}
       \bigl(k\log k-(k-1)\log(k-1)\bigr)+O_K(\log s)\\
 &=s\bigl(K\log K-6\log6\bigr)+O_K(\log s)=O_K(s).         \tag{6.5}
\end{aligned}
$$



The prime coverage is also exact.  Let $p$ be prime with



$$
6s<p\leq Ks.                 \tag{6.6}
$$



Choose $k=\lceil p/s\rceil$.  Then $7\leq k\leq K$ and



$$
(k-1)s<p\leq ks.                \tag{6.7}
$$



Since $p>s$ and $ks<2p$, Legendre's factorial formula gives



$$
v_p{ks\choose s}
 =\left\lfloor\frac{ks}{p}\right\rfloor
  -\left\lfloor\frac{s}{p}\right\rfloor
  -\left\lfloor\frac{(k-1)s}{p}\right\rfloor
 =1.                                                        \tag{6.8}
$$



Thus



$$
\boxed{6s<p\leq Ks\quad\Longrightarrow\quad
                         p\mid P_s^{(K)}.}                 \tag{6.9}
$$



No primes are scanned or factored in this proof.

To retain the exact Item 308 form, define



$$
\widetilde a_s=\widetilde b_{s,\epsilon}=P_s^{(K)},\qquad
 \widetilde D_{s,\epsilon}
 =(P_s^{(K)})^2(2^{3s+1}-\delta_{s,\epsilon}).              \tag{6.10}
$$



Every $\widetilde D_{s,\epsilon}$ is nonzero, has the same
$\eta z^2-\delta b^2$ norm shape, is P-recursive, and has logarithmic
height $O_K(s)$.  Its clearing denominator is one.  Whenever
$p\mid P_s^{(K)}$, both the comparison linear form and its norm container
vanish modulo $p$.

## 7. Exact fixed-$M$ mass of the comparison

Item 264's actual indexing is



$$
\mathcal S_M=\{s\geq1:4s\leq M-5,\ s\equiv M+1\pmod3\},
\qquad
 p_s=\frac{4M+2s+1}{3}.                                    \tag{7.1}
$$



Every candidate satisfies



$$
p_s-6s=\frac{4M-16s+1}{3}\geq7,                           \tag{7.2}
$$



because $4s\leq M-5$.  Also



$$
p_s\leq Ks
 \quad\Longleftrightarrow\quad
 s\geq\frac{4M+1}{3K-2}.                                   \tag{7.3}
$$



Therefore (6.9) captures every prime candidate in the upper-$s$ slice
(7.3).  Under the bijection $s\mapsto p_s$, this slice is, up to bounded
endpoint errors,



$$
\frac{4K}{3K-2}M\leq p\leq\frac32M.                       \tag{7.4}
$$



The prime number theorem gives logarithmic mass



$$
\begin{aligned}
\sum_{\substack{s\in\mathcal S_M,\ p_s\ {\rm prime}\\
                 s\geq(4M+1)/(3K-2)}}\log p_s
 &=\left(\frac32-\frac{4K}{3K-2}\right)M+o(M)\\
 &=\boxed{\left(\frac{K-6}{2(3K-2)}\right)M+o(M).}          \tag{7.5}
\end{aligned}
$$



Normalized per $6M$, this is



$$
\frac{K-6}{12(3K-2)}+o(1)
                    \longrightarrow\frac1{36}.             \tag{7.6}
$$



Consequently, for every $c<1/6$, some fixed $K$ gives a nonzero
first-order P-recursive comparison family of exponential height and exact
norm shape whose admissible tied-prime mass is greater than $cM+o(M)$.
No strict coefficient below the raw $1/6$, equivalently below $1/36$
per $6M$, follows uniformly from those qualitative properties alone.

The degree in (6.4) grows with $K$.  Thus this theorem does not rule out
a result using a separately bounded operator degree, the exact operator
coefficients of Item 308, or a special factor theorem for its initial
conditions.  The comparison also realizes its vanishing through
$p\mid\gcd(\widetilde a_s,\widetilde b_{s,\epsilon})$.  A moving-prime
gcd bound for the **actual** Item 308 coefficients would therefore escape
this no-go.

## 8. Capacity, strict scope, and smallest remaining lemma

The actual P-recursive theorem (4.3) compresses the sequence but gives no
prime-factor localization.  The norm audit (5.3) removes no residue class.
The comparison theorem proves that recurrence existence, exponential
height, and norm shape have no admission value by themselves.

The sufficient container target remains



$$
\boxed{
 \mathcal W_D(M)=
 \sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                  p_s\text{ prime}\\
                  p_s\mid D_{s,h_s\bmod2}}}\log p_s=o(M),}
 \qquad
 h_s=\frac{M-4s-2}{3}.                                     \tag{8.1}
$$



The smallest new lemma capable of using Item 310 is a sequence-specific
horizontal theorem for the **exact** annihilating operator or exact
constant-term diagonal which proves (8.1), or an exact factor localization
placing all sufficiently large rational prime factors of
$D_{s,\epsilon}$ outside the tied interval


$$
6s+7\leq p\leq Ks                  \tag{8.2}
$$


on all but weighted-$o(M)$ actual indices.  An exact moving-prime bound on
$\gcd(a_s,b_{s,\epsilon})$, followed by control of the nondegenerate norm
factors, is another admissible route.  None of these statements is proved.

- **PROVED:** (3.2), (3.7), the P-recursiveness theorem (4.3), the complete
  actual-prime splitting table (5.3), and the nonzero first-order
  hypergeometric information-class no-go (6.1)--(7.6).
- **EXACT FINITE ONLY:** the replay's bounded coefficient and recurrence
  controls.  They are not evidence for prime density or factor patterns.
- **OPEN:** a minimal or arithmetically useful exact recurrence,
  algebraicity of the actual generating functions, universal nonvanishing
  of the actual containers, factor localization, (8.1), the full
  fixed-$j=1$ closer, Route 1, and every conclusion about $e+\pi$.
- **NOT CLAIMED:** a large prime scan, a factor census, or positive capacity.

The booking and retained ceiling are unchanged:



$$
\boxed{\text{capacity booked}=0,\qquad
       \text{fixed-}j=1\text{ ceiling}=\frac1{36}\text{ per }6M.}    \tag{8.3}
$$



No canonical, master, or status file is edited by this research package.

## 9. Deterministic replay

From the archive root, run

~~~text
python work/item310_j1_container_holonomy_no_go_certificate.py --output work/item310_j1_container_holonomy_no_go_certificate.replay.json
~~~

The checker uses only standard-library exact integer, rational, and
Gaussian-rational arithmetic.  It pins Item 308; checks the affine numerator
split, constant-term base/ratio decompositions, P-recursive closure graph,
Euler/splitting table, exact hypergeometric recurrence, height-rate
telescoping, prime-interval logic, and fixed-$M$ mass normalization.  Its
bounded rows are labeled replay-only.  It performs no prime scan and no
factorization.
