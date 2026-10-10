> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 308 — all-$s$ fixed divisors for the pinned $j=1$ orbit and the height-information no-go

Date: 2026-08-31

## 1. Outcome and capacity first

Let



$$
p=4h+6s+3,\qquad h,s\geq1,\qquad p\text{ prime}.          \tag{1.1}
$$



This item extends Item 307's Frobenius calculation from the three
coefficient-singular rays to **every** positive integer $s$.  It proves an
exact parity residue



$$
\boxed{c_h^*\equiv \Lambda_s^{-1}
       \bigl(a_s+b_{s,\epsilon}w_h\bigr)\pmod p},
 \qquad
 w_h=(-1)^{\lfloor h/2\rfloor}2^h,\quad \epsilon=h\bmod2,  \tag{1.2}
$$



where $a_s,b_{s,\epsilon}$ are explicit integers given by the coefficient
formulas in Section 4 and



$$
\Lambda_s=3\,2^{10s+10}.           \tag{1.3}
$$



The clearing factor is a $p$-unit on every actual row.  Euler's criterion
then gives the all-$s$ necessary container



$$
\boxed{E_h^*\equiv0\pmod p\quad\Longrightarrow\quad
        p\mid D_{s,\epsilon}},\qquad
 D_{s,\epsilon}=2^{3s+1}a_s^2-
                 \delta_{s,\epsilon}b_{s,\epsilon}^2,     \tag{1.4}
$$



with



$$
\delta_{s,\epsilon}=(-1)^{s(s+1)/2+1+\epsilon}
                     =\left(\frac2p\right).               \tag{1.5}
$$



The formulas are symbolic for every $s$; the bounded rows in the
certificate are replay controls only.  No scan inference is used.

The admission audit is negative.  The rational source has denominator
degree $6s+8$, the coefficient extractions have order $O(s)$, and



$$
\log\max\{1,|a_s|,|b_{s,0}|,|b_{s,1}|,
                 |D_{s,0}|,|D_{s,1}|\}=O(s).              \tag{1.6}
$$



At fixed $M$, however, there are $\asymp M$ different containers, one
for each moving $s$.  Their product has only the unusable bound
$\exp(O(M^2))$.  More decisively, Section 8 constructs fixed-in-$s$
comparison containers of the same linear-height and quadratic-norm type
which permit candidate-prime mass arbitrarily close to the complete raw
mass $M/6$.  Therefore existence of (1.4), quadratic-norm factorization,
and linear logarithmic height **alone** cannot certify any strict reduction
of the raw $1/36$-per-$6M$ ceiling.

This is an information-class no-go, not a counterexample to the actual
$E_h^*$ sequence.  A factor localization, common recurrence with genuine
horizontal force, or weighted theorem for the exact $D_{s,\epsilon}$
could still close the cell.  None is proved here.  Hence



$$
\boxed{\text{new linear log rate}=0,\qquad
        \text{new fixed-}j=1\text{ capacity reduction}=0.} \tag{1.7}
$$



## 2. Bridge to the actual pinned ordinary gate

Let $\sigma$ be Item 222's ordinary row parameter and
$\sigma_*=-(4h+3)/6$.  On every actual row (1.1),



$$
6(s-\sigma_*)=p.                  \tag{2.1}
$$



Also $p\equiv h\pmod3$ and $p>3$, so every actual prime row has
$3\nmid h$, as required by the two gauge progressions.

Item 222's ordinary denominators are $p$-units, and an ordinary
fixed-$j=1$ collision forces $E_h(s)\equiv0\pmod p$.  Thus



$$
E_h(s)\equiv E_h(\sigma_*)=E_h^*\pmod p. \tag{2.2}
$$



The all-$h$ gauge proved in Item 243 is



$$
c_h^*=\mathcal G_hE_h^*,                                  \tag{2.3}
$$



where



$$
\mathcal G_1=-\frac{49}{18},\qquad
\mathcal G_2=\frac{4235}{1944},\qquad
\frac{\mathcal G_{u+3}}{\mathcal G_u}=
\frac{u(4u+1)(4u+5)(4u+7)(4u+9)(4u+11)(4u+15)^2}
{864(u+1)(u+2)(2u+1)^2(2u+3)(2u+5)^2(4u+3)}.              \tag{2.4}
$$



For every step $u\leq h-3$, every nonzero linear factor in (2.4) is at
most $4h+3$.  The two bases and 864 have prime support at most 11, while



$$
p=4h+6s+3\geq4h+9>4h+3.           \tag{2.5}
$$



Consequently $\mathcal G_h\in\mathbb F_p^\times$ on every actual row, not
only on the three structural rays.  Equations (2.2)--(2.5) give



$$
\text{ordinary collision}\Longrightarrow E_h^*\equiv0
 \Longleftrightarrow c_h^*\equiv0\pmod p.                 \tag{2.6}
$$



Only the necessary implication from the original collision is used.

## 3. The all-$s$ rational source

Item 237 proves, with



$$
Q(y)=1+y+y^2/2,\quad
 A(y)=(20+14y+4y^2)/3,\quad B(y)=2-5y-3y^2,
$$



that



$$
c_h^*=[y^{2h}](1+y)^{-2h-1}Q(y)^{(4h+3)/3}
                         (hA(y)+B(y)).                     \tag{3.1}
$$



Since $(4h+3)/3=p/3-2s$, put $R(y)=Q(y)^{1/3}$, with constant
term one.  In characteristic $p>3$,



$$
Q(y)^{p/3}=R(y)^p=R(y^p).                                \tag{3.2}
$$



Because $2h<p$, only the constant term of $R(y^p)$ reaches the target
coefficient.  With $n=2h$, $t=y/(1+y)$,



$$
D(t)=t^2-2t+2,\quad
 R_1(t)=\frac{10-13t+5t^2}{3},\quad R_0(t)=2-9t+4t^2,
$$



residue substitution, a second Frobenius reduction, and
$n[t^n]F=[t^n]tF'$ give



$$
c_h^*\equiv2^{2s}[t^{2h}]G_s(t)\pmod p, \tag{3.3}
$$



where



$$
G_s(t)=\frac{N_s(t)}{(1-t)^{2s+6}D(t)^{2s+1}},            \tag{3.4}
$$



and the numerator is the degree-five polynomial



$$
\begin{aligned}
3N_s(t)={}&12+(80s-4)t-(224s+8)t^2+(256s+16)t^3\\
          &-(138s+9)t^4+(30s+3)t^5.                       \tag{3.5}
\end{aligned}
$$



Equations (3.3)--(3.5) hold for every $s\geq1$.  The denominator degree
is exactly



$$
(2s+6)+2(2s+1)=6s+8.                  \tag{3.6}
$$



## 4. Exact coefficient definitions for $a_s,b_{s,\epsilon}$

Put



$$
\lambda=\frac{1+i}{2},\qquad r=2s+6,\qquad q=2s+1,
 \qquad \nu_s=3s+\frac12.                                 \tag{4.1}
$$



Define the rational and Gaussian-rational coefficients



$$
\boxed{
 A_s=-[x^{2s+5}]
 \frac{(1+x)^{\nu_s}N_s(1+x)}{(1+x^2)^q}}                 \tag{4.2}
$$



and



$$
\boxed{
 B_s=U_s+iV_s=[x^{2s}]
 \frac{(1+x)^{\nu_s}N_s((1-i)(1+x))}
 {2^q i^r(1+i)^q(1+(1+i)x)^r(1+\lambda x)^q}.}            \tag{4.3}
$$



All series in (4.2)--(4.3) are needed only through the displayed finite
coefficient.  Now set



$$
X_s=2^{2s}A_s,\qquad
 Y_{s,0}=\delta_{s,0}2^{5s+2}U_s,\qquad
 Y_{s,1}=-\delta_{s,1}2^{5s+2}V_s,                         \tag{4.4}
$$



and use the explicit clearing (1.3):



$$
a_s=\Lambda_sX_s,\qquad b_{s,\epsilon}=\Lambda_sY_{s,\epsilon}. \tag{4.5}
$$



These are the promised exact definitions.  Section 6 proves that every
quantity in (4.5) is an integer and that $\Lambda_s$ is a $p$-unit.

## 5. Proof of the all-$s$ parity residue

Factor



$$
D(t)=2(1-\lambda t)(1-\bar\lambda t).                    \tag{5.1}
$$



The unique partial fractions of (3.4) give



$$
[t^n]G_s(t)=\mathcal A_s(n)+
             2\operatorname {Re}(\mathcal B_s(n)\lambda^n), \tag{5.2}
$$



where $\mathcal A_s$ and $\mathcal B_s$ are binomial polynomials of
degrees at most $2s+5$ and $2s$, respectively.  On (1.1),



$$
n=2h\equiv n_s:=-\frac{6s+3}{2}\pmod p. \tag{5.3}
$$



Every factorial in these binomial polynomials is below $p$, because
$p\geq6s+7>2s+5$.  The pole constants have denominators supported at
2 and 3.  Thus substitution in (5.3) is legitimate.

Here is the symbolic evaluation, avoiding an $O(s)$-sized partial
fraction table.  At $t=1$, write $z=1-t$.  Then



$$
z^rG_s(1-z)=\frac{N_s(1-z)}{(1+z^2)^q}=:H_1(z).           \tag{5.4}
$$



If $H_1(z)=\sum h_jz^j$, the coefficient of $(1-t)^{-k}$ is
$h_{r-k}$.  With $m=r-1=2s+5$, the negative-binomial identity gives



$$
{n_s+r-j-1\choose r-j-1}
 =-(-1)^j{3s+1/2\choose m-j}.                              \tag{5.5}
$$



Summing (5.5) is exactly (4.2), so $\mathcal A_s(n_s)=A_s$.

At the Gaussian pole $t=\lambda^{-1}=1-i$, put $z=1-\lambda t$.
Direct substitution gives



$$
z^qG_s((1-z)/\lambda)=
 \frac{N_s((1-i)(1-z))}
 {2^q i^r(1+i)^q(1-(1+i)z)^r(1-\lambda z)^q}
 =:H_\lambda(z).                                           \tag{5.6}
$$



Now $q-1=2s$ is even, and the same identity yields



$$
{n_s+q-j-1\choose q-j-1}
 =(-1)^j{3s+1/2\choose 2s-j}.                              \tag{5.7}
$$



Therefore



$$
\mathcal B_s(n_s)=[x^{2s}](1+x)^{3s+1/2}H_\lambda(-x)=B_s, \tag{5.8}
$$



which is (4.3).  This proves (4.2)--(4.3) symbolically for every $s$,
not by checking finitely many values.

It remains to specialize $\lambda^{2h}$.  Since



$$
2^{2h+3s+1}=2^{(p-1)/2}\equiv\delta_{s,\epsilon}\pmod p, \tag{5.9}
$$



Euler's criterion gives



$$
2^{3s+1}w_h^2\equiv\delta_{s,\epsilon}\pmod p            \tag{5.10}
$$



and



$$
\lambda^{2h}=(i/2)^h\equiv
 \begin{cases}
 \delta_{s,0}2^{3s+1}w_h,&\epsilon=0,\\
 i\delta_{s,1}2^{3s+1}w_h,&\epsilon=1.
 \end{cases}                                               \tag{5.11}
$$



Substituting (5.8)--(5.11) into (3.3) proves



$$
c_h^*\equiv X_s+Y_{s,\epsilon}w_h
 \equiv\Lambda_s^{-1}(a_s+b_{s,\epsilon}w_h)\pmod p,      \tag{5.12}
$$



which is (1.2).  Squaring a vanishing linear form and using (5.10)
proves (1.4).

## 6. Denominator prime support and the $p$-unit audit

For integer $u\geq0$, the coefficients of
$(1+x)^{u+1/2}=(1+x)^u(1+x)^{1/2}$ through degree $m$ have denominators
dividing $2^{2m}$.  Also



$$
(1+x^2)^{-q}\in\mathbb Z[[x]],\qquad
 N_s(t)\in\tfrac13\mathbb Z[t].                            \tag{6.1}
$$



Consequently (4.2), through degree $2s+5$, has denominator dividing



$$
3\,2^{4s+10}.                     \tag{6.2}
$$



For (4.3), the half-binomial part contributes at most $2^{4s}$.  The
constant satisfies



$$
\frac1{2^q i^r(1+i)^q}
       =\frac{i^{-r}(1-i)^q}{2^{2q}},                      \tag{6.3}
$$



so contributes at most $2^{4s+2}$.  The coefficients through degree
$2s$ of $(1+\lambda x)^{-q}$ contribute at most $2^{2s}$, while
$(1+(1+i)x)^{-r}\in\mathbb Z[i][[x]]$.  Including the single factor 3
from $N_s$,



$$
B_s\in
 \frac1{3\,2^{10s+2}}\mathbb Z[i].                         \tag{6.4}
$$



Equations (6.2)--(6.4) prove (4.5) is integral for the conservative
choice $\Lambda_s=3\,2^{10s+10}$.  In particular, the complete prime
support of the clearing denominator is



$$
\operatorname {supp}(\Lambda_s)=\{2,3\}. \tag{6.5}
$$



Every actual prime in (1.1) is at least 13.  Thus $\Lambda_s$ is a
$p$-unit for every actual row.  This audit is uniform in $s$; no hidden
factorial prime or row-dependent denominator has been discarded.

The integer $D_{s,\epsilon}$ itself has no proved rational-prime
localization.  Only its total height is controlled below.

## 7. Exact sign cases, norm identity, and height

The Euler sign and parity parameter are



$$
\begin{array}{c|cc|c}
s\bmod4&\delta_{s,0}&\delta_{s,1}&\eta_s\\ \hline
0&-1&+1&2\\
1&+1&-1&1\\
2&+1&-1&2\\
3&-1&+1&1,
\end{array}
\qquad
\eta_s=2^{(3s+1)-2\lfloor(3s+1)/2\rfloor}
=\begin{cases}1,&s\text{ odd},\\2,&s\text{ even}.
\end{cases}                                                \tag{7.1}
$$



Let



$$
k_s=\lfloor(3s+1)/2\rfloor,\qquad z_s=2^{k_s}a_s,
 \qquad
 K_{s,\epsilon}=\mathbb Q[T]/(T^2-\delta_{s,\epsilon}\eta_s),
 \quad\theta=T\bmod(T^2-\delta_{s,\epsilon}\eta_s).        \tag{7.2}
$$



Then the container has the uniform quadratic-norm form



$$
\boxed{
 D_{s,\epsilon}=\eta_sz_s^2-\delta_{s,\epsilon}b_{s,\epsilon}^2
 =-\delta_{s,\epsilon}
   \operatorname N_{K_{s,\epsilon}/\mathbb Q}
   \bigl(b_{s,\epsilon}+z_s\theta\bigr).}                  \tag{7.3}
$$



When $s$ is odd and $\delta=+1$, $K_{s,\epsilon}$ is the split
quadratic algebra and (7.3) is the integer factorization



$$
D=(z-b)(z+b).                     \tag{7.4}
$$



The other three cases are norms from $\mathbb Q(i)$,
$\mathbb Q(\sqrt2)$, or $\mathbb Q(\sqrt{-2})$, with the sign shown
in (7.3).  This is a genuine uniform factorization, but it does not bound
the rational prime factors.  Item 307's exact $(s,\epsilon,p)=(2,0,47)$
witness already has $47\mid D_{2,0}$, despite the minimum actual prime
on that ray being $6s+7=19$.  No finite factor list is used here.

For completeness, (1.6) follows directly from the finite coefficient
formulas.  Through the required ranges,



$$
\sum_k\left|{3s+1/2\choose k}\right|\leq e^{3s+1}.        \tag{7.5}
$$



The shifted degree-five polynomial $N_s$ has coefficient $\ell^1$-norm
$O(s+1)$.  The relevant coefficients of $(1+x^2)^{-q}$ have total
absolute value at most $2^{3s+3}$.  For (4.3), the two inverse-linear
series have truncated $\ell^1$-norm $\exp(O(s))$; this follows from
${r+k-1\choose k}\leq2^{r+k-1}$, $|1+i|=\sqrt2$, and
$|\lambda|=2^{-1/2}$.  Hence



$$
|A_s|+|B_s|\leq\exp(O(s)).         \tag{7.6}
$$



Multiplication by the powers of 2 in (4.4) and by $\Lambda_s$ preserves
an exponential bound.  Finally (1.4) proves



$$
\log\max\{1,|a_s|,|b_{s,0}|,|b_{s,1}|,
                 |D_{s,0}|,|D_{s,1}|\}=O(s),              \tag{7.7}
$$



with an absolute implied constant.  This proves the claimed height audit.
It does not prove $D_{s,\epsilon}\ne0$ for all $s$, and no such claim
is needed for the no-go: a zero container is weaker still.

## 8. Decisive scoped no-go for the height-only extension

Item 264's exact fixed-$M$ indexing is



$$
\mathcal S_M=\{s\geq1:4s\leq M-5,\ s\equiv M+1\pmod3\},
\quad
 p_s=\frac{4M+2s+1}{3},\quad
 h_s=\frac{M-4s-2}{3}.                                    \tag{8.1}
$$



The map $s\mapsto p_s$ is a bijection from prime candidates in
$\mathcal S_M$ to primes in



$$
\frac{4M+3}{3}\leq p\leq\frac{3M-1}{2},      \tag{8.2}
$$



whose logarithmic mass is $M/6+o(M)$.

First, direct product height already fails.  Since
$|\mathcal S_M|=M/12+O(1)$ and $s\leq M/4$, (7.7) gives only



$$
\log\prod_{s\in\mathcal S_M}\prod_{\epsilon=0}^1
          \max(1,|D_{s,\epsilon}|)=O(M^2),                 \tag{8.3}
$$



far above the raw $O(M)$ support.  Taking the minimum of (8.3) and the
raw bound simply returns the raw bound.

The limitation is logical, not merely a loose summation.  Fix any
$0<\rho<1/4$ and define a sequence independent of $M$:



$$
P_s^{(\rho)}=\prod_{\substack{q\leq 2s/\rho\\q\text{ prime}}}q,
 \qquad
 \widetilde a_{s,\epsilon}=\widetilde b_{s,\epsilon}
 =P_s^{(\rho)}.                                            \tag{8.4}
$$



Chebyshev's estimate gives



$$
\log P_s^{(\rho)}=O_\rho(s).                              \tag{8.5}
$$



These are integer, fixed-in-$s$, denominator-free linear forms.  Their
containers



$$
\widetilde D_{s,\epsilon}
 =(P_s^{(\rho)})^2
  \bigl(2^{3s+1}-\delta_{s,\epsilon}\bigr)                 \tag{8.6}
$$



have exactly the same quadratic-norm shape as (7.3), are nonzero, and have
$\log|\widetilde D|=O_\rho(s)$.

Now take an actual fixed-$M$ candidate with $s\geq\rho M$.  Equation
(8.1) gives



$$
p_s\leq\frac{3M-1}{2}<\frac{2s}{\rho}.                   \tag{8.7}
$$



Thus $p_s\mid P_s^{(\rho)}$.  In particular both the comparison linear
form and its norm container vanish modulo every candidate prime in this
slice.  The slice corresponds, up to endpoint errors, to



$$
\left(\frac43+\frac{2\rho}{3}\right)M
 \leq p\leq\frac32M,                                      \tag{8.8}
$$



so the prime number theorem gives retained logarithmic mass



$$
\left(\frac16-\frac{2\rho}{3}\right)M+o(M),              \tag{8.9}
$$



or



$$
\frac1{36}-\frac{\rho}{9}+o(1)                           \tag{8.10}
$$



per $6M$.  Since $\rho$ may be arbitrarily small, no bound with a
strict coefficient below $1/6$, equivalently below $1/36$ per $6M$,
can follow uniformly from the following information alone:

- one fixed integer linear form and one necessary divisor for each $s$;
- a clearing denominator supported at 2 and 3;
- the quadratic-norm identity (7.3); and
- $\log|D_{s,\epsilon}|=O(s)$, with no prime-factor localization.

The comparison family (8.4) is **not** the actual $E_h^*$ sequence and
does not disprove a sequence-specific theorem.  It proves only that the
natural fixed-divisor/absolute-height information class cannot pass the
Item 264 admission threshold.  Special factorization of the exact
coefficients, an arithmetic recurrence that restricts their moving prime
factors, or direct weighted cancellation remains admissible.

## 9. Coverage, open target, and strict labels

Unlike Item 307, the residue theorem (1.2) covers every $s\geq1$, hence
the entire fixed-$j=1$ cell at the level of the sole pinned necessary
gate.  It retains the actual fixed-$M$ indexing and does not replace it
by a varying-$h$ ray count.

Removing $s=2,4,6$ changes fixed-$M$ support by only $O(\log M)$.
The live actual target is still



$$
\mathcal W_{\rm off}(M)=
 \sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                  p_s\text{ prime}\\
                  p_s\mid N_E(h_s)}}\log p_s=o(M).         \tag{9.1}
$$



For the new container extension, a sufficient sequence-specific lemma is



$$
\boxed{
 \mathcal W_D(M)=
 \sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                  p_s\text{ prime}\\
                  p_s\mid D_{s,h_s\bmod2}}}\log p_s=o(M).} \tag{9.2}
$$



Divisibility by zero is understood in the usual sense, so an identically
zero row would be included and would have to be controlled.  Equation
(1.4) gives $\mathcal W_{\rm off}(M)\leq\mathcal W_D(M)$.  Proving (9.2)
requires genuine prime localization or weighted arithmetic of the exact
coefficient sequence; (7.7) alone cannot do it.

- **PROVED:** the all-$s$ rational reduction (3.3)--(3.5), coefficient
  formulas (4.2)--(4.5), parity residue (5.12), denominator support, norm
  identity, linear logarithmic height, and the information-class no-go.
- **OPEN:** (9.1), (9.2), uniform nonzero/factor localization for the exact
  $D_{s,\epsilon}$, the full fixed-$j=1$ closer, Route 1, and every
  conclusion about $e+\pi$.
- **NOT CLAIMED:** a recurrence forcing $o(M)$, a complete factorization,
  a prime scan, universal nonvanishing, or positive capacity.

No canonical file is edited by this research package.

## 10. Deterministic replay

From the archive root, run

~~~text
python work/item308_j1_all_s_fixed_divisor_no_go_certificate.py --output work/item308_j1_all_s_fixed_divisor_no_go_certificate.replay.json
~~~

The checker uses standard-library exact rational and Gaussian-rational
arithmetic.  It pins the upstream formulas; constructs (3.4)--(3.5);
evaluates (4.2)--(4.3) directly; independently evaluates the exact partial
fractions on a fixed bounded list; checks integrality, Euler signs, norm
identities, denominator support, and preselected residue controls; and emits
the fixed-$M$ comparison inequalities.  The finite controls are explicitly
labeled as replay only.  It performs no factorization and no prime scan.
