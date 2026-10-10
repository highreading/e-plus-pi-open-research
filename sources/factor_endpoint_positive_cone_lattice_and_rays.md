> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The factor-endpoint positive cone: exact lattice image and changing primitive rays

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
A(F)=\sum_{j\geq0}(-1)^jF^{(j)}(1),\qquad
 B(F)=\sum_{j\geq0}(-1)^jF^{(j)}(0),
 \tag{1}
$$



and consider the restricted common-kernel cone



$$
F=(1-x)^2H,\qquad H\in\mathbb Z[x],\qquad H\geq0\quad(0\leq x\leq1),
 \tag{2}
$$



with



$$
A(F)=F(i)=F(-i)=a.
 \tag{3}
$$



This branch gives three exact structural results.

First, for $\deg H\leq7$, the full unconstrained integer image in the
coordinates



$$
(a,B,I),\qquad
 I=4\int_0^1\frac{F-a}{1+x^2}\,dx,
 \tag{4}
$$



is



$$
\boxed{4\mathbb Z\times\mathbb Z\times\frac1{210}\mathbb Z.}
 \tag{5}
$$



Thus this factor class forces $4\mid a$, but already in degree seven
there is no further congruence coupling the three output coordinates.

Second, an exact nonnegative Bernstein construction produces fourteen
different fully primitive rays



$$
(q,-p)
 \tag{6}
$$



realized by primitive integer polynomials satisfying (2)--(3). Their
positive primitive forms $q(e+\pi)-p$ decrease strictly from



$$
7(e+\pi)-41=0.0191213743\ldots
 \tag{7}
$$



to



$$
\boxed{
 1246188493618(e+\pi)-7302508153575
 =3.273998315\ldots\,10^{-13}.}
 \tag{8}
$$



The polynomials themselves are primitive, while their exact output
cross-contents have as many as 114 decimal digits. Hence exceptional
cross-content is compatible not only with one fixed ray, but with many
genuinely changing rays close to the boundary of the positive half-plane.

Third, there is an all-parameter primitive positive family with genuinely
changing rays



$$
(16n+4,-85n),\qquad n\equiv3\pmod {170}.
 \tag{9}
$$



Its cross-content can be multiplied by an arbitrary parameter while the
polynomial remains primitive. However, its primitive value is



$$
n\{16(e+\pi)-85\}+4(e+\pi),
 \tag{10}
$$



which grows rather than shrinks.

These are constructive advances and an exact image theorem, but they do
**not** prove that $e+\pi$ is irrational or transcendental. The fourteen
small forms are a finite list. Extending a finite list of continued-fraction
type rays to an infinite shrinking sequence would already contain the
unresolved irrationality step; that extension is not assumed here.

## 2. Exact output identities

Repeated integration by parts gives



$$
\int_0^1e^xF(x)\,dx=eA(F)-B(F).
 \tag{11}
$$



If (3) holds, then



$$
G=\frac{F-a}{1+x^2}\in\mathbb Z[x]
 \tag{12}
$$



and



$$
\begin{aligned}
 L(F)
 &:=
 \int_0^1F(x)\left(e^x+\frac4{1+x^2}\right)dx\\
 &=a(e+\pi)-B(F)+4\int_0^1G(x)\,dx.
 \end{aligned}
 \tag{13}
$$



Write



$$
I=4\int_0^1G=\frac MD,\qquad D>0,\qquad (M,D)=1,
 \tag{14}
$$



and put



$$
N=M-BD,\qquad g=(aD,N).
 \tag{15}
$$



The fully primitive positive form is therefore



$$
\boxed{
 \Lambda_F=\frac{aD}{g}(e+\pi)+\frac Ng=\frac DgL(F)>0.}
 \tag{16}
$$



No numerical approximation is used in obtaining (11)--(16).

## 3. The factor-endpoint lattice

Let



$$
f_k=x^k(1-x)^2,
 \qquad
 u_k=A(x^k)=(-1)^k!k,
 \tag{17}
$$



where $!k$ is the derangement number. The recurrence



$$
u_{k+1}=1-(k+1)u_k
 \tag{18}
$$



gives



$$
\boxed{
 A(f_k)=(k^2+5k+5)u_k-(k+3),}
 \tag{19}
$$



and direct evaluation at zero gives



$$
\boxed{
 B(f_k)=(-1)^k(k^2+5k+5)k!.}
 \tag{20}
$$



Since



$$
F(i)=(1-i)^2H(i)=-2iH(i),
 \tag{21}
$$



the endpoint equations are



$$
\Re H(i)=0,\qquad a=2\Im H(i).
 \tag{22}
$$



Thus the real target contributed by $x^k$ in $H$ is



$$
a_k=
 \begin{cases}
 2,&k\equiv1\pmod4,\\
 -2,&k\equiv3\pmod4,\\
 0,&k\text{ even}.
 \end{cases}
 \tag{23}
$$



### 3.1 The target is always divisible by four

Modulo four, (18) gives the periodic pattern



$$
u_k\equiv1,0,1,2\pmod4
 \quad(k\equiv0,1,2,3\pmod4).
 \tag{24}
$$



Substitution in (19), together with (23), gives for every $k\geq0$



$$
A(f_k)-a_k\equiv2\pmod4.
 \tag{25}
$$



If $H=\sum h_kx^k$ satisfies the common equations, (25) implies



$$
\sum_kh_k\equiv0\pmod2.
 \tag{26}
$$



The first equation in (22) says



$$
\sum_{k\equiv0(4)}h_k=\sum_{k\equiv2(4)}h_k,
 \tag{27}
$$



so the sum of the even-index coefficients is even. Equations (26)--(27)
then show that the sum of the odd-index coefficients is even. Finally,



$$
\frac a2=\sum_{k\equiv1(4)}h_k-\sum_{k\equiv3(4)}h_k
 \tag{28}
$$



is even. Hence



$$
\boxed{4\mid a.}
 \tag{29}
$$



### 3.2 Exact degree-seven image

If $\deg H\leq7$, then $\deg G\leq7$. Since



$$
\operatorname {lcm}(1,2,\ldots,8)=840,
 \tag{30}
$$



we have $840\int_0^1G\in\mathbb Z$, and consequently



$$
I=4\int_0^1G\in\frac1{210}\mathbb Z.
 \tag{31}
$$



Also $B\in\mathbb Z$. Thus the image is contained in the lattice in
(5). Equality follows from the following three exact preimages:



$$
\begin{array}{c|rrrrrrrr|ccc}
 &h_0&h_1&h_2&h_3&h_4&h_5&h_6&h_7&a&B&I\\ \hline
H_A&-17&21&161&95&167&74&-11&-2&4&0&0\\
H_B&7&-26&2&-26&-5&0&0&0&0&1&0\\
H_P&11&-85&78&-13&66&71&-1&-1&0&0&1/210.
\end{array}
\tag{32}
$$



For each row, $(1-x)^2H$ satisfies both common equations. The three
rows generate every element of the ambient lattice in (5), proving the
claimed exact image.

There is also a strictly positive interior point



$$
H_*=3+8x+3x^2\geq3,
 \tag{33}
$$



whose data are



$$
(a,B,I)=(16,41,-44),\qquad c:=I-B=-85.
 \tag{34}
$$



The coefficient $\ell^1$-norms of $H_A,H_B,H_P$ are respectively
$548,66,326$. Therefore



$$
H=tH_*+rH_A+sH_B+uH_P>0\quad\hbox{on }[0,1]
 \tag{35}
$$



whenever



$$
3t>548|r|+66|s|+326|u|.
 \tag{36}
$$



Its exact image is



$$
(a,B,I)=(16t+4r,\ 41t+s,\ -44t+u/210).
 \tag{37}
$$



This proves that the positive image contains a full-dimensional rational
cone; it is not merely a single feasible ray.

## 4. Exact Bernstein interpolation onto prescribed primitive rays

For $0\leq j\leq m$, define the normalized Bernstein polynomial



$$
\beta_{m,j}(x)=\binom mjx^j(1-x)^{m-j}\geq0
 \quad(0\leq x\leq1).
 \tag{38}
$$



For a rational polynomial $H$, form the three linear coordinates



$$
\bigl(\Re H(i),\ A((1-x)^2H)-2\Im H(i),\ 2\Im H(i)\bigr).
 \tag{39}
$$



The first two must vanish, while the third is the target $a$. The
rational output



$$
c=-B+4\int_0^1\frac{(1-x)^2H-a}{1+x^2}\,dx
 \tag{40}
$$



is also linear on the constrained plane. For an individual unconstrained
Bernstein column, (40) is evaluated by taking the Euclidean quotient and
retaining the remainder separately; both operations are linear, and the
remainders cancel once (39) is imposed.

For every row of the table in Section 6, three indicated Bernstein columns
have exact nonnegative rational weights $w_1,w_2,w_3$ satisfying



$$
\sum_{r=1}^3w_r(\text{coordinates of }\beta_{m,j_r})=(0,0,1).
 \tag{41}
$$



Let $H_m=\sum_rw_r\beta_{m,j_r}$. Then



$$
H_m\geq0,\qquad a(H_m)=1,\qquad c(H_m)=\rho_m.
 \tag{42}
$$



All weights and every $\rho_m$ are exact fractions in the certificate.
For the corresponding coprime integers $p,q>0$, the exact inequalities



$$
\rho_m<-\frac pq<-\frac{85}{16}
 \tag{43}
$$



are checked by integer cross-multiplication.

Put



$$
\lambda=
 \frac{-85/16+p/q}{-85/16-\rho_m}\in(0,1)
 \tag{44}
$$



and



$$
\widehat H=(1-\lambda)\frac{H_*}{16}+\lambda H_m.
 \tag{45}
$$



Then



$$
a(\widehat H)=1,\qquad
 c(\widehat H)=-\frac pq,
 \tag{46}
$$



and, crucially,



$$
\widehat H\geq(1-\lambda)\frac3{16}>0
 \quad(0\leq x\leq1).
 \tag{47}
$$



Clear all monomial-coefficient denominators in $\widehat H$, and then
divide their common content. Call the resulting integer polynomial
$\overline H$, and let $S>0$ be the rational scaling factor such that
$\overline H=S\widehat H$. Equations (46)--(47) give



$$
\overline H\geq S(1-\lambda)\frac3{16}>0.
 \tag{48}
$$



Moreover, the fully primitive output ray of
$(1-x)^2\overline H$ is exactly



$$
\boxed{(q,-p).}
 \tag{49}
$$



This is an exact rational construction. The decimal values in Section 6
are not used to select signs or to certify positivity.

## 5. A monic zero-output direction and polynomial primitivity

The following degree-64 integer polynomial in the $H$-coordinate is used
for every finite witness:



$$
\begin{split}
 Z={}&-2+16x-12x^2-15x^3+3x^4-x^5-16x^6+11x^8-19x^9\\
 &+24x^{10}+14x^{11}-x^{12}-16x^{13}-16x^{14}-15x^{15}
 +3x^{16}-14x^{17}+5x^{18}-14x^{19}\\
 &+28x^{20}-15x^{21}+7x^{22}-40x^{23}+10x^{24}-14x^{25}
 +13x^{26}+14x^{27}+14x^{28}+14x^{29}\\
 &+14x^{30}+14x^{31}-19x^{32}+15x^{33}-19x^{34}+17x^{35}
 -19x^{36}+19x^{37}-19x^{38}+21x^{39}\\
 &+22x^{40}+22x^{41}-21x^{42}+23x^{43}-21x^{44}+25x^{45}
 -21x^{46}+27x^{47}-21x^{48}+29x^{49}\\
 &+30x^{50}+30x^{51}-23x^{52}+85x^{53}+31x^{54}+198x^{55}
 +27x^{56}+256x^{57}+20x^{58}\\
 &+256x^{59}+12x^{60}+194x^{61}+5x^{62}+66x^{63}+x^{64}.
\end{split}
\tag{50}
$$



Omitted powers in (50) have coefficient zero. Exact calculation gives



$$
\boxed{
 A((1-x)^2Z)=((1-x)^2Z)(i)=((1-x)^2Z)(-i)=0,}
 \tag{51}
$$



and separately



$$
B((1-x)^2Z)=0,\qquad
 4\int_0^1\frac{(1-x)^2Z}{1+x^2}\,dx=0.
 \tag{52}
$$



Also



$$
\sum_{k=0}^{64}|[x^k]Z|=2028,
 \tag{53}
$$



so $Z(x)\geq-2028$ on $[0,1]$. Its leading coefficient is one.

For every cleared witness in Section 4, the exact lower bound in (48) is
larger than $2028$; the smallest is already $273228$. Hence



$$
H^{\rm final}=\overline H+Z>0
 \quad(0\leq x\leq1).
 \tag{54}
$$



Because $\deg\overline H\leq63$, the polynomial



$$
F^{\rm final}=(1-x)^2H^{\rm final}
 \tag{55}
$$



has leading coefficient one and is therefore primitive in $\mathbb Z[x]$.
Equations (51)--(52) show that its endpoint and output data are unchanged.
Thus (49) is realized by a **primitive positive integer polynomial**, not by
trivially scaling a smaller polynomial.

The same direction also amplifies cross-content. If a base witness has
reduced correction denominator $D_0$, then for every positive integer
$t$ coprime to $D_0$,



$$
t\overline H+Z
 \tag{56}
$$



has the same primitive ray, remains primitive, is positive for all
sufficiently large $t$, and has cross-content exactly $t$ times the
base cross-content. Indeed, scaling by such a $t$ leaves $D_0$
unchanged and multiplies $a,M,B,N$ by $t$, while (51)--(52) add zero.

## 6. Fourteen changing primitive rays

The following table records the Bernstein degree, the fully primitive ray,
the number of decimal digits in the exact cross-content $g$, and a
rigorous outward-rounded upper endpoint for the positive primitive value.
Every final polynomial has degree 66 and leading coefficient one.



$$
\begin{array}{r|r|r|r|l}
m&q&p&\#\operatorname{digits}(g)&\text{upper bound for }q(e+\pi)-p\\ \hline
7&7&41&9&0.0191213743418693167605159824251576736810\\
15&157&920&22&0.0002936816676403902001441772499649668434\\
20&6851&40146&31&0.0000765165923841608992850849650317697074\\
24&27247&159664&38&0.0000123847018962533969961626101621119862\\
26&91939&538751&42&0.0000050881604448064398440266530515070980\\
30&405201&2374427&49&0.0000006713984315254052278080449333115175\\
35&4521903&26497784&57&0.0000000888412953325003537525371558218033\\
41&56602103&331681219&69&0.0000000063256883359957678520624182236460\\
43&180222349&1056080344&70&0.0000000024739436086863863760923071513064\\
45&484064944&2836559813&77&0.0000000010961424900633912762145032302731\\
49&2847787561&16687677659&84&0.0000000002511666043845798052246011579925\\
55&31933348361&187125413187&96&0.0000000000072304109843876577150048958501\\
61&557409702537&3266350891943&110&0.0000000000009488900344941074002850983790\\
63&1246188493618&7302508153575&114&0.0000000000003273998315148272218902473901.
\end{array}
\tag{57}
$$



The exact $D,M,N,g$, the three nonnegative Bernstein weights, the
interpolation parameter, coefficient hashes, and the lower positivity
margin are all included in the JSON certificate. The displayed decimal
intervals come from exact rational enclosures: a truncated positive series
with an explicit geometric tail bounds $e$, while Machin's identity



$$
\pi=16\arctan(1/5)-4\arctan(1/239)
 \tag{58}
$$



is bounded by the alternating-series remainder. Thus every decimal bound
in (57) is rigorous.

## 7. An infinite moving-ray, linear-content family

For $n\geq183$, put



$$
K_n=nH_*+H_A.
 \tag{59}
$$



Equations (32)--(34) give



$$
(a,B,I,c)(K_n)=(16n+4,\ 41n,\ -44n,\ -85n).
 \tag{60}
$$



Moreover,



$$
K_n(x)\geq3n-\|H_A\|_1=3n-548>0
 \quad(0\leq x\leq1).
 \tag{61}
$$



If



$$
n\equiv3\pmod {170},
 \tag{62}
$$



then $n$ is odd, $n\not\equiv1\pmod5$, and
$n\not\equiv4\pmod {17}$. Since



$$
\gcd(16n+4,85n)\mid340,
 \tag{63}
$$



these three exclusions give



$$
\gcd(16n+4,85n)=1.
 \tag{64}
$$



For positive integers $t$ satisfying



$$
t(3n-548)>2028,
 \tag{65}
$$



define



$$
F_{n,t}=(1-x)^2\{tK_n+Z\}.
 \tag{66}
$$



Equations (53), (61), and (65) prove positivity. The leading coefficient
is one, so $F_{n,t}$ is primitive. Its exact data are



$$
a=t(16n+4),\qquad B=41tn,\qquad I=-44tn,
 \tag{67}
$$



and, by (64),



$$
\boxed{
 g=t,\qquad
 (a/g,c/g)=(16n+4,-85n).}
 \tag{68}
$$



Thus both the primitive ray and the cross-content can vary without
introducing polynomial content. On the other hand, its primitive form is



$$
\Lambda_n=(16n+4)(e+\pi)-85n
 =n\{16(e+\pi)-85\}+4(e+\pi).
 \tag{69}
$$



The first brace is positive because it is the positive integral associated
with $H_*$. Hence (69) grows linearly. This family defeats a
fixed-ray-only interpretation of large content, but it is deliberately
recorded as a nonshrinking barrier example.

## 8. What this resolves and what it does not

The exact image theorem (5) rules out a hidden low-degree congruence as the
explanation for the difficulty. The constructions in Sections 4--6 prove
that positivity, polynomial primitivity, changing approximant rays, and
very large cross-content can coexist. In particular, a proposed universal
upper bound on cross-content based only on polynomial content or on a fixed
ray is false in this factor-endpoint class.

What remains is genuinely all-degree and arithmetic. A proof of
irrationality through this cone would require infinitely many primitive
rays $(q_n,-p_n)$ with



$$
0<q_n(e+\pi)-p_n\longrightarrow0.
 \tag{70}
$$



The finite table (57), however small its last entry, does not imply (70).
Nor may one assume an infinite continued fraction for $e+\pi$, because
that assumption is equivalent to already knowing irrationality. The exact
Bernstein denominators also grow very rapidly; generic continuous cone
convergence does not control primitive arithmetic after clearing.

Accordingly this package supplies a rigorous constructive branch and a
sharper description of the surviving synchronization problem. It does not
claim an irrationality or transcendence proof.

## 9. Deterministic certificate

Run

    python -m py_compile scripts/factor_endpoint_positive_cone_rays_certificate.py
    python scripts/factor_endpoint_positive_cone_rays_certificate.py

The script writes

    results/factor_endpoint_positive_cone_rays_certificate.json

using only the Python standard library. It verifies all endpoint and
output identities, the three degree-seven image generators, the zero-output
direction, every exact Bernstein weight and interpolation, denominator
clearing, cross-content, strict positivity margin, polynomial primitivity,
and the rational enclosures used in (57).
