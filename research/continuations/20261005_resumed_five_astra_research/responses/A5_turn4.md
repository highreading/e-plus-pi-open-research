> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 4 — Corrected finite period and an exact coefficient-contraction program

## Executive result

The individual-parameter assertion in A5 turn 3, §10 is false and is withdrawn:



$$
D,t\bmod512
\quad\text{do not determine}\quad
d=D-t,\ K=k+d\pmod{1024}.
$$



The correct approach here is to use the **safe period $1024$** for both state variables. I prove that this period suffices for all four raw coefficient functions


$$
\mathcal A_{\rm full},\quad \mathcal D_{\rm full},\quad
\mathcal A_{\rm end},\quad \mathcal D_{\rm end}\pmod{1024}.
$$



There is nevertheless a useful, rigorously justified reduction:



$$
\boxed{
(\mathcal A_{\rm full},\mathcal D_{\rm full})(D+512,t+512)
=
(\mathcal A_{\rm full},\mathcal D_{\rm full})(D,t)
\pmod{1024}.
}
\tag{E1}
$$



The terminal functions consequently have period $512$. This diagonal symmetry reduces the required coefficient calculation from $524{,}288$ full states to



$$
\boxed{262{,}144\text{ full states and }256\text{ terminal states}.}
$$



This does **not** prove independent $512$-periodicity in $D$ or $t$.

Below I supply fully specified bounded pseudocode, retaining:

* actual coefficient evaluation at $j=128t+\rho$;
* the actual bounded multipliers $a_s(2n)$ to modulus $1024$;
* all six floor patterns;
* all negative moments through $-10$;
* all $128$ coordinate residues;
* terminal negative-lower zeros;
* odd factorial units and only odd modular inverses.

No computation is executed. In particular, the universal mixed identities are **not asserted to pass**.

If they fail, I give an exact residue-class high-kernel contraction, with a division-safe evaluation rule and the original exponential reachability constraint retained.

---

## 1. Scope and accepted inputs

The original family remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


Set


$$
k=2C+1,\qquad A=2n=128k+4.
$$



The actual finite inverse indices remain


$$
0\le i,j<b.
$$



I reuse the accepted finite transport, its coefficient-valued transfer, the completed contact certificate, and


$$
X,Y\in2\mathbb Z_2^{b+1},\qquad H-N\in64\mathbb Z_2.
$$


I also retain $N>0$ and the established original-family nonvanishing of $H$.

The coefficient representatives used throughout this report are exactly


$$
\begin{aligned}
p={}&(34,31,71,69,48,12,4,4,96,72,120,72,0,64,64,64),\\
\delta={}&(112,102,10,124,16,24,184,0,96,16,80,96,0,128,128,0),\\
\beta={}&(113,202,78,200,248,80,240,128,128).
\end{aligned}
\tag{1.1}
$$



Fixing these representatives matters: the low coefficients are auxiliary normalized quantities. Their representative-independent meaning is supplied by the **complete weighted scalar contraction**, not by an unsupported claim that each normalized coefficient is intrinsically determined at raw precision.

No contact or central forcing computation is repeated. The complete exterior data are retained through $\beta$, including all nine entries. The omitted logarithmic force and later exponential tail remain omitted only under their accepted whole-force and whole-tail bounds.

The factorial stripping and binomial-translation methods used below are classical. No new literature search or execution of the supplied certificates is claimed.

---

## 2. Exact low-state formulas

### 2.1 Coefficients at the actual coordinate

For $0\le s\le15$, define


$$
a_s(A)=\binom{A+s-1}{s},
$$




$$
F_s(x)=a_s(A)\sum_{r=s}^{15}p_r\binom{x}{r-s},
\qquad
G_s(x)=a_s(A)\sum_{r=s}^{15}\delta_r\binom{x}{r-s}.
\tag{2.1}
$$


Zero-extend $F_s$ outside $0\le s\le15$, and put


$$
Z_{-i}(x)=\beta_i\quad(1\le i\le9),\qquad
Z_s(x)=G_s(x)\quad(0\le s\le15),
$$


with zero extension elsewhere.

Then


$$
U_s(x)=F_s(x)+xF_s(x-1)+xF_{s+1}(x-1),
\tag{2.2}
$$




$$
V_s(x)=Z_s(x)+xZ_s(x-1)+xZ_{s+1}(x-1).
\tag{2.3}
$$



The full ranges are


$$
-1\le s\le15\quad\text{for }U,\qquad
-10\le s\le15\quad\text{for }V.
$$



Every evaluation below uses


$$
\boxed{x=j=128t+\rho.}
$$


In particular, neither


$$
U_0(128)-U_0(0)\equiv64\pmod{128}
$$


nor


$$
V_{-2}(x+128)-V_{-2}(x)\equiv128\pmod{256}
$$


is suppressed.

There is no use of $a_s(644)\bmod1024$. The accepted replacement by $644$ has only its previously proved weighted lower-column scope.

### 2.2 Six floor patterns

Write


$$
d=D-t,\qquad K=k+d.
$$


For $0\le\rho<128$, $-10\le s\le15$, set


$$
a_0=\left\lfloor\frac{84-\rho}{128}\right\rfloor,\quad
\ell_0=\left\lfloor\frac{80-\rho-s}{128}\right\rfloor,\quad
c_0=\left\lfloor\frac{4+s}{128}\right\rfloor,
$$


and


$$
a=84-\rho-128a_0,\quad
\ell=80-\rho-s-128\ell_0,\quad
c=4+s-128c_0.
$$



All three remainders lie in $[0,127]$. The six factors are


$$
\begin{array}{c|c}
(a_0,\ell_0,c_0)&P_{\rho s}\\ \hline
(0,0,0)&K\\
(0,-1,0)&Kd\\
(0,0,-1)&Kk\\
(-1,-1,0)&d\\
(-1,0,-1)&k\\
(-1,-1,-1)&dk.
\end{array}
\tag{2.4}
$$



Put


$$
v(q)=v_2(q!)=\sum_{i\ge1}\left\lfloor q/2^i\right\rfloor
\quad(q\ge0),
$$




$$
m_{\rho s}=127(a_0-\ell_0-c_0)+v(a)-v(\ell)-v(c).
\tag{2.5}
$$


This is nonnegative: it is the sum of the seven nonnegative floor discrepancies obtained by stripping the low seven binary levels.

Define


$$
O(m)=\prod_{\substack{1\le r\le m\\r\ {\rm odd}}}r,
\qquad
L_7(m)=\prod_{i=0}^{6}O\!\left(\left\lfloor m/2^i\right\rfloor\right).
$$


For a valid moment,


$$
u_{\rho s}=
\frac{L_7(128K+84-\rho)}
{L_7(128d+80-\rho-s)L_7(128k+4+s)}.
\tag{2.6}
$$



The actual moment is


$$
\mathcal M_s(128t+\rho)
=
\frac{J_d}{k}\,P_{\rho s}2^{m_{\rho s}}u_{\rho s},
\qquad
J_d=\binom{k+d-1}{d}.
\tag{2.7}
$$



At $d=0,\ell_0=-1$, its actual lower argument is negative. The moment is zero, and the program below returns zero **before evaluating any factorial unit**.

### 2.3 Weight and scalar coefficients

Put


$$
\varepsilon_\rho=\mathbf1_{\rho\ge69},\qquad
z_\rho=68-\rho+128\varepsilon_\rho,
$$




$$
b_\rho=127\varepsilon_\rho+v(68)-v(\rho)-v(z_\rho),
$$




$$
w_{\rho,t}=
\frac{L_7(128C+68)}
{L_7(128t+\rho)L_7(128(C-t)+68-\rho)}.
$$



Define


$$
f_{\rho,t}=\sum_{s=-1}^{15}
U_s(128t+\rho)P_{\rho s}2^{m_{\rho s}}u_{\rho s},
$$




$$
g_{\rho,t}=\sum_{s=-10}^{15}
V_s(128t+\rho)P_{\rho s}2^{m_{\rho s}}u_{\rho s}.
\tag{2.8}
$$



The coefficients to evaluate are


$$
\mathcal A_\rho=
2^{2b_\rho}w_{\rho,t}^2(C-t)^{2\varepsilon_\rho}k^{-2}f_{\rho,t}^2,
$$




$$
\mathcal D_\rho=
2^{2b_\rho}w_{\rho,t}^2(C-t)^{2\varepsilon_\rho}k^{-2}f_{\rho,t}g_{\rho,t}.
\tag{2.9}
$$



Finally,


$$
\mathcal A_{\rm full}=\sum_{\rho=0}^{127}\mathcal A_\rho,\qquad
\mathcal D_{\rm full}=\sum_{\rho=0}^{127}\mathcal D_\rho,
$$


and


$$
\mathcal A_{\rm end}(D)=\sum_{\rho=0}^{80}\mathcal A_\rho(D,D),\qquad
\mathcal D_{\rm end}(D)=\sum_{\rho=0}^{80}\mathcal D_\rho(D,D).
\tag{2.10}
$$



All inverses here are odd inverses.

---

## 3. Corrected period theorem

### Theorem 1 — Safe period

Modulo $1024$, the full coefficient functions have period $1024$ separately in $D$ and $t$, on admissible nonnegative representatives. The terminal functions have period $1024$ in $D$.

### Proof

For $p\ge3$, the product of all odd residue classes modulo $2^p$ is $1$. Thus


$$
O(m+2^p)\equiv O(m)\pmod{2^p},
$$


and


$$
L_7(m+2^{p+6})\equiv L_7(m)\pmod{2^p}.
$$


At $p=10$, an $L_7$ value depends only on its argument modulo $65536$.

Under either $D\mapsto D+1024$ or $t\mapsto t+1024$:

1. Every argument in the $L_7$ quotients changes by a multiple of $65536$.
2. The integers $d,K,k,C-t$ are unchanged modulo $1024$.
3. The floors and low remainders depend only on $\rho,s$.
4. A change in $t$ changes $j$ by $2^{17}$.

For a bounded lower index $r\le15$, binomial translation gives


$$
v_2\left(\binom{x+h}{r}-\binom xr\right)
\ge v_2(h)-\lfloor\log_2r\rfloor.
\tag{3.1}
$$


Thus a $2^{17}$-shift preserves every binomial used in (2.1) modulo $1024$, with ample margin. The explicit factor $x$ in (2.2)–(2.3) is also preserved.

A $1024$-shift of $D$ changes


$$
A=256C+132
$$


by


$$
256\cdot4002\cdot1024,
$$


whose valuation is $19$. Therefore every actual bounded $a_s(A)$, $s\le15$, is preserved modulo $1024$.

All factors in (2.9) are consequently preserved.

For terminal coefficients, set $t=D$. The same argument applies to nonzero moments; the zero moments remain exactly zero because $d=0$ remains fixed. ∎

### What this corrects

Under $D\mapsto D+512$, with $t$ fixed,


$$
d\mapsto d+512,\qquad K\mapsto K+512\pmod{1024}.
$$


These individual factors are not invariant. The previous proof of independent $512$-periodicity is therefore not valid.

I do not replace that missing proof by an assumption about weighted cancellation.

---

## 4. A proved symmetry reducing the table by half

### Theorem 2 — Diagonal half-period

For the full coefficients,


$$
(\mathcal A_{\rm full},\mathcal D_{\rm full})(D+512,t+512)
\equiv
(\mathcal A_{\rm full},\mathcal D_{\rm full})(D,t)
\pmod{1024}.
\tag{4.1}
$$


For the terminal coefficients,


$$
(\mathcal A_{\rm end},\mathcal D_{\rm end})(D+512)
\equiv
(\mathcal A_{\rm end},\mathcal D_{\rm end})(D)
\pmod{1024}.
\tag{4.2}
$$



### Proof

Under the simultaneous shift,


$$
d'=d,
$$




$$
C'-C=4002\cdot512,
\qquad
k'-k=8004\cdot512.
$$


Both latter changes are divisible by $1024$. Hence $K,d,k$, and every six-case factor $P_{\rho s}$, are preserved modulo $1024$.

All factorial-unit arguments change by multiples of $65536$. Also,


$$
j'-j=65536,
$$


so (3.1) preserves the bounded coefficient evaluations modulo $1024$. The change in $A$ has valuation $18$, sufficient for every $a_s(A)$.

The only remaining factor is $C-t$:


$$
(C'-t')-(C-t)=4001\cdot512.
$$


It need not be invariant modulo $1024$, but its square is:


$$
(x+512h)^2-x^2
=1024hx+262144h^2\equiv0\pmod{1024}.
$$


Since (2.9) uses only $(C-t)^0$ or $(C-t)^2$, the claimed symmetry follows.

At the terminal boundary the same shift preserves $d=0$, including every exact negative-lower zero. ∎

### Table representatives

Every orbit under (4.1) has a unique representative with


$$
D\bmod1024\in\{1,3,\ldots,511\},\qquad
t\bmod1024\in\{0,\ldots,1023\}.
\tag{4.3}
$$



For safe, positive full-block evaluation use


$$
D=D_0+2048,\qquad t=t_0+1024.
\tag{4.4}
$$


Then $t<D$, $d\ge2$, and all required factorial arguments are nonnegative.

For terminal evaluation use $D=D_0+2048,\ t=D$.

These are representatives for **auxiliary low coefficients**, not replacements for the actual original high kernels.

---

## 5. Fully specified bounded pseudocode

All modular quantities below are reduced modulo


$$
M=1024.
$$



`choose_exact(x,r)` means the integer-valued binomial polynomial:


$$
\binom xr=\frac{x(x-1)\cdots(x-r+1)}{r!}
$$


computed by exact integer arithmetic before reduction. It supports $x=-1$, which can arise in a direct boundary audit. It uses no modular inverse of $r!$.

```text
M = 1024

p     = [34,31,71,69,48,12,4,4,96,72,120,72,0,64,64,64]
delta = [112,102,10,124,16,24,184,0,96,16,80,96,0,128,128,0]
beta  = [113,202,78,200,248,80,240,128,128]

function invodd(x):
    x = x mod M
    assert x is odd
    return inverse of x modulo M by extended Euclidean algorithm

function choose_exact(x, r):
    assert r >= 0
    numerator = product(x-i, i=0,...,r-1)   # empty product = 1
    denominator = product(i, i=1,...,r)     # empty product = 1
    assert numerator is exactly divisible by denominator
    return numerator / denominator        # exact integer division

function vf(q):
    assert q >= 0
    ans = 0
    while q > 0:
        q = floor(q/2)
        ans += q
    return ans

# Odd-prefix table.  O(m) modulo M depends on m modulo 1024.
oddprefix[0] = 1
for r = 1,...,1023:
    oddprefix[r] = oddprefix[r-1]
    if r is odd:
        oddprefix[r] = oddprefix[r] * r mod M

function L7(m):
    assert m >= 0
    ans = 1
    for i = 0,...,6:
        ans = ans * oddprefix[(floor(m/2^i)) mod 1024] mod M
    return ans

function columns(A, x):
    for s = 0,...,15:
        aa[s] = choose_exact(A+s-1, s) mod M

    function F(s, y):
        if s < 0 or s > 15: return 0
        return aa[s] *
               sum(p[r] * choose_exact(y,r-s), r=s,...,15) mod M

    function Z(s, y):
        if -9 <= s <= -1:
            return beta[-s-1]
        if 0 <= s <= 15:
            return aa[s] *
                   sum(delta[r] * choose_exact(y,r-s), r=s,...,15) mod M
        return 0

    for s = -1,...,15:
        U[s] = (F(s,x) + x*F(s,x-1) + x*F(s+1,x-1)) mod M
    for s = -10,...,15:
        V[s] = (Z(s,x) + x*Z(s,x-1) + x*Z(s+1,x-1)) mod M

    return U,V

function moment_factor(C, k, d, K, rho, s):
    upper = 128*K + 84-rho
    lower = 128*d + 80-rho-s
    complement = 128*k + 4+s

    assert upper == lower + complement

    # Exact terminal convention, before any factorial-unit evaluation.
    if lower < 0:
        assert d == 0
        return 0
    assert upper >= 0 and complement >= 0

    a0 = floor((84-rho)/128)
    l0 = floor((80-rho-s)/128)
    c0 = floor((4+s)/128)

    a = 84-rho-128*a0
    l = 80-rho-s-128*l0
    c = 4+s-128*c0
    assert 0 <= a,l,c < 128

    pattern = (a0,l0,c0)
    if pattern == ( 0, 0, 0): P = K
    elif pattern == ( 0,-1, 0): P = K*d
    elif pattern == ( 0, 0,-1): P = K*k
    elif pattern == (-1,-1, 0): P = d
    elif pattern == (-1, 0,-1): P = k
    elif pattern == (-1,-1,-1): P = d*k
    else: fail("unlisted floor pattern")

    m = 127*(a0-l0-c0) + vf(a)-vf(l)-vf(c)
    assert m >= 0
    if m >= 10: return 0

    unit = L7(upper) * invodd(L7(lower)) *
           invodd(L7(complement)) mod M

    return P * 2^m * unit mod M

function row(C, k, A, D, t, rho):
    d = D-t
    K = k+d
    x = 128*t+rho
    U,V = columns(A,x)

    f = 0
    g = 0
    for s = -10,...,15:
        h = moment_factor(C,k,d,K,rho,s)
        if s >= -1:
            f = (f + U[s]*h) mod M
        g = (g + V[s]*h) mod M

    eps = 0 if rho <= 68 else 1
    z = 68-rho+128*eps
    depth = 127*eps + vf(68)-vf(rho)-vf(z)
    assert depth >= 0

    # Exact raw-weight depth pruning only.
    if 2*depth >= 10:
        return (0,0)

    w = L7(128*C+68) *
        invodd(L7(128*t+rho)) *
        invodd(L7(128*(C-t)+68-rho)) mod M

    scale = 2^(2*depth) * w*w * invodd(k)^2 mod M
    if eps == 1:
        scale = scale*(C-t)^2 mod M

    return (scale*f*f mod M, scale*f*g mod M)

function block(D,t,last_rho):
    C = 4002*D+2532
    k = 2*C+1
    A = 128*k+4
    asum = 0
    dsum = 0

    for rho = 0,...,last_rho:
        ar,dr = row(C,k,A,D,t,rho)
        asum = (asum+ar) mod M
        dsum = (dsum+dr) mod M

    return asum,dsum

for D0 in [1,3,...,511]:
    Drep = D0+2048
    for t0 = 0,...,1023:
        trep = t0+1024
        assert trep < Drep
        FULL[D0,t0] = block(Drep,trep,127)

    END[D0] = block(Drep,Drep,80)
```

### Precision and size remarks

1. `aa[s]` is computed from the representative’s actual $A$, not from $644$.
2. Every `choose_exact` has lower index at most $15$. Large factorials are never formed.
3. `L7` uses seven table accesses, not an unbounded product.
4. There is no negative factorial and no even modular inverse.
5. The depth pruning only removes a row whose explicit raw factor $2^{2b_\rho}$ already vanishes modulo $1024$. It does not discard weight-depth-four coordinates.
6. A practical implementation should cache `aa`, the two short binomial arrays at $x,x-1$, and the fixed floor data. These are optimizations, not additional hypotheses.

The outer state count is $262{,}144$. There are $33{,}554{,}432$ full residue rows before pruning, plus $20{,}736$ terminal residue rows.

---

## 6. Required output and a reviewable certificate

The program should output:

1. The ordered pairs in `FULL` and `END`.
2. The residue image and frequency distribution of each component.
3. The complete list of states with nonzero mixed component.
4. The minimum capped dyadic depth of each component:
   

$$
\min(10,v_2(r)),\qquad v_2(0):=\infty.
$$


5. A small selection of expanded row records, including
   

$$
(\rho,s)=(85,-10),
$$


   which tests the $(-1,0,-1)$ pattern.
6. Explicit terminal records showing that every negative actual lower argument was returned as zero before unit evaluation.

The sufficient universal identities are now correctly stated as


$$
\mathcal D_{\rm full}(D,t)\equiv0\pmod{1024}
$$


for the reduced representatives (4.3), and


$$
\mathcal D_{\rm end}(D)\equiv0\pmod{1024}
$$


for odd $D\bmod512$.

**An all-zero output is a proposition to test, not a prediction.**

### A smaller first probe

Before producing a large table, inspect full blocks at


$$
(D_0,t_0)\in
\{1,3,5,7\}\times\{0,1,2,3,511,512,1023\},
$$


and the corresponding four terminal states.

These $28$ full probes can reveal a failure of the sufficient identity quickly. They cannot establish it universally.

The diagonal symmetry should also be checked on those probes by independent evaluations at $(D+512,t+512)$. Such checks corroborate the proof; they are not its basis.

### Further depth reduction: a precise follow-on lemma

A useful next lemma, directly testable from this program, is:

> Determine the greatest common dyadic divisor of the complete full mixed coefficients and separately of the terminal mixed coefficients on the proved finite state space.

If, for example, all mixed coefficients are divisible by $2^h$, the remaining high-kernel contraction needs only precision $2^{10-h}$. No value of $h$ beyond what has actually been proved or exhaustively checked should be assumed from the old modulus-$512$ alignment.

The diagonal symmetry is the unconditional table reduction established here. Additional coefficient depth remains an arithmetic question.

---

## 7. Complete scalar meaning, including finite endpoints

The retained common higher kernel is


$$
\mathcal B_t=\binom Ct\binom{2C+D-t}{D-t}.
$$


The exact original ranges give


$$
4N\equiv
\sum_{t=0}^{D-1}\mathcal B_t^2\mathcal A_{\rm full}(D,t)
+\mathcal B_D^2\mathcal A_{\rm end}(D)
\pmod{1024},
\tag{7.1}
$$




$$
8(H-N)\equiv
\sum_{t=0}^{D-1}\mathcal B_t^2\mathcal D_{\rm full}(D,t)
+\mathcal B_D^2\mathcal D_{\rm end}(D)
\pmod{1024}.
\tag{7.2}
$$



The actual exterior point remains


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


Its $+1$ is retained. The accepted endpoint bounds imply zero contribution to both raw congruences modulo $1024$.

Only after the **whole** sums are assembled may one divide (7.1) by $4$ and (7.2) by $8$. These are exact divisions of divisible residue classes, not modular inversions.

If all tested universal mixed coefficients vanish over the complete proved finite state space, then (7.2) proves


$$
H-N\equiv0\pmod{128}
$$


on the original family.

---

## 8. If the universal identities fail: exact high-kernel contraction

A nonzero low coefficient is not a counterexample to original-family alignment. It can be annihilated by $\mathcal B_t^2$, or canceled by other $t$-terms.

Here is a precise contraction separating those issues.

For actual $D,C$, define


$$
P_a(z)=
\sum_{\substack{0\le t\le D\\t\equiv a\ (1024)}}
\binom Ct^{\,2}z^t,
\qquad 0\le a<1024,
$$


and


$$
Q(z)=\sum_{d=0}^{D}\binom{2C+d}{d}^{\,2}z^d.
$$


Work in


$$
(\mathbb Z/1024\mathbb Z)[z]/(z^{D+1}).
$$



Set


$$
R_a(D)=[z^D]P_a(z)Q(z).
\tag{8.1}
$$


Then


$$
R_a(D)=
\sum_{\substack{0\le t\le D\\t\equiv a\ (1024)}}\mathcal B_t^2
\pmod{1024}.
$$



Writing $d_a=\mathcal D_{\rm full}(D,a)$ and $e=\mathcal D_{\rm end}(D)$, the complete raw discrepancy is exactly


$$
\boxed{
T(D)=
\sum_{a=0}^{1023}d_aR_a(D)
+\binom CD^{\,2}\bigl(e-d_{D\bmod1024}\bigr)
\pmod{1024}.
}
\tag{8.2}
$$


The last term replaces the artificial full terminal block by the actual shortened block. The same formula with $\mathcal A$ gives the norm contraction.

This is an exact residue-class convolution, not a truncation of the original $t$-range.

### Division-safe binomial evaluation for this contraction

For nonnegative $m$, define


$$
E(m)=m-s_2(m),\qquad
U(m)=\prod_{i\ge0}O(\lfloor m/2^i\rfloor)\pmod{1024}.
$$


The product is finite. Then, for $0\le r\le m$,


$$
e=E(m)-E(r)-E(m-r),
$$


and


$$
\binom mr\equiv
\begin{cases}
0,&e\ge10,\\
2^eU(m)U(r)^{-1}U(m-r)^{-1},&e<10
\end{cases}
\pmod{1024}.
\tag{8.3}
$$


Every inverse is odd.

Because the kernels are squared, an individual summand vanishes once


$$
v_2\binom Ct+
v_2\binom{2C+D-t}{D-t}\ge5.
\tag{8.4}
$$


This is a valid high-kernel filter, separate from the low-coordinate filter.

Equations (8.1)–(8.4) specify the remaining contraction exactly. They do not claim a uniformly small computation for enormous original $D$.

### Original reachability is retained

The required theorem is not $T(D)=0$ for arbitrary odd $D$, but


$$
\boxed{
T\!\left(\frac{9^{18+32u}-81}{128}\right)=0
\quad\text{for every }u\ge0.
}
\tag{8.5}
$$



Equivalently, the reachable integers satisfy the exact recurrence


$$
D_{u+1}
=
9^{32}D_u+\frac{81(9^{32}-1)}{128},
\qquad
D_0=\frac{9^{18}-81}{128}.
\tag{8.6}
$$



Although all odd residues modulo a fixed power of two are populated, this does not make the complete high kernels arbitrary or periodic. A small auxiliary odd $D$ with $T(D)\ne0$ would not refute (8.5).

Thus, if the sufficient coefficient identity fails, the concrete follow-on obligation is to prove (8.5) using the exact contraction (8.2), or to exhibit an actual $u\ge0$ with nonzero complete $T(D_u)$. Even the latter would disprove only the proposed new alignment, not irrationality of $e+\pi$.

---

## 9. Final gcd, primitive denominator, and whole evaluated error

No normalization changes.

With the least actual clearer $d_B$, retain


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$


and the full gcd


$$
g_B=\gcd(A_B,|H_B|).
$$


The actual primitive pair is


$$
q_n=A_B/g_B>0,\qquad p_n=H_B/g_B,
$$


with primitive multiplier $d_B^2/g_B$.

For


$$
\alpha=v_2(N),\qquad\gamma=v_2(H),
$$


the retained exact interface is


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
\tag{9.1}
$$



A successful new alignment would imply $\gamma=\alpha$ where $\alpha\le6$, but only $\alpha,\gamma\ge7$ where both vanish modulo $128$. It would not control the odd-prime part of the full gcd.

At the accepted scope of the whole-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The entire primitive evaluated error remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n>0}
\quad\text{eventually}.
\tag{9.2}
$$



Nothing proved here makes this whole nonzero quantity tend to zero.

---

## 10. Final ledger

### New rigorous results

1. The unsupported individual $512$-state assertion is corrected.
2. A sufficient separate period $1024$ is proved for the raw full coefficients.
3. A diagonal half-period is proved, reducing the universal table to
   

$$
262{,}144\text{ full states and }256\text{ terminal states}.
$$


4. A complete bounded arithmetic specification is supplied with all floors, negative moments, actual bounded $a_s(A)$, actual coordinate evaluation, and terminal zeros.
5. An exact residue-class high-kernel contraction is supplied for any residual discrepancy, including the shortened terminal block and the original reachability recurrence.

### Not established

The coefficient table has not been evaluated. Therefore this report proves neither


$$
H-N\equiv0\pmod{128}
$$


nor its failure on the original family. No new norm digit, valuation equality, primitive-denominator estimate, or irrationality result is assigned.

### Exact next calculation

Use the vectors (1.1), the bounded program in §5, and the representatives (4.3)–(4.4). The verifiable output is the complete coefficient-pair table, its mixed exceptional-state list, and its capped depth distributions.

If the complete mixed output is zero, the new alignment follows immediately from (7.2). If not, the remaining mathematical bottleneck is precisely (8.5), evaluated through the full high-kernel contraction—not another contact calculation.

Beyond that carry remain unrestricted relative valuation, the full final gcd, and a sufficient same-index bound for the whole primitive error.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


