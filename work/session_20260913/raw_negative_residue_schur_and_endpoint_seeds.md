> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Negative residue classes: fixed Schur seeds and the actual endpoint

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: FULL PASS by audit_computations, saved as
raw_negative_residue_transfer_independent_review.md. The review identified
and the source corrected the added-column starting-residue transcription
in Section 3; no theorem or seed value changed.
Only the predeclared symbolic seeds k=1,2
are evaluated; no new actual canonical degree or prime scan is used.

This note treats n congruent to -k-1 modulo p with p>2k+1.
The fixed Appell background is the integer -k-1, not k.
The full determinant and precisely the cofactors needed by the endpoint
reduce to fixed partitions. The resulting finite integer endpoint seed
controls every degree in the residue class, subject to two explicit seed
unit conditions. No prime-power lift is asserted.

## 1. Definitions and statement

For any integer background b, including b<0, put


$$
{\cal A}_d^{[b]}(x)
 =d![z^d]e^{xz}(1+z^2)^b
 =\sum_{h=0}^{\lfloor d/2\rfloor}
   \binom bh(d)_{\underline{2h}}x^{d-2h}.
 \tag{1}
$$


For a partition lambda write M_lambda^[b]=H_lambda s_lambda under
the complete-function specialization e^(xz)(1+z²)^b.
These are integer polynomials. The power sums are
p_1=x, p_(2h)=2b(-1)^(h+1), and p_(2h+1)=0 for h>=1.
Thus changing the background sign must not be confused with leaving
the complete/elementary convention unchanged.

Fix k>=1 and an odd prime p>2k+1. Write


$$
n=ap-k-1,\quad a\ge1,\qquad b=-k-1,\qquad d=k(k+1).
$$


Define the fixed partitions and integers


$$
\lambda^-=(k^{k+1}),\qquad
 \gamma_i=((k+1)^{k-i},k^i)\quad(0\le i\le k),
$$




$$
D_k^-(x)=M_{\lambda^-}^{[b]}(x),\quad
 C_{k,i}^-(x)=M_{\gamma_i}^{[b]}(x),\quad
 D=D_k^-(1),\quad C_i=C_{k,i}^-(1).
 \tag{2}
$$


For 0<=h<=k define finite integers


$$
J_{k,h}=h!\sum_{i=h}^k(-1)^{k-i}\binom{b+i}{i-h}
 \sum_{u=0}^{\lfloor(k-i)/2\rfloor}
   \binom bu(b+i+1)^{\overline{2u}}\binom b{i+2u}C_{i+2u}.
 \tag{3}
$$


Here an overline denotes a rising factorial, an underline a falling
factorial, and all binomial coefficients with negative integer top
arguments have their usual integral meaning. Put


$$
A_{k,h}=\sum_{s=h}^k(-1)^s\binom ks\binom sh
                  (b)_{\underline{s-h}},\qquad
 {\cal E}_k^-=\sum_{h=0}^k A_{k,h}J_{k,h}\in\mathbb Z.
 \tag{4}
$$



Retain the actual primitive dual normalization


$$
W_n(t)=t^n(t-1)^nV_n(t),\quad
 b_{n,l}=\frac{U_{n,l}}{(n+l)!}\in\mathbb Z,\quad
 \gcd_{0\le l\le n}b_{n,l}=1.
 \tag{5}
$$


Let Pe_n=[Qhat_n e^z]_(<=2n), Pa_n=[Qhat_n atan z]_(<=2n),
Z_n=Qhat_n(1), N_n=Pe_n(1)+4Pa_n(1), and
q_n=|Z_n|/gcd(|Z_n|,|N_n|). These retain the original common
integer scale.

**Theorem.** If p does not divide D, then V_n(1) is a p-unit and


$$
\boxed{D V_n^{(h)}(1)\equiv J_{k,h}V_n(1)\pmod p
        \quad(0\le h\le k),}
 \tag{6}
$$




$$
\boxed{D\,Pe_n(1)\equiv{\cal E}_k^- V_n(1)\pmod p.}
 \tag{7}
$$


Consequently, if


$$
p\nmid D{\cal E}_k^-,\qquad
 v_p(n!)>\lfloor\log_p(2n)\rfloor,
 \tag{8}
$$


then the actual reduced denominator satisfies


$$
\boxed{v_p(q_n)=v_p(Z_n)\ge v_p(n!).}                 \tag{9}
$$


For a fixed k and p satisfying the two seed unit conditions, the
factorial threshold holds for every sufficiently large n in this
residue class. There is no restriction on the other factors of n.
If D is a unit but E_k^- vanishes modulo p, (7) instead proves
that the actual exponential endpoint is divisible by p.
If D vanishes modulo p, the primitive-unit argument below is unavailable;
that fact alone says nothing about the actual reduced denominator.
The already reviewed k=0 case is the separate n+1 congruence theorem.

## 2. Integral content comparison and inflation

We use the proved integral central-character lemma from
raw_appell_neighbor_content_and_denominator.md:
for partitions lambda,eta of the SAME size, equality of their content
multisets modulo p implies


$$
H_\lambda s_\lambda\equiv H_\eta s_\eta
       \pmod{p\mathbb Z[p_1,p_2,\ldots]}.
 \tag{10}
$$


Its primary input is integral generation by symmetric polynomials in
Jucys--Murphy elements, from Ryba, *Stable centres of wreath products*,
Proposition 3.11 and Theorem 3.14.
[Primary paper](https://alco.centre-mersenne.org/item/10.5802/alco.264.pdf).
The independent review is raw_appell_neighbor_content_independent_review.md.
No comparison between different symmetric-group sizes is implicit in (10).

For completeness, the inflation step used here is the same elementary
one as Section 2 of raw_positive_residue_schur_and_endpoint_transfer.md,
and is valid for negative background. If lambda has r rows, its increasing
Appell degrees are d_i=lambda_(r-i)+i, 0<=i<r, and


$$
M_\lambda^{[b]}(x)=
 \frac{\det(({\cal A}_{d_i}^{[b]})^{(j)}(x))_{i,j=0}^{r-1}}
      {\prod_{i<j}(d_j-d_i)}.                         \tag{11}
$$


Suppose max d_i<p. Enlarge the first row by Delta>=0 with p|Delta.
Only the largest d_i changes. Both Vandermondes are congruent p-units.
For L>=0 and ell=L mod p,


$$
{\cal A}_L^{[n]}(x)
 \equiv x^{L-\ell}{\cal A}_\ell^{[b]}(x)\pmod p
 \quad(n\equiv b\pmod p).
 \tag{12}
$$


Indeed every falling factorial of length >=p vanishes modulo p.
For length 2h<p, it vanishes also when 2h>ell; otherwise h! is
a p-unit, so binom(n,h) reduces to binom(b,h). This argument includes
negative integer b because those binomial coefficients are integral.
The derivative of x^Delta vanishes modulo p, and (11) therefore gives


$$
M_{\lambda+\Delta e_1}^{[n]}(x)
       \equiv x^\Delta M_\lambda^{[b]}(x)\pmod p.
 \tag{13}
$$


Only the maximum Appell degree must be less than p. The partition
size need not be less than p. In particular no factorial of the
partition size is inverted.

## 3. Full rectangle and the required cofactor residues

The actual determinant partition is lambda_D=(n^(n+1)), of size
N=n(n+1). Its contents modulo p consist of


$$
B=a^2p-a(2k+1)
 \quad\hbox{copies of every residue, plus the contents of }(k^{k+1}).
 \tag{14}
$$


One direct count starts with an ap by ap square, which has a²p
copies of every residue. Remove the last k rows and the last k+1
columns. Each removed row or column contains a copies of every
residue. Their overlap is added back. With zero-based indices its
contents are u-v-1, 0<=u<=k and 0<=v<k. The map
c'=k-1-v, r'=k-u identifies them with the contents c'-r' of
the k-wide, k+1-high rectangle. Thus (14) is an equality of multisets.
The integer B is positive under p>2k+1.

Since N=d+pB, enlarge the first row of (k^(k+1)) by pB.
The added segment consists of B full residue sets and the new
partition has exactly size N. Apply (10), then (13); the small
Appell degrees are k,k+1,...,2k, all below p. Hence


$$
\boxed{M_D^{[n]}(x)\equiv
             x^{N-d}D_k^-(x)\pmod p.}              \tag{15}
$$



For the endpoint calculation we need precisely coefficient indices


$$
l=vp+i,\qquad 0\le v\le a-1,\quad0\le i\le k.
 \tag{16}
$$


The corresponding actual cofactor index is j=n-l, whose partition
is lambda_j=((n+1)^j,n^(n-j)), of size N_j=n²+j=N-l.
Start with the n by n square. Its residue multiset is
a²p-2a(k+1) uniform copies plus a (k+1)-square.
The additional column has contents n,n-1,...,n-j+1, hence
residues -k-1,-k-2,...,-k-j.
As
j=(a-v)p-(k+1+i), this is a-v uniform copies minus the
interval -k,-k+1,...,i.

That interval is exactly the removable rim strip of the small
(k+1)-square formed by its bottom row and i boxes above it in its
rightmost column. Removing the strip leaves
gamma_i=((k+1)^(k-i),k^i). Therefore the actual cofactor contains
B-v uniform copies plus gamma_i. Its size is
N_j=d-i+p(B-v), with B-v>=0.

Enlarge the first row of gamma_i by p(B-v). The small Appell
degree set is


$$
\{k,k+1,\ldots,2k\}\setminus\{k+i\}.
 \tag{17}
$$


Its degrees are distinct and below p. The same-size content lemma
and inflation give


$$
\boxed{M_{n-l}^{[n]}(x)\equiv
    x^{\,N-l-(d-i)}C_{k,i}^-(x)\pmod p
       \quad(l\equiv i\pmod p,\ 0\le i\le k).}       \tag{18}
$$


This is deliberately a statement about the required residue classes,
not an assertion about every cofactor.

## 4. Primitive endpoint normalization

The reviewed exact hook/cofactor identity is


$$
b_{n,l}=(-1)^{n-l}\binom nl V_n(1)
                    \frac{M_{n-l}^{[n]}(1)}{M_D^{[n]}(1)}.
 \tag{19}
$$


It is proved with the original factorial and primitive normalizations
in raw_appell_all_cofactors_and_endpoint_units.md and rechecked in
raw_appell_column_endpoint_independent_review.md.
If p does not divide D, (15) makes the denominator in (19) a p-unit.
All the other displayed factors are p-integral. If p divided V_n(1),
then every b_(n,l) would be divisible by p, contradicting (5).
Thus V_n(1) is a p-unit. No individual cofactor unit assumption is needed.

Combining (18)-(19), for indices (16),


$$
D\,b_{n,l}\equiv
       (-1)^{n-l}\binom nl V_n(1)C_i\pmod p.
 \tag{20}
$$


The remaining b-coordinates need not have this small description.
The next step shows that they are not needed for (6)-(7).

## 5. Exact endpoint derivatives and Lucas elimination

Write w_r=[t^r]W_n(t). The following identities hold over the integers:


$$
\frac{V_n^{(h)}(1)}{h!}
      =\sum_{l=0}^n\binom{n+l}{n+h}w_{2n+l},        \tag{21}
$$




$$
w_{2n+l}=\sum_{\substack{u\ge0\\l+2u\le n}}
       \binom nu(n+l+1)^{\overline{2u}}b_{n,l+2u}.
 \tag{22}
$$


For (21), invert the upper triangular coefficient map
W=t^n(t-1)^nV. The coefficient of w_(2n+l) in V^(h)(1)/h!
is
sum_(r=h)^l binom(r,h)binom(n+l-r-1,l-r)=binom(n+l,n+h);
this follows by multiplying the generating series
t^h/(1-t)^(h+1) and (1-t)^(-n).
For (22), use the exact relation S=(1+t²)^n U and
S_(2n+l)=(n+l)!w_(2n+l), then replace its coefficient index
by n-u. These are the same reviewed upper-tail identities as in
raw_appell_minus_one_hook_and_endpoint_residue.md.

Put r=p-k-1, so n=(a-1)p+r. For 0<=h<=k, Lucas's theorem
in (21) leaves only l=vp+i with h<=i<=k and 0<=v<=a-1.
If i<h the low digit of n+l is too small. If i>=k+1,
addition carries and its low digit becomes i-k-1<r+h, again
making the binomial zero. On the surviving indices,


$$
\binom{n+l}{n+h}\equiv
    \binom{a+v-1}{a-1}\binom{r+i}{r+h}\pmod p.
 \tag{23}
$$


The high binomial here is an ordinary integer binomial; this formula
does not require a<p.

For surviving i, the first multiple of p among n+l+1,n+l+2,...
occurs in position k-i+1. Thus (22) leaves only 2u<=k-i.
In particular l+2u has residue i+2u<=k, so (20) applies to
every surviving input. Also


$$
\binom n{l+2u}\equiv\binom{a-1}v\binom r{i+2u},
 \qquad
 (-1)^{n-l-2u}=(-1)^{a-1-v}(-1)^{k-i}.             \tag{24}
$$


The second equality uses that p is odd and r has parity k.
All upper-tail indices are within 0,...,n because
(a-1)p+k<n.

The high-digit dependence now disappears by the exact finite difference


$$
\sum_{v=0}^{a-1}(-1)^{a-1-v}
       \binom{a-1}v\binom{a+v-1}{a-1}=1.           \tag{25}
$$


For example, the second binomial as a polynomial in v has degree a-1
and leading coefficient 1/(a-1)!, so its (a-1)-st forward
difference is one. This identity is over Z; it introduces no division
in the reduction modulo p.

In the remaining small factors, replace r by b modulo p:
binom(r+i,r+h)=binom(r+i,i-h) reduces to binom(b+i,i-h),
binom(n,u) to binom(b,u), and the rising factorial to
(b+i+1) rising (2u). All binomial bottom indices are at most k<p.
Equations (20)-(25) give exactly (3) and (6), including the factor h!.

## 6. The actual exponential border and reduced denominator

The exact endpoint identity, with its sign as independently corrected, is


$$
Pe_n(1)=\sum_{r=0}^n V_{n,r}D_{n,r},\qquad
 D_{n,r}=\sum_{s=0}^{n+r}\binom{n+s}s(n+r)_{\underline s}.
 \tag{26}
$$


There is no outside (-1)^n factor. Every term with s>=p vanishes
modulo p through the falling factorial. For s<p,


$$
\binom{n+s}s\equiv\binom{b+s}s
                =(-1)^s\binom ks\pmod p.
 \tag{27}
$$


It vanishes when k<s<p. Thus the endpoint border is, modulo p,
a polynomial of degree at most k in its coefficient index r:


$$
D_{n,r}\equiv
       \sum_{s=0}^k(-1)^s\binom ks(r+b)_{\underline s}.
 \tag{28}
$$


Use the falling-factorial Vandermonde identity
(r+b) falling s = sum_(h=0)^s binom(s,h)
b falling (s-h) r falling h. Summing against V_(n,r)
turns r falling h into V_n^(h)(1), and yields


$$
Pe_n(1)\equiv\sum_{h=0}^k A_{k,h}V_n^{(h)}(1)\pmod p.
 \tag{29}
$$


Together with (6), this proves (7).

The globally reviewed factorial integrality is
n! divides content U_n and content Qhat_n, so n! divides Z_n.
It also gives


$$
v_p(Pa_n(1))\ge v_p(n!)-\lfloor\log_p(2n)\rfloor.
 \tag{30}
$$


Under (8), (7) makes Pe_n(1) a unit and (30) makes Pa_n(1)
divisible by p. Therefore the actual numerator Pe_n(1)+4Pa_n(1)
is a unit. Reducing that numerator over Z_n proves (9).
No assertion about a different cofactor denominator is substituted here.

## 7. The two predeclared fixed symbolic seeds

These calculations use only the small Wronskians (11), not actual
canonical solves at degrees n=p-k-1.

For k=1, b=-2,


$$
D_1^-(x)=x^2+4,\quad
 C_{1,0}^-(x)=x^2-4,\quad C_{1,1}^-(x)=x.
$$


Consequently


$$
D=5,\quad (C_0,C_1)=(-3,1),\quad
 (J_{1,0},J_{1,1})=(5,-2),\quad
 (A_{1,0},A_{1,1})=(3,-1),\quad {\cal E}_1^-=17.
 \tag{31}
$$


Thus for every prime p>3 other than 5, and every n congruent to -2,
Pe_n(1)/V_n(1) is congruent to 17/5 modulo p.
Prime 17 is an actual exponential-numerator exception in this class.
Prime 5 is instead a zero determinant seed, and the argument makes
no primitive-unit conclusion there.

Root separately predeclared k=2 to settle the missing negative residue
at p=7. Direct evaluation gives


$$
D_2^-(x)=x^6+18x^4+432x^2-1296,
$$




$$
(C_{2,0}^-,C_{2,1}^-,C_{2,2}^-)
 =(x^6-18x^4+216x^2+2592,\ x^5-12x^3+72x,\ x^4+108).
$$


At x=1,


$$
D=-845,\quad(C_0,C_1,C_2)=(2791,61,109),
$$




$$
(J_{2,0},J_{2,1},J_{2,2})=(-845,-471,1308),\quad
 (A_{2,0},A_{2,1},A_{2,2})=(19,-8,1),\quad
 {\cal E}_2^-=-10979.
 \tag{32}
$$


Modulo 7 these are D=2 and E=4, both units. Therefore


$$
\boxed{Pe_n(1)/V_n(1)\equiv2\pmod7
          \quad\hbox{for every }n\equiv4\pmod7.}    \tag{33}
$$


With the threshold (8), the actual denominator has the factorial
7-adic lower bound on the whole class. Combining this with other
residue classes requires their separate reviewed theorems.

The exact symbolic checker is
check_negative_residue_fixed_seeds.py, with output
raw_negative_residue_fixed_seed_checks.json. It checks only k=1,2,
the displayed Wronskians and the finite integer formulas (3)-(4).
It does not certify the all-index proof by finite testing.

## 8. Precise remaining arithmetic scope

The reduction is uniform in the number a of prime blocks. Its input
is a fixed small partition and a fixed negative integer background.
Only k+1 residue classes of the primitive b-vector are needed, because
Lucas and the factorial upper-tail map discard every other class
before any endpoint evaluation.

This is a prime-level theorem. It does not compute a higher valuation
when D or E is divisible by p. In particular a zero E with unit D
is a concrete, actual endpoint obstruction, not proof of a large
common endpoint gcd or of a small reduced denominator.
No claim about irrationality of e+pi follows.
