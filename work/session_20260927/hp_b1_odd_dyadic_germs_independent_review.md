> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the odd dyadic numerator germs

Date: 2026-09-27. Reviewer: audit_sources.
Reviewed inputs: check_hp_b1_odd_dyadic_germs.py and
hp_b1_odd_dyadic_germs_checks.json.
Status: FULL PASS, including a successful unchanged certificate rerun.
This closes an in-progress task after the user's request to stop.
No new residue disk, degree, prime, or precision was introduced.

## 1. Coefficientwise tail proof

For integers a and L>=0, consider


$$
(a+8Y)_L=\prod_{j=0}^{L-1}(a-j+8Y).
$$


The Gauss valuation of each linear factor is min(v_2(a-j),3).
Among L consecutive integers there are at least floor(L/2),
floor(L/4), and floor(L/8) multiples of 2,4,8 respectively.
Thus


$$
v_{\rm G}((a+8Y)_L)
 \ge\lfloor L/2\rfloor+\lfloor L/4\rfloor+\lfloor L/8\rfloor
 \ge7L/8-3.                                             \tag{1}
$$


The bound is uniform in a, including negative a. A slope 16 in
place of 8 only improves it.

Put R=b+2c, s=b+c, and epsilon=(-1)^b/(2^c b!c!).
Then


$$
v_2(2^c b!c!)\le c+b+c=R,\qquad s\ge R/2.
$$


Therefore the H summand
epsilon (X)_R(X)_s on X=a+8Y has Gauss valuation


$$
\ge7(R+s)/8-6-R\ge5R/16-6.                            \tag{2}
$$


This also bounds the A summand after multiplication by
D(2X-R), because D(Z)=sum_{j>=0}(Z)_j is integral on every
integer 8-adic disk and has Gauss norm at most 1.

The division-free K summand for R>=1 is


$$
\epsilon (X)_{R-1}(X+1)_s(2X+2-R).
$$


Its bound is


$$
\ge7(R-1+s)/8-6-R\ge5R/16-7.                           \tag{3}
$$


Multiplication by D(2X+1-R) gives the same bound for B.
The R=0 terms are respectively 2 and 2D(2X+1).
These are exactly the actual Rodrigues contractions; no division
by the nonunit X+1 is performed.

Equations (2)–(3) prove convergence as restricted Q_2 series.
They do not on their own prove that every low summand is integral.
The script supplies that missing finite check before using modular
multiplication, as detailed next.

## 2. Precision and integrality in the exact program

The program uses precision 10, modulus 1024, and R<55.
For every omitted R>=55, (2)–(3) give Gauss valuation at least 10.
For D it retains j<20. Every omitted j>=20 has valuation at least
7j/8-3>=10 by (1), including the actual slope-16 arguments.

For EVERY retained H and K summand the numerator is formed as a
complete integer polynomial first. The function divided asserts that
every coefficient is divisible by the full 2-primary part of
2^c b!c!, divides that part exactly, and only then inverts its odd
part modulo 1024. Thus every retained summand is certified
coefficientwise 2-integral. Together with the tail bounds this
proves integrality of the entire H,K germs.

D is integral coefficientwise without a check. Hence the same
assertions also give integrality of every retained A,B summand
and of their full tails. It follows that errors of order 1024 in
the four contractions remain of order 1024 in C=KA-HB.
There is no guard-bit loss. In particular, no value-only integrality
or unverified cancellation of denominators is being used.

The polynomial code does not truncate by degree: all coefficients
of every finite product are retained, and only zero terminal
coefficients after reduction are removed. The certificate therefore
covers entire germs modulo 1024, rather than finitely many Taylor
coefficients or finitely many integer evaluations.
The four disks 1,3,5,7 modulo 8 exhaust the odd 2-adic integers.

## 3. Certified reductions and exact consequences

The complete output for C(a+8Y), modulo 1024, is


$$
\begin{array}{c|l}
a& C(a+8Y)\\ \hline
1&216Y+32Y^2+768Y^3+512Y^4\\
3&652+296Y+544Y^2+128Y^3\\
5&564+184Y+672Y^2+768Y^3+512Y^4\\
7&824+808Y+480Y^2+128Y^3 .
\end{array}                                               \tag{4}
$$


Every omitted coefficient is zero modulo 1024.

At a=1 the exact identity C(1)=0 is required, and is available:
H_1=K_2=0, A_1=3, B_1=10. Therefore C(1+8Y)/(8Y)
is an integral restricted series with constant reduction 1
modulo 2. The source's exact index derivative C'(1)=27 is
consistent with the displayed linear coefficient 216; the reduction
already suffices for unitness. Thus


$$
v_2(C_n)=v_2(n-1)\quad(n\equiv1\pmod8,\ n\ne1).          \tag{5}
$$



At a=3 and a=5, division by 4 gives constant reduction 1 modulo 2.
Consequently


$$
v_2(C_n)=2\quad(n\equiv3,5\pmod8).                       \tag{6}
$$


The a=3 value is 2, not v_2(n-1); extrapolating a single polynomial
factor across all odd disks would have been incorrect.

At a=7, F(Y)=C(7+8Y)/8 is integral restricted and has reduction
1+Y modulo 2. Its linear coefficient is odd and every coefficient
of degree >=2 is even. Hensel's lemma gives a unique root
eta in 1+2 Z_2. Factoring the root leaves a unit at every point:


$$
C(7+8Y)=8(Y-\eta)U(Y),\qquad U(Y)\equiv1\pmod2.
$$


With nu=7+8eta this proves


$$
\nu\in15+16\mathbb Z_2,\qquad
 v_2(C_n)=v_2(n-\nu)\quad(n\equiv7\pmod8).                \tag{7}
$$


Valuations of zero may be infinite. The assertion is a statement
about the actual integer contractions via analytic interpolation.

The existence of nu supplies no Diophantine upper bound on
v_2(n-nu), and no assertion that nu is rational or irrational.
The certificate alone neither resolves this exceptional branch nor
proves a whole odd-family exclusion. Any transfer from C to the
actual rational endpoint must additionally preserve Delta and the
second-kind term, exactly as in the separate b=1 normalization.

## 4. Reproducibility

I inspected the whole saved script and the saved output, including
the all-coefficient integrality assertions and the order of exact
division/modular reduction. The unchanged precision-10 script was
rerun with Python 3.12 and exited successfully, reproducing every
displayed polynomial and integrality assertion. No ordinary floating arithmetic is used in
the polynomial certificate. The only floating operation is ceil
of the exactly harmless rational 272/5=54.4 when setting the cutoff
55; the displayed mathematical bound independently validates 55.
