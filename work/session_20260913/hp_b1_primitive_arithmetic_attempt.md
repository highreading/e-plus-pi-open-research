> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primitive arithmetic of the degree-one HP family

Date: 2026-09-13. Bounded arithmetic continuation of
`hp_b1_endpoint_attempt.md`. No bulk q_n scan was performed.

**Subsequent resolution of the coefficient-clearer target:**
`hp_b1_special_gcd_and_denominator.md` proves that every coefficient
clearer of C_0-C_1 has logarithm at least 2n log n-O(n), matching the
available upper bound. Thus the sufficient target (18) below is now
proved impossible, including on infinite subsequences. The companion
algebra remains valid, but further progress must concern its reduced
evaluated gcd or a different companion. The earlier open-target language
below records the state at the time this note was written.

## Verdict

No unconditional upper bound below 2log(1+sqrt2) for log(q_n)/n, and no
unconditional lower bound proving primitive nondecay, was obtained.
The previous analytic theorem remains valid. This investigation proves
two actual arithmetic restrictions and constructs a rational companion
whose exact remaining height threshold can be stated:

1. Every coefficient of the elementary projection polynomials C_0,C_1,
   and the rational numbers t_0,t_1,a_0,a_1, has reduced denominator
   supported on primes at most n. In particular, all apparent factorial
   poles at n<p<=2n+1 cancel. An exact first-lift formula identifies what
   must be controlled next; large factorial denominators cannot themselves
   be counted as prime factors of the final q_n.

2. For the primitive *full integral triple*, the part of its endpoint gcd
   at p>2n+2 is bounded by the gcd of two explicitly defined integer
   coefficients H_n(1) and J_(n+1)(1). This is an all-index local
   divisibility theorem for the actual endpoint gcd, not a model sequence.
   No sufficiently strong global bound for this auxiliary gcd is proved.

3. There is a rational companion to e with factorially small error. To
   turn it into a primitive-growth proof, it would suffice to clear one
   explicit difference polynomial with common denominator at most
   exp((3/2-eta)n log n+O(n)). The currently proved common clearer has
   leading exponent2; the new prime cancellation improves only its O(n)
   term. Thus the b=0 continued-fraction argument still does not close b=1.

## 1. Archive and literature checks

Reviewed the Laguerre-square common-kernel gcd barrier, the conditional
rational-output saturation theorem, Item184's projective-height audit,
and the constrained root-of-unity HP audit with its tangent-number gcd.
They concern different families, but correctly warn that a real norm or
an arbitrary clearing scale does not bound the reduced endpoint gcd.
Nothing in those notes proves the divisibility statements below or closes
the actual b=1 denominator.

For Legendre congruences I checked Zhi-Hong Sun's primary paper
[Generalized Legendre polynomials and related congruences modulo p^2](https://arxiv.org/pdf/1101.5386).
Its parameter symmetry and binomial representation support the elementary
folding proof below. Its p^2 identities concern truncated generalized
Legendre polynomials; they do not supply a nonvanishing or gcd bound for
our bilinear kernel after factorial contractions. This hypothesis mismatch
is retained rather than treating a supercongruence as an endpoint theorem.

## 2. Exact large-prime cancellation

Use the objects from the preceding note:



$$
K_n(t,s)=\sum_{k=0}^n p_k(t)p_k(s)/h_k,
 \quad \ell_j(s^q)=1/(n+q+1-j)!,\quad
 C_j^*(t)=-\ell_j^{(s)}K_n(t,s),\quad j=0,1.
$$



The kernel can equally be written



$$
K_n(t,s)=\frac12\sum_{k=0}^n(2k+1)P_k(x)P_k(y),
 \qquad x=-i(2t-1),\quad y=-i(2s-1).
\tag{1}
$$



Its coefficients are dyadic rationals; the two i-powers combine to real
coefficients. All reductions below can first be made in Z_p[i] and then
restricted to the rational coefficients.

### Folding lemma

Let p be an odd prime with n<p<=2n+1, and set



$$
m=p-2-n\ge-1,\qquad K_{-1}=0.
$$



Then coefficientwise



$$
K_n(t,s)\equiv K_m(t,s)\pmod p.
\tag{2}
$$



Proof: for 0<=k<=p-1, the polynomial congruence
P_(p-1-k)(x)=P_k(x) mod p follows from



$$
P_k(x)=\sum_j\binom kj\binom{k+j}j((x-1)/2)^j.
$$



For j<p, the coefficient is a polynomial in k modulo p and is symmetric
under k -> -1-k. Terms beyond the respective polynomial degrees vanish
by their binomial factors. Pair indices k and p-1-k in (1). Their
weights sum to2p and their polynomial products agree modulo p. The
central weight p also vanishes. Exactly the indices0,...,p-2-n remain.

Put r=p-n-1=m+1. In ell_0, factorial poles occur precisely for q>=r.
In ell_1 they occur for q>=r+1. Every such kernel coefficient vanishes
modulo p by (2), because K_m has degree at most r-1 in s. The factorials
in question are less than2p and contain only one p. Therefore



$$
C_0,C_1\in\mathbb Z_p[z].
\tag{3}
$$



The endpoint values t_j=-C_j(1) are p-integral. Since p>n, the Taylor
coefficients of e^z and F through degree n are p-integral as well, so
a_j=-[T_n(z^j e^z+C_jF)](1) is p-integral. Primes p>2n+1 cannot divide
the easy common denominator in the first place. Hence all reduced
denominators of these quantities are supported on primes at most n.

This statement does **not** say that q_n is supported on those primes:
division by the rational endpoint delta introduces its numerator.

### Exact first-lift formula

Define the p-integral polynomial



$$
E(t,s)=(K_n(t,s)-K_m(t,s))/p,
\quad E_q(t)=[s^q]E(t,s),\quad K_{m,q}(t)=[s^q]K_m(t,s).
$$



Wilson's theorem gives p/(p+j)! = -1/j! mod p for 0<=j<p. Consequently



$$
\ell_0 K_n\equiv
 \sum_{q=0}^{m}\frac{K_{m,q}}{(n+q+1)!}
 -\sum_{q=r}^{n}\frac{E_q}{(q-r)!}\pmod p,
\tag{4}
$$





$$
\ell_1 K_n\equiv
 \sum_{q=0}^{m}\frac{K_{m,q}}{(n+q)!}
 -\sum_{q=r+1}^{n}\frac{E_q}{(q-r-1)!}\pmod p.
\tag{5}
$$



An empty sum is zero, including m=-1. These expressions involve the
first quotient of the actual kernel, not just its degree-drop residue.

For the rational representative



$$
X=(1+t_1)a_0-(1+t_0)a_1,\qquad Y=\delta=t_1-t_0,
\tag{6}
$$



both X,Y are p-integral, and



$$
v_p(q_n)=\max(0,v_p(Y)-v_p(X)).
\tag{7}
$$



Thus Y nonzero mod p excludes p from q_n, whereas Y=0 and X nonzero
mod p includes it. If both vanish, a further lift is needed. The folding
lemma alone proves neither alternative uniformly.

The original easy clearer for C_j was
T=2^(2n+1)(2n+1)!. Equation(3) permits the improved all-index clearer



$$
T^\flat=\frac{2^{2n+1}(2n+1)!}{\prod_{n<p\le2n+1}p}.
\tag{8}
$$



This is an actual denominator cancellation. It changes log T by O(n),
not by a positive multiple of n log n.

## 3. A local restriction on the actual endpoint gcd

Define integer polynomials



$$
H_k(x)=k![t^k]e^{xt}(1-t+t^2/2)^k,\qquad
 J_k(x)=kH_k(x)+H'_k(x).
\tag{9}
$$



Integrality follows directly from the ring of exponential generating
series with integer derivative coefficients: 1-t+t^2/2 and e^{xt}
have integer derivative coefficients in Z[x], as do their products.

Let (A,B,C) be the primitive full integral triple at index n, and let
d=gcd(A(1),B(1)). Then, for every prime p>2n+2,



$$
v_p(d)\le v_p\bigl(\gcd(H_n(1),J_{n+1}(1))\bigr).
\tag{10}
$$



This is meaningful for all sufficiently large n; if both displayed
auxiliary integers vanish at a small index, the assertion is vacuous.

### Proof

Suppose p^h divides d. Modulo p^h, each of A,B,C is divisible by z-1,
because A(1)=0 and B(1)=C(1)=0. Divide and write the quotient triple
(Abar,b,Cbar), of degree caps (n-1,0,n-1). The constant b is a p-unit.
Otherwise B is zero mod p; the n+1 high logarithmic moment equations
then force C=0 mod p because the Legendre norms h_0,...,h_n are units
when p>2n+2. The low equations force A=0 mod p, contradicting primitive
full coefficient content.

Since z-1 is a unit at zero, the quotient remainder still vanishes
through degree2n+1 modulo p^h. Let m=n-1. Testing its high moment
equations against p_(m+1) and p_(m+2), which are orthogonal to Cbar^*,
therefore gives



$$
\ell_m(p_n)=\ell_m(p_{n+1})=0\pmod{p^h},
 \qquad \ell_m(t^j)=1/(m+j+1)!.
\tag{11}
$$



The constant b has been canceled as a p-unit. Rodrigues' formula for
p_k, followed by reversing (t^2-t+1/2)^k, gives the exact identities



$$
\ell_{n-1}(p_n)=H_n(1)/(2n)!,\qquad
 \ell_{n-1}(p_{n+1})=J_{n+1}(1)/(2n+2)!.
\tag{12}
$$



All these factorials are p-units. This proves (10), including its full
prime-power valuation rather than only a mod-p implication.

The new obstacle is an ordinary gcd of two explicit integers. A
classical-orthogonal-polynomial shortcut is not justified: H_k is not the
standard Laguerre or Bessel polynomial. For example, exact small-degree
resultants of H_n(x) and J_(n+1)(x) already have prime factors31 and107
at n=4, and3371 at n=5. Thus a parameter-uniform assertion that all their
resultant primes are at most2n+2 is false. This does not rule out a stronger
special statement at x=1, but that statement still needs a proof.

The checked values at the already used degrees n=4,8,12,16 have auxiliary
gcds15,7,11,15. These four values are diagnostics only. Equation(10)
does not bound the endpoint gcd at primes at most2n+2, and it does not
yet give a rate for q_n.

## 4. A factorially accurate rational companion and its exact height gap

Set g_j=[T_n(C_jF)](1), so a_j=-E_(n-j)-g_j, with
E_k=sum_(r=0)^k1/r!. The representative (6) corresponds to



$$
B=(1+t_0)(1-z)+\delta,\qquad
 C=C_0-C_1+t_1C_0-t_0C_1.
$$



Define the rational companion



$$
f_n^*=\frac{g_0-g_1+1/n!}{\delta},\qquad
 r_n^*=-X/\delta-f_n^*.
\tag{13}
$$



Exact endpoint algebra gives



$$
r_n^*=E_n+
 \frac{t_0/n!+t_1g_0-t_0g_1}{\delta}.
\tag{14}
$$



All t_j,g_j are at most exp(O(n))/n! in absolute value. The proved
endpoint bound gives |delta|>=exp(-O(n))/n!. Therefore



$$
0<|e-r_n^*|\le\exp(-n\log n+O(n)).
\tag{15}
$$



Strict positivity uses irrationality of e. Since X/delta tends to
-(e+pi), f_n^* tends to pi and remains bounded.

Let S_n be **any positive integer multiple of n!** that clears the
coefficients of C_0-C_1. Its endpoint is delta, so S_n delta is integral.
Let d_F=2^n lcm(1,...,n). Clearing (13) shows



$$
H(f_n^*)\le\exp(\log S_n-\log n!+O(n)),
\tag{16}
$$



where H is the maximum of the reduced numerator and denominator. This
uses both the real size of delta and the *proved* denominator clearing;
real size alone would not justify (16).

If q_n=den(X/delta), the denominator of r_n^* is at most q_n H(f_n^*).
Euler's continued fraction gives the all-rationals irrationality measure
mu(e)=2. Combining it with (15)–(16), for each epsilon>0, yields



$$
\log q_n\ge
 \frac{n\log n}{2+\epsilon}-\log S_n+\log n!-O_\epsilon(n).
\tag{17}
$$



Consequently an all-index estimate



$$
\log S_n\le(3/2-\eta)n\log n+O(n),\qquad\eta>0,
\tag{18}
$$



would prove liminf log(q_n)/(n log n)>=eta and hence eventual primitive
growth by the established analytic rate. The analogous estimate on a
subsequence would only prove growth on that subsequence.

The available S_n=T^flat in (8) has log S_n=2n log n+O(n), so (17) is
currently vacuous at its leading scale. Proving (18) requires a further
factorial-scale cancellation, not just the large-prime cancellation in
Section2. No such estimate has been established.

A stronger error estimate of order exp(-2n log n+O(n)) would also alter
this balance, but it is not supplied by (14). At the four pre-existing
degrees4,8,12,16, r_n^* is not the classical diagonal Padé approximant
to e; the bounded exact comparison does not support identifying the two.
These finite checks do not prove an asymptotic lower error bound.

## 5. What should be attempted next

The most specific remaining arithmetic targets are:

* Bound the special gcd gcd(H_n(1),J_(n+1)(1)) and the complementary small
  prime endpoint valuations. The explicit resultants warn against assuming
  a classical two-term orthogonal-polynomial gcd theorem.
* Analyze the first lifted kernel in (4)–(5), followed by the exact valuation
  difference (7), before attempting to count large primes in q_n.
* Prove or refute the concrete denominator threshold (18) for C_0-C_1.
  This would decide whether the newly constructed rational companion can
  extend the successful b=0 obstruction.

At present none of these supplies the requested favorable bound for q_n
or an unconditional primitive-growth theorem for b=1. The main project
therefore remains unresolved; the new claims in this note are the exact
denominator support, first-lift formulas, local gcd restriction, and
conditional companion-height reduction.

## 6. Verification record and subsequent additions

`check_hp_b1_arithmetic.py` passes five predeclared exact local controls
at (n,p)=(2,3),(4,5),(8,11),(12,17),(16,19), checking folding, Wilson
first lifts, p-integrality, and the two Rodrigues identities in (12).
These checks support the algebra but are not asymptotic evidence for q_n.

The independent audit in `hp_b1_prime_folding_independent_review.md`
accepts the prime-power endpoint-gcd gate and the rational-companion
height calculation. It also proves the new exact exclusion
p does not divide q_(p-1) for every odd prime p, using the first
Christoffel-Darboux lift at n=p-1. Section7 of that independent audit
verifies the subsequent sharp coefficient-denominator obstruction.
