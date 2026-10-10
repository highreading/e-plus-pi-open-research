> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — a next-precision common-unit expansion and the unresolved joint carry

## Executive conclusion

I retain as an accepted scoped input


$$
H\equiv N\pmod{64}
$$


on the original family


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$



**I do not obtain a proved modulus-$128$ or modulus-$256$ mixed–norm alignment on $N\equiv0\pmod{64}$, nor a relative valuation bound on an infinite subfamily of that locus.** The next precision cannot be obtained by reusing the displayed fifth-precision coefficient vectors as exact coefficients.

The rigorous progress below is:

1. An explicit common-unit ratio expansion modulo $256$, with the higher-parameter dependence retained.
2. A finite description of the common odd units modulo $256$, including the overflow cases and all negative-complement ratios.
3. A proof that every odd residue class of $D\bmod2^L$ is reached infinitely often by the **original power-$9$ family**. This transfers bounded local unit states, but not unbounded binomial convolutions.
4. An exact decomposition of the next joint carry. The old first-column precision already determines $N\bmod128$; the old two-column precision does **not** determine $H\bmod128$.
5. Identification of new contact and exterior-force terms that prevent a silent lift of the completed argument.

These results isolate a concrete next obligation rather than establish a new depth comparison. Irrationality of $e+\pi$ remains unresolved.

---

## 1. Scope, notation, and sources

Keep


$$
D=\frac{9^{18+32u}-81}{128},\qquad
C=4002D+2532,
$$


so


$$
b=128D+81,\qquad n=128C+66,
$$


with $D$ odd and $C\equiv2\pmod4$.

The actual quantities remain


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad N=X^TX,\qquad H=X^TY,
$$




$$
R=2^{n/2}\binom n{n/2},\qquad
\lambda=\frac{(n!)^2}{2^n}.
$$


The metric is unchanged:


$$
W_j=\binom{n+2}{j},\qquad
\Omega=\operatorname{diag}\bigl((n+2)_{\underline j}^{\,2}\bigr)_{0\le j\le b}.
$$


Every actual contact inverse has range $0\le i,j<b$.

I use the audited fifth-precision interfaces at their stated scope:


$$
2X_j\pmod{64},\qquad 4Y_j\pmod{128},
$$


including the complete exterior forcing and actual endpoint. In particular,


$$
X,Y\in2\mathbb Z_2^{b+1}.
$$



The accepted turn22 theorem is not reproved. The auxiliary $D$-tables remain finite computations; they are not higher-precision data. The paired-derangement determinant family is separate and supplies no replacement denominator or coefficient vector here.

No external search, hash verification, or computation was executed for this report.

---

# Part I. One further common-unit precision

## 2. Exact common-unit ratios, including overflow

For a non-overflow residue retained in turn22, write


$$
j=128t+\rho,\qquad d=D-t,\qquad k=2C+1,\qquad a=84-\rho.
$$


Thus $a\ge16$ for these residues and $0\le t\le D$. The moments are


$$
M_s=\binom{128(k+d)+a}{128d+a-(s+4)}.
$$



The reference moment is


$$
M_{-4}=\binom{128(k+d)+a}{128d+a}.
$$


As established by factorial stripping,


$$
M_{-4}=\binom{k+d}{d}\,\tau,\qquad \tau\in\mathbb Z_2^\times.
$$



For $c=s+4\ge0$,


$$
R_c(d,k;a):=\frac{M_s}{M_{-4}}
=\frac{\binom{128d+a}{c}}{\binom{128k+c}{c}}.
\tag{2.1}
$$


For $c=-q$, $1\le q\le4$,


$$
R_{-q}(d,k;a)
=\frac{(128k)_{\underline q}}
       {(128d+a+1)^{\overline q}}.
\tag{2.2}
$$


These are exact identities, not congruences.

The same formulas cover the two previously retained overflow residues. For


$$
\rho=96,100,\qquad 0\le t\le D-1,
$$


put


$$
a=84-\rho+128,\qquad d'=D-t-1.
$$


Then $d'\ge0$, and


$$
M_{-4}
=\binom{k+d'}{d'}\,\tau
=\binom{k+D-t-1}{D-t-1}\tau.
$$


Equations (2.1)–(2.2) apply with $d'$ in place of $d$.

Thus the overflow substitution is **not** $d\mapsto d$: it is $d\mapsto d-1$, with the shorter original range retained. The weight still supplies the additional factor


$$
(C-t)\binom Ct.
$$



---

## 3. A linear translation formula modulo $256$

Define, for $1\le c\le15$,


$$
\mathcal L_c(a)
=\sum_{i=1}^{c}\frac{(-1)^{i-1}}{i}\binom a{c-i},
\qquad
\mathcal H_c=\sum_{i=1}^{c}\frac1i.
$$


Set $\mathcal L_0=\mathcal H_0=0$.

Although these are rational numbers, all expressions below are $2$-integral after multiplication by $128$.

### Proposition 3.1

For every nonnegative integer $d$, every integer $k$, and $0\le c\le15$,


$$
\boxed{
R_c(d,k;a)\equiv
\binom ac+
128\left(
d\,\mathcal L_c(a)
-k\,\mathcal H_c\binom ac
\right)
\pmod{256}.
}
\tag{3.1}
$$


Here the denominator in (2.1) is odd, and division means inversion in $\mathbb Z_2$.

### Proof

For $1\le i\le15$,


$$
\binom{128d}{i}
=
\frac{128d}{i}(-1)^{i-1}
\prod_{j=1}^{i-1}\left(1-\frac{128d}{j}\right).
$$


Every factor $128d/j$ in the product has valuation at least


$$
7-\lfloor\log_2(i-1)\rfloor.
$$


Consequently,


$$
v_2\left(
\binom{128d}{i}
-\frac{128d}{i}(-1)^{i-1}
\right)
\ge
14-v_2(i)-\lfloor\log_2(i-1)\rfloor
\ge9
$$


for $2\le i\le15$. The assertion for $i=1$ is exact. Hence


$$
\binom{128d}{i}
\equiv128d\,\frac{(-1)^{i-1}}i\pmod{256}.
$$



Vandermonde gives


$$
\binom{128d+a}{c}
\equiv
\binom ac+128d\,\mathcal L_c(a)
\pmod{256}.
\tag{3.2}
$$



Similarly,


$$
\binom{128k+c}{c}
=\prod_{i=1}^{c}\left(1+\frac{128k}{i}\right).
$$


Every nonconstant factor has valuation at least four. Products of two such factors vanish modulo $256$, so


$$
\binom{128k+c}{c}
\equiv1+128k\,\mathcal H_c\pmod{256}.
$$


In particular it is odd, and


$$
\binom{128k+c}{c}^{-1}
\equiv1-128k\,\mathcal H_c\pmod{256}.
\tag{3.3}
$$


The product of the two correction terms in (3.2) and (3.3) also has valuation at least eight. Multiplication proves (3.1). ∎

### What this changes

Turn22 replaced $R_c$ by $\binom ac$ at a coefficient-weighted lower precision. At the next precision, the explicit dependence


$$
128d\,\mathcal L_c(a)
-
128k\,\mathcal H_c\binom ac
\tag{3.4}
$$


must be retained whenever its coefficient does not annihilate it.

Thus a higher-precision table consisting only of $\rho$-dependent constants is not automatically valid. The first correction is an explicit function of the actual higher parameters.

This proposition is unconditional. Its application to the actual next mixed column still requires the next complete coefficient lift.

---

## 4. Negative moments are retained by exact odd-denominator arithmetic

For the four negative-complement ratios, formula (2.2) is the appropriate bounded expression. One must not apply (3.1) with negative $c$.

A division-safe implementation is:

1. Form the $q$ numerator factors and $q$ denominator factors in (2.2).
2. Extract their exact powers of two.
3. Retain the net power of two.
4. Invert only the remaining odd denominator modulo the required power of two.

For the retained non-overflow residues and $\rho=96,100$, the numbers


$$
a+1,\ldots,a+4
$$


are positive and less than $128$. Therefore


$$
v_2(128d+a+i)=v_2(a+i)
$$


for $1\le i\le4$; no unbounded valuation ambiguity occurs in these denominator factors.

At fifth precision, the supplied coefficient-depth inequalities killed the corresponding mixed terms. That does **not** by itself kill their next lifts: both the coefficient precision and the target modulus have changed. Formula (2.2), rather than their former zero residues, is the retained input for the next calculation.

---

## 5. A proved finite description of the common units

Let


$$
O(m)=\prod_{\substack{1\le j\le m\\j\ {\rm odd}}}j,
\qquad
L_7(m)=\prod_{i=0}^{6}O\!\left(\left\lfloor m/2^i\right\rfloor\right).
$$



For $p\ge3$,


$$
O(m+2^p)\equiv O(m)\pmod{2^p}.
$$


Indeed, the extra factors represent every odd residue modulo $2^p$, whose product is $1$.

It follows that


$$
\boxed{
L_7(m+2^{p+6})\equiv L_7(m)\pmod{2^p}.
}
\tag{5.1}
$$


Each floor in the definition changes by a multiple of $2^p$.

At modulus $256$, therefore, $L_7(m)$ depends only on


$$
m\bmod 2^{14}.
$$


For arguments $m=128q+a$, this is dependence only on


$$
q\bmod128,\qquad a.
$$



For example, the non-overflow common moment unit is


$$
\tau=
\frac{L_7(128(k+d)+a)}
 {L_7(128d+a)L_7(128k)}
\pmod{256}.
\tag{5.2}
$$


All denominators here are odd.

The weight unit has the analogous stripped expression. Hence the external common unit


$$
\xi=w\tau
$$


modulo $256$ has a finite description in terms of


$$
C,\ t,\ d,\ k\pmod{128}
$$


and the fixed residue $\rho$. On the original affine relation, it is enough to retain


$$
\boxed{D\bmod128,\qquad t\bmod128,\qquad \rho.}
\tag{5.3}
$$



This is a finite description of the **local units**, not of the complete higher-binomial sum. The higher factors


$$
\binom Ct\binom{k+D-t}{D-t}
$$


and their overflow counterparts must still retain their carry counts and normalized units.

In particular, the fact that odd squares are $1\bmod8$ no longer licenses dropping $\xi^2$ at every larger modulus. The weighted coefficient must be checked first.

---

# Part II. Original parameter transfer

## 6. Every odd $D$-residue is reachable infinitely often

The local-state transfer can be proved exactly.

### Proposition 6.1

For every $L\ge1$, as $u$ varies over the nonnegative integers,


$$
D(u)=\frac{9^{18+32u}-81}{128}
$$


runs through every odd residue modulo $2^L$, periodically. Every such residue occurs infinitely often.

### Proof

Put $g=9^{32}$. The elementary lifting identity gives


$$
v_2(g-1)=8,
$$


and, for $a\ge0$,


$$
v_2(g^{2^a}-1)=8+a.
$$


Therefore $g$ has order $2^{L-1}$ modulo $2^{L+7}$.

The group of residues congruent to $1\bmod256$ modulo $2^{L+7}$ also has $2^{L-1}$ elements. Thus $g$ generates this group.

The original value $9^{18}$ is congruent to $209\bmod256$, so


$$
9^{18}g^u
$$


runs through every residue congruent to $209\bmod256$ modulo $2^{L+7}$.

The map


$$
b\longmapsto\frac{b-81}{128}\pmod{2^L}
$$


is a bijection from those residues to the odd residues modulo $2^L$. Periodicity supplies infinitely many nonnegative $u$ for each residue. ∎

Equivalently, the exact recurrence is


$$
D(u+1)=gD(u)+\frac{81(g-1)}{128}.
\tag{6.1}
$$



### Necessary limitation

This proposition transfers a theorem whose hypotheses and conclusion depend only on a specified finite residue of $D$. It does **not** show that


$$
N\bmod128,\qquad H\bmod128,
$$


or an unbounded binomial convolution depends only on that residue.

Thus a passing local unit table on every odd $D\bmod128$ would have genuine original-domain relevance. An auxiliary full-convolution value at a small representative $D$, however, still cannot be transferred without a separate carry-and-terminal theorem.

---

# Part III. The exact next joint carry

## 7. What the old precision determines

Choose the canonical even residues


$$
x_j\equiv X_j\pmod{32},\qquad
y_j\equiv Y_j\pmod{32},
\qquad 0\le x_j,y_j<32.
$$


These are determined by the accepted fifth-precision interfaces. Write


$$
X_j=x_j+32a_j,\qquad
Y_j=y_j+32b_j,
\qquad a_j,b_j\in\mathbb Z_2.
$$


Define


$$
N_0=\sum_{j=0}^{b}x_j^2,\qquad
H_0=\sum_{j=0}^{b}x_jy_j.
$$



### Proposition 7.1 — next joint-carry decomposition

On the original family,


$$
\boxed{N\equiv N_0\pmod{128},}
\tag{7.1}
$$


whereas


$$
\boxed{
H\equiv H_0+64\mathcal C\pmod{128},
}
\tag{7.2}
$$


with


$$
\boxed{
\mathcal C=
\sum_{j=0}^{b}
\left(
a_j\frac{y_j}{2}
+b_j\frac{x_j}{2}
\right)\pmod2.
}
\tag{7.3}
$$



### Proof

Since $x_j$ is even,


$$
X_j^2-x_j^2=64x_ja_j+1024a_j^2
$$


is divisible by $128$. Summing proves (7.1).

Also,


$$
X_jY_j-x_jy_j
=32(a_jy_j+b_jx_j)+1024a_jb_j.
$$


Both $x_j,y_j$ are even, giving (7.2)–(7.3). ∎

This exhibits the missing mixed information precisely. It is not an unspecified “higher unit”: it is a single bilinear parity of the next column lifts.

On the true locus


$$
\mathcal Z_{64}=\{u\ge0:N\equiv0\pmod{64}\},
$$


the accepted theorem also gives $H\equiv0\pmod{64}$. Therefore


$$
\boxed{
\frac N{64}\equiv\frac{N_0}{64}\pmod2,
\qquad
\frac H{64}\equiv\frac{H_0}{64}+\mathcal C\pmod2.
}
\tag{7.4}
$$


The divisions are legitimate after the complete sums.

The old first-column precision is thus sufficient for the next norm digit. The old mixed precision is not sufficient for the next mixed digit.

### Why this is a real obstruction to the proposed lift

Abstractly, changing $Y$ by $32b$ preserves every displayed old second-column residue and preserves $H\bmod64$, but may change $H\bmod128$ through (7.3). This does not claim that the actual construction allows arbitrary $b$; it proves that the old residue interface alone cannot determine the next mixed digit.

The actual construction must supply $\mathcal C$.

---

## 8. New contact and forcing terms cannot be omitted

There are concrete reasons not to set the unknown next lifts to zero.

### 8.1 Contact polynomial modulo $128$

Write


$$
h=n/2=1+32e,\qquad e=2C+1\ \text{odd},
$$


and retain


$$
\phi^2=1+2U.
$$


In the integral divided-power ring,


$$
\phi^n=(1+2U)^h.
$$



Every divided-power polynomial with zero constant coefficient has square divisible by $2$: cross terms occur twice, and


$$
\binom{2i}{i}
$$


is even for $i>0$. Hence $U^2\in2\mathbb Z_2\langle x\rangle$.

The $k=1$ binomial term is


$$
2hU=2U+64eU.
$$


The $k=2$ term is $64ehU^2$, which vanishes modulo $128$. The $k=3,4,5$ terms have scalar depth at least seven; the $k=6$ term does also, since $\binom h6$ is even. Terms $k\ge7$ vanish immediately.

Consequently,


$$
\boxed{\phi^n\equiv1+66U\pmod{128}.}
\tag{8.1}
$$



Thus the old congruence $\phi^n\equiv1+2U\pmod{64}$ does not persist unchanged. The extra $64U$ is nonzero, for example in degree one.

Transferring this correction through the actual contact construction and finite inverse is a required part of a complete $P_{128}$ interface.

### 8.2 Exterior factorial tail modulo $256$

Let


$$
f_a=\frac{(b+a)!}{b!}.
$$


On the original family $b\equiv209\bmod256$,


$$
v_2(f_7)=7.
$$


Since $b+8$ is odd,


$$
v_2(f_8)=7.
$$


Since $v_2(b+9)=1$,


$$
v_2(f_9)=8.
$$


Therefore


$$
\boxed{
f_7\equiv f_8\equiv128\pmod{256},
\qquad
f_a\equiv0\pmod{256}\quad(a\ge9).
}
\tag{8.2}
$$



At raw second-column precision $256$, the exterior force therefore has **nine**, not seven, potentially nonzero factorial entries. In moment reconstruction this can extend the negative-moment range beyond the former $-8$ endpoint.

The whole logarithmic-force estimate remains comfortably sufficient to remove that entire force at this fixed precision. That fact does not remove the new exponential boundary terms.

### 8.3 Endpoint

The actual endpoint is still


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


Using the retained bounds,


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4,
$$


both


$$
X_b^2,\qquad X_b(Y_b-X_b)
$$


vanish modulo $256$. The endpoint causes no next-digit ambiguity, but this conclusion is taken **after retaining its $+1$**.

### 8.4 Interior support

The old high-weight exclusion proves vanishing modulo $64$, not automatically modulo $128$. Likewise, overflow contributions previously known to have raw depth nine may survive at raw modulus $1024$.

Accordingly, the old 31-class support is not asserted to be exhaustive at the next precision. A next-precision certificate must either reprove its exclusions or include the newly admitted classes.

---

# Part IV. Follow-on lemma and arithmetic consequences

## 9. A concrete joint lemma that would suffice

The shortest useful next target is not separate norm and mixed residue tables.

> **Joint next-carry lemma.** Prove, on an explicitly specified infinite subset of the original family contained in $\mathcal Z_{64}$, that
> 

$$
> N_0\equiv64\pmod{128},
> \qquad
> H_0+64\mathcal C\equiv64\pmod{128},
>
$$


> with $\mathcal C$ computed from the complete next column lifts and the original finite range.

It would give


$$
N\equiv H\equiv64\pmod{128},
$$


hence


$$
\boxed{\alpha=\gamma=6,\qquad \gamma-\alpha=0}
$$


on that infinite subfamily.

To use Proposition 6.1 for infinitude, the lemma would additionally need a proved finite-residue or carry-language population statement. Local unit periodicity alone does not supply one.

A stronger alternative remains


$$
v_2(H-N)>v_2(N)
$$


on an infinite reachable subfamily. No such comparison is proved here.

---

## 10. Actual denominator and whole evaluated error

The actual center remains


$$
c_n=\frac{2b!}{\lambda R}\frac HN.
$$


With the least actual clearer $d_B$, retain


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
$$


The primitive multiplier on the uncleared quadratic pair is $d_B^2/g_B$.

The exact retained binary interface is


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
\tag{10.1}
$$



**The new results in this report do not change a proved value or bound for $v_2(q_n)$ on $\mathcal Z_{64}$.** They identify the next missing bit needed to obtain such a change.

Even a successful joint next-carry lemma would determine only the binary contribution at its stated indices. The odd-prime support and the final full gcd would remain part of the global obligation.

At the retained scope of the fixed-ratio whole-error theorem,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The whole primitive evaluated error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n>0}
$$


eventually. Neither a local common-unit expansion nor an isolated depth equality proves that this quantity tends to zero.

---

# 11. Bounded calculation for coordinator inspection

No new complete coefficient lift is claimed here. The following bounded audit would verify the new local arithmetic, without repeating the settled fifth contraction.

## A. Translation certificate

**Inputs**

- The 31 previously retained residues.
- $a=84-\rho$ for non-overflow and $a=212-\rho$ for overflow.
- $0\le c\le15$.
- $d,k\bmod128$, or symbolic $d,k$.
- Formula (3.1).

**Required divisions**

For $128/i$, extract the power of two from $i$, then invert its odd part. In (2.1), the binomial denominator is odd.

**Expected output**

A certificate of the congruence (3.1), including its coefficient-weighted use where applicable. This is a local ratio certificate, not a mixed–norm theorem.

## B. Common-unit table

**Inputs**



$$
D\bmod128\ \text{odd},\qquad t\bmod128,\qquad
C=4002D+2532,\qquad k=2C+1.
$$


Use the exact $L_7$-quotients for $w,\tau$, with the overflow borrow retained.

**Expected output**

For each state and each of the 31 residues, record


$$
w,\quad\tau,\quad(w\tau)^2\pmod{256},
$$


together with the exact negative-ratio power of two and odd unit.

There are


$$
64\cdot128\cdot31=253{,}952
$$


local rows. An $O(m)$ prefix table for $O(m)\bmod256$, $0\le m<2^{14}$, makes each $L_7$-evaluation a product of seven table lookups. This is on the order of tens of millions of small modular operations, with a compact binary output of a few megabytes; a verbose textual certificate would be larger. No large factorial is required.

Propositions 5.1 and 6.1 prove the unit-table parameter transfer to original indices. They do not transfer a full auxiliary convolution.

## C. Missing prerequisite for a decisive next computation

Before producing any actual $H\bmod128$ certificate, the coordinator needs a complete lift yielding


$$
2X\bmod128,\qquad 4Y\bmod256,
$$


or an equally strong direct theorem for $\mathcal C$. Its proof must include:

- the new contact correction;
- the complete normalized first forcing at its new precision;
- exterior indices $7,8$;
- the resulting full negative-moment range;
- all finite inverse and parameter-transfer losses;
- newly admitted interior and overflow contributions.

The expected decisive output is then the **joint pair**


$$
\left(N\bmod128,\ H\bmod128\right)
$$


with a proved carry-and-terminal evaluation on an infinite original-domain subfamily—not isolated residues at auxiliary parameters.

---

## Final proof-status ledger

**Proved here:** the modulo-$256$ positive-ratio translation, finite common-unit dependence, exact original $D$-residue reachability, the next joint-carry decomposition, and the stated next contact and factorial-tail corrections.

**Not proved here:** a modulus-$128/256$ mixed–norm relation, a finite-state evaluation of the complete higher convolution, an infinite relative-depth bound on $N\equiv0\pmod{64}$, or a new bound for the actual primitive denominator.

**Exact bottleneck:** evaluate the mixed correction parity $\mathcal C$ jointly with the next norm digit using the complete lifted forces, original finite boundaries, higher-binomial carry units, and terminal conditions.

**Global status:** no unconditional proof of rationality or irrationality of $e+\pi$ follows.
