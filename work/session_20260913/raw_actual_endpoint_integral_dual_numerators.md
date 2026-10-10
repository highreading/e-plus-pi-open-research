> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual selected type-I endpoint from integral dual numerators

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review passed: raw_actual_endpoint_integral_numerators_independent_review.md.

This note proves an exact global bridge from the primitive simultaneous polynomial to the actual selected rational approximation. Let $q_n$ be the positive reduced denominator of the actual canonical $A_n(1)$, with $B_n(1)=1,\ C_n(1)=4$. Then


$$
\boxed{
A_n(1)=-\frac{N_n}{Z_n},\qquad
N_n\in\mathbb Z,\qquad
q_n=\frac{|Z_n|}{\gcd(|Z_n|,|N_n|)}\mid |Z_n|.
}
\tag{1}
$$


The numerator is explicitly the sum of the two simultaneous Taylor numerators at 1. No denominator for all coefficients of the type-I triple is identified with the simultaneous denominator.

More strongly, on the saturated family


$$
n=mp^\nu,\quad p\ {\rm odd},\quad \nu\ge1,\quad3m<p,\quad n>p,
$$


the numerator $N_n$ is a $p$-adic unit. Hence the exact actual denominator valuation is


$$
\boxed{
v_p(q_n)=v_p(Z_n)
=\frac{n-m}{p-1}+v_p(d_n^{II}).
}
\tag{2}
$$


Here $d_n^{II}$ is the least positive coefficient denominator of the actual normalized simultaneous polynomial. Its unitness does not imply unitness of $q_n$; (2) provides infinitely many actual counterexamples to that implication.

## 1. Exact normalization and archive comparison

Use the already independently reviewed raw_extremal_dual_polynomial_and_content_identity.md. The integer extremal matrix $X_n$ has rows $k=n,\ldots,3n$, columns $B_j,C_j$, $0\le j<n$, and entries


$$
(k)_j,\qquad k!\tau_{k-j},\qquad
\tau_r=[z^r]\arctan z.
$$


Its fixed signed maximal cofactors and their primitive quotient are


$$
u_k=(-1)^{k-n}\det X_n[\widehat k],\quad
F_n=\gcd_k|u_k|>0,\quad w_k=u_k/F_n.
$$


The actual primitive dual polynomial and endpoint scalar are


$$
\widehat Q_n(z)=\sum_{k=n}^{3n}\frac{k!}{n!}w_kz^{3n-k},
\qquad Z_n=\widehat Q_n(1)\ne0.
\tag{3}
$$


The endpoint determinant is exactly $\mathcal E_n=(-1)^nF_nZ_n$.

The earlier dual note establishes the one-dimensional simultaneous Taylor system and the cross-product identification. The earlier literature_hp_dvr_content_and_obstruction.md records the simultaneous numerators as $p$-integral for $p>3n$ and the loss of information when coordinate Plücker minors are combined into polynomial coefficients. A targeted project search found no previous statement of the global numerator-integrality argument below or of (1)–(2). This is an extension of those identities, not a new proof of Mahler duality or a resolution of that Plücker-information obstruction.

## 2. Both actual simultaneous numerator polynomials are integral

Define


$$
\widehat P_{e,n}=T_{2n}(\widehat Q_ne^z),\qquad
\widehat P_{a,n}=T_{2n}(\widehat Q_n\arctan z).
\tag{4}
$$


The simultaneous Taylor equations say that both omitted blocks of coefficients at degrees $2n+1,\ldots,3n$ vanish.

For a coefficient of degree $0\le t\le2n$, put $j=3n-t$, so $n\le j\le3n$. Only $k\ge j$ can contribute to the exponential coefficient. Its term is


$$
\frac{k!}{n!(k-j)!}w_k
=\frac{j!}{n!}\binom kj w_k\in\mathbb Z.
\tag{5}
$$


For the arctangent coefficient, only positive odd $k-j$ contribute, and the term is


$$
\frac{k!}{n!}\tau_{k-j}w_k
=\frac{j!}{n!}\binom kj (k-j-1)!
 (-1)^{(k-j-1)/2}w_k\in\mathbb Z.
\tag{6}
$$


Here $j!/n!$ is integral because $j\ge n$. These identities prove


$$
\boxed{\widehat P_{e,n},\widehat P_{a,n}\in\mathbb Z[z].}
\tag{7}
$$


They avoid a loss of $n!$ in the endpoint denominator. Merely noting that $k!$ clears the Taylor coefficients would give the weaker bound $q_n\mid n!|Z_n|$.

## 3. Evaluation of the actual cross product gives the selected endpoint

Let $T_E=(A_E,B_E,C_E)$ and $T_F=(A_F,B_F,C_F)$ denote the two unique high solutions of degree at most $n$, with endpoints


$$
(B_E(1),C_E(1))=(1,0),\qquad
(B_F(1),C_F(1))=(0,1).
$$


Their remainders have order at least $3n+1$, and the standard cross product is


$$
T_E\times T_F
=(B_EC_F-C_EB_F,\ C_EA_F-A_EC_F,\ A_EB_F-B_EA_F).
$$


The reviewed simultaneous uniqueness and (3) give the exact polynomial identity


$$
T_E\times T_F
=\frac1{Z_n}
(\widehat Q_n,\widehat P_{e,n},\widehat P_{a,n}).
\tag{8}
$$


At $z=1$, the second and third components on the left are respectively $-A_E(1)$ and $-A_F(1)$. The actual canonical solution is $T_E+4T_F$. Thus, with


$$
N_n=\widehat P_{e,n}(1)+4\widehat P_{a,n}(1)\in\mathbb Z,
\tag{9}
$$


equation (1) follows. Reversing the sign of the rational approximant does not change $q_n$. The formula includes $N_n=0$, with the conventional denominator 1.

For direct arithmetic use, let $E_r=\sum_{s=0}^r1/s!$ and $T_r=\sum_{s=1}^r\tau_s$. Interchanging the finite Taylor sums gives the explicit integer functional


$$
\boxed{
N_n=\sum_{k=n}^{3n}\binom kn w_k
 \left((k-n)!E_{k-n}+4(k-n)!T_{k-n}\right).
}
\tag{9a}
$$


Both factorial partial sums in parentheses are integers. Replacing $E_{k-n},T_{k-n}$ by $E_k,T_k$ inside the equivalent expression $(1/n!)\sum k!w_k(\cdots)$ leaves the result unchanged: their differences pair with precisely the $n$ exponential and arctangent column equations of $X_n$. This supplies the direct endpoint-telescoping form with the same normalization.

For $p>3n$, the primitive dual has unit coefficient content, so


$$
v_p(q_n)\le v_p(Z_n)=v_p(d_n^{II}).
\tag{10}
$$


This local implication concerns the single selected endpoint value. It does not assert integrality of the full selected triple from simultaneous integrality.

More generally, an integer endpoint pair $(B(1),C(1))=(\beta,\gamma)$ has


$$
A(1)=-\frac{\beta\widehat P_{e,n}(1)+\gamma\widehat P_{a,n}(1)}{Z_n},
\tag{11}
$$


so its reduced denominator also divides $|Z_n|$.

There is also an exact global gcd identity in the archive's augmented-determinant convention. In raw_arctan_endpoint_dyadic_attempt.md, $\Delta_A$ appends $n!A(1)$ and $\Delta_B$ appends $B(1)$, after the common row $C(1)-4B(1)$. Thus


$$
\Delta_B=-\mathcal E_n=(-1)^{n+1}F_nZ_n,\qquad
\frac{\Delta_A}{n!\Delta_B}=A_n(1).
$$


Consequently


$$
\boxed{
\Delta_A=(-1)^n n!F_nN_n,\qquad
\gcd(|\Delta_A|,n!|\Delta_B|)
=n!F_n\gcd(|N_n|,|Z_n|).
}
\tag{11a}
$$


In particular the complete extremal content $F_n$, with every prime-power exponent, cancels from the actual reduced endpoint denominator. The factor $n!$ in (11a) belongs to the appended row normalization and is not an extra factor in (1).

## 4. A primitive cofactor congruence on the saturated family

Assume $n=mp^\nu,\ 3m<p$. Write $T=p^\nu$, and retain the notation from raw_endpoint_scalar_cauchy_restriction.md:


$$
c_r=\frac{(2n)!}{(n+r)!},\quad
\delta_r=\det\mathsf Z[\widehat r,:],\quad
h_n=\gcd_r|c_r\delta_r|.
$$


The exact cofactor transport there states


$$
w_{n+t}
=\frac{(-1)^t}{h_n}
 \sum_{\substack{0\le r\le n\\0\le t-r\le n}}
 \binom n{t-r}c_r\delta_r.
\tag{12}
$$


The independently reviewed Cauchy-block theorem gives


$$
p\nmid\delta_n,\qquad p\nmid h_n.
\tag{13}
$$


For every $r<n$, the factorial ratio $c_r$ contains the factor $2n$; hence $p\mid c_r$. Since $c_n=1$, (12) implies


$$
w_k\equiv0\quad(k<2n),\qquad
w_{2n+s}\equiv(-1)^{n+s}\binom ns\,\eta_n
\quad(0\le s\le n),
\quad
\eta_n=\delta_n/h_n\in\mathbb Z_p^\times.
\tag{14}
$$


In particular the exact normalization retains $h_n$; it may not be silently set equal to 1. If
$W_n(z)=\sum_{k=n}^{3n}w_kz^k$, then


$$
\boxed{W_n(z)\equiv\eta_n z^{2n}(z-1)^n\pmod p.}
\tag{15}
$$


Since $p\mid n$, Lucas's theorem (or $(z-1)^n=((z^p-1)^{n/p})$ in characteristic $p$) also implies that the surviving coefficients in (15) have $p\mid k$.

## 5. The exponential and arctangent endpoints modulo $p$

In the endpoint sum of the coefficients (5), indices satisfy $n\le j\le k\le3n$. The factor $j!/n!$ is divisible by $p$ whenever $j\ge n+p$. For $j=n+a,\ 1\le a<p$, any $k$ with $w_k\not\equiv0\pmod p$ is divisible by $p$, and
$\binom{k}{n+a}\equiv0\pmod p$, again by Lucas. Thus only $j=n$ remains:


$$
\widehat P_{e,n}(1)
\equiv\sum_k\binom kn w_k
=[y^n]W_n(1+y)
\equiv\eta_n\pmod p.
\tag{16}
$$


This is a Hasse coefficient identity and does not divide an ordinary derivative by a nonunit factorial.

The same argument applies to (6), since every extra factorial there is integral. Only $j=n$ can remain, and every surviving $k$ satisfies $k\ge2n$. If $n>p$, then $k-n>p$, so $(k-n-1)!$ is divisible by $p$. Therefore


$$
\boxed{
n>p\quad\Longrightarrow\quad
\widehat P_{a,n}(1)\equiv0,\qquad N_n\equiv\eta_n\not\equiv0\pmod p.
}
\tag{17}
$$


Combining (1) and (17) gives $v_p(q_n)=v_p(Z_n)$.

The remaining saturated case $n=p$ can also be evaluated exactly at this first layer. Only $j=p,k=2p$ survives the arctangent sum: $w_{2p}\equiv-\eta_n$, $\binom{2p}{p}\equiv2$, and Wilson gives $(p-1)!\equiv-1$. Hence, with $\chi_p=(-1)^{(p-1)/2}$,


$$
\widehat P_{a,p}(1)\equiv2\chi_p\eta_p,\qquad
N_p\equiv(1+8\chi_p)\eta_p\pmod p.
\tag{18}
$$


For $p>3$, $1+8\chi_p$ is a unit except at $p=7$. This is a finite symbolic exception obtained from (18), not a prime scan.

## 6. Exact actual-denominator consequences

The reviewed endpoint-scalar theorem supplies


$$
v_p(Z_n)=\frac{n-m}{p-1}+e_{n,p},
\qquad e_{n,p}=v_p(d_n^{II}).
\tag{19}
$$


Thus (2) follows for every saturated $n>p$, irrespective of whether $e_{n,p}$ is known.

The separately reviewed p-adic nonvanishing criterion in raw_endpoint_padic_limit_nonvanishing_criterion.md gives concrete families:

- For $n=p^\nu,\ p>3,\ \nu\ge2$, one has $e_{n,p}=0$, so
  

$$
\boxed{v_p(q_{p^\nu})=(p^\nu-1)/(p-1).}
$$


  The simultaneous denominator is a $p$-unit but the actual selected denominator has the displayed positive valuation.
- For $n=p,\ p>3,\ p\ne7$, equations (18)–(19) give $v_p(q_p)=1$.
- At the single degree $n=p=7$, $v_7(Z_7)=1$ and (18) gives $v_7(N_7)\ge1$, so
  

$$
\boxed{v_7(q_7)=0.}
$$


  This does not require solving the degree-7 system.
- For $n=4\cdot17^\nu,\ \nu\ge2$, the reviewed $p^2$ coefficient-ray criterion gives $e_{n,17}=1$, hence
  

$$
\boxed{v_{17}(q_n)=(n-4)/16+1.}
$$


- More generally, on a saturated family with $n>p$, any known exact value of $e_{n,p}$ transfers without further loss to (2). In particular a unit fixed Legendre seed gives $e=0$, and a seed of valuation exactly 1 gives $e=1$ from the second level onward.

These are local exact valuations. The displayed explicit families with $e_{n,p}=0$ or $1$ have a contribution linear in $n$ for a fixed $p$. The general formula (2) does not bound an unknown $e_{n,p}$, and no global sharp height estimate for $q_n$ is inferred.

## 7. Normalization controls from already archived degrees

No new degree system was solved. The archived primitive vectors give:

For $n=1$, $w=(-2,3,-1)$,


$$
\widehat Q=-2z^2+6z-6,\quad
\widehat P_e=z^2-6,\quad
\widehat P_a=6z^2-6z.
$$


Thus $Z=-2,\ N=-5,\ A(1)=-5/2,\ q=2$.

For $n=2$, $w=(940,-1944,1117,-162,49)$,


$$
\begin{aligned}
\widehat Q&=940z^4-5832z^3+13404z^2-9720z+17640,\\
\widehat P_e&=925z^4+5652z^3+12504z^2+7920z+17640,\\
\widehat P_a&=-2592z^4+7524z^3-9720z^2+17640z.
\end{aligned}
$$


Consequently $Z=16432,\ N=96049,\ q=16432$, whereas $d_2^{II}=4108$. This is a small exact control of the distinction between the global denominator $|Z_n|$ in (1) and $d_n^{II}$; it is not the proof of any infinite-family claim.

## 8. Scope and the useful next arithmetic quantity

Equation (1) reduces the actual selected endpoint denominator to two explicit integers with all factorial factors retained. On the saturated families in (2), the numerator is proved to be a unit, so no unknown cancellation remains at that prime. For other primes, the remaining gate is exactly


$$
v_p(N_n)=v_p\!\left(\widehat P_{e,n}(1)+4\widehat P_{a,n}(1)\right)
$$


relative to $v_p(Z_n)$. This is an endpoint functional, not the full coordinate Plücker content.

The theorem does not reconstruct every coefficient of $A,B,C$ from the simultaneous polynomial, prove a global denominator growth rate, or settle the analytic error estimate needed for the irrationality argument. It does show precisely why a general warning about lost Plücker coordinates does not prevent the selected endpoint relation: the chosen endpoint rows themselves isolate the two needed cross-product components.
