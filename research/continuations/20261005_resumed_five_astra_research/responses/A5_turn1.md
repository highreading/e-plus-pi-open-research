> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — complete exterior lift, a new degree-eight contact term, and the remaining coefficient obstruction

## 1. Result and scope

I reuse, without reproving, the accepted theorem


$$
H\equiv N\pmod{64}
$$


on


$$
\boxed{
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
}
$$


The original parameters remain


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$


with $D$ odd and $C\equiv2\pmod4$.

**This report does not complete the actual $P_{128},Q_{256}$ coefficient lift, and therefore does not evaluate the joint carry $\mathcal C(X,Y)$.** In particular, I do not claim a new mixed–norm congruence modulo $128$ or $256$.

The new rigorous results are:

1. The contact polynomial has the stronger, explicitly nontrivial lift
   

$$
\boxed{\phi^n\equiv1+66U+64U^2\pmod{256}.}
$$


   In divided-power coordinates, the last term introduces degrees $5,7,8$, as well as degree $2$.

2. All nine exterior forcing values modulo $256$ are evaluated:
   

$$
\boxed{
   (B_0,\ldots,B_8)
   =(197,234,54,56,248,208,112,128,128)\pmod{256}.
   }
$$



3. The complete exterior negative-moment coefficients are evaluated. Reconstruction genuinely extends the negative range to
   

$$
\boxed{-10\le s<0,}
$$


   and its two newly exposed coefficients are not identically zero modulo $256$.

4. A precision-safe central and first-forcing truncation is proved at modulus $256$: central summation index $s\le9$, central coefficient index $\ell\le10$, and forcing index $i\le17$. These are conservative bounds, not purported sharp support.

5. A new sufficient high-weight exclusion is proved:
   

$$
\boxed{
   v_2(W_j)\ge5
   \Longrightarrow
   X_j^2\equiv X_jY_j\equiv0\pmod{256}
   \quad(0\le j<b).
   }
$$


   I do **not** retain the old 31-class cutoff at the new precision.

These advances expose an additional obstruction beyond the turn0 handoff: **at raw modulus $256$, the contact operator is no longer merely a changed scalar multiple of the old degree-four operator.** Its degree-eight correction must be transported through the actual finite contact construction, exterior insertion, and inverse.

No table of mixed–norm states is proposed before that transport is proved.

---

## 2. Verification gate and unchanged arithmetic objects

The supplied overlap gate and the accepted parent theorem are retained at their stated scopes. I have no browsing, archive-access, or execution facility in this response; I therefore do not claim an additional external search, hash verification, or executed certificate.

The calculations below use the displayed central formulas, integral divided-power arithmetic, finite binomial identities, and the retained reconstruction interface. Classical factorial stripping and Lucas–Kummer arithmetic are reused, not offered as new general theorems.

Keep


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad
N=X^TX,\qquad H=X^TY,
$$


and


$$
W_j=\binom{n+2}{j},\qquad
\Omega=\operatorname{diag}\bigl((n+2)_{\underline j}^{\,2}\bigr)_{0\le j\le b}.
$$


All actual contact inverses have indices


$$
0\le i,j<b.
$$


The retained integrality is


$$
X,Y\in2\mathbb Z_2^{b+1}.
$$



For clarity about target precision:

- $X,Y\bmod64$ suffice to determine $N,H\bmod128$.
- They also suffice for $N\bmod256$, because $X$ is even.
- They do **not**, without an additional argument, suffice for $H\bmod256$.

Indeed, changing $X,Y$ by $64a,64b$ changes the mixed product by


$$
64(ay+bx)+4096ab,
$$


whose valuation can be exactly $7$ when $x,y$ are even. Thus a full modulus-$256$ mixed theorem requires either stronger columns or a separate cancellation theorem for this next correction. The raw $P_{128},Q_{256}$ lift is the immediate prerequisite for the modulus-$128$ joint problem; it should not be mislabeled as automatically determining $H\bmod256$.

---

# Part I. The contact polynomial at the actual new precision

## 3. Divided-power factorial divisibility

Write


$$
h=\frac n2,\qquad
\phi^2=1+2U,
$$


where


$$
U=-x+x^2-\frac{x^3}{2}+\frac{x^4}{8}
$$


has integral divided-power coefficients


$$
(u_1,u_2,u_3,u_4)=(-1,2,-3,3).
$$



I use the following elementary property of the integral divided-power ring:


$$
\boxed{U^j\in j!\,\mathbb Z_2\langle x\rangle.}
\tag{3.1}
$$


One justification is to expand $U^j$ by multiplicities of its positive-degree terms. After division by $j!$, the coefficient associated with multiplicities $m_a$, $\sum m_a=j$, is an integer multiple of


$$
\frac{(\sum a m_a)!}
     {\prod_a(a!)^{m_a}m_a!}.
$$


This integer counts partitions of a labeled set into unlabeled blocks having the specified sizes. Thus the division by $j!$ is coefficientwise integral.

Consequently,


$$
2^j\binom hjU^j
$$


has coefficientwise valuation at least


$$
j+v_2\bigl((h)_{\underline j}\bigr).
\tag{3.2}
$$



On the actual domain,


$$
h\equiv161\pmod{256},
\qquad v_2(h-1)=5,\qquad v_2(h-3)=1.
$$



For $3\le j\le7$, the falling product contains $h-1$, so (3.2) is at least $8$. For $j\ge8$, the factor $2^j$ is sufficient. Hence every term with $j\ge3$ vanishes modulo $256$.

## 4. The exact contact lift modulo $256$

The first two nonconstant terms are


$$
2hU,\qquad 4\binom h2U^2=2h(h-1)U^2.
$$


Since


$$
2h=n\equiv322\pmod{512},
$$


we have


$$
2h\equiv66\pmod{256}.
$$


Also


$$
2h(h-1)\equiv2\cdot161\cdot160\equiv64\pmod{256}.
$$



Therefore


$$
\boxed{
\phi^n=(1+2U)^h
\equiv1+66U+64U^2\pmod{256}.
}
\tag{4.1}
$$



This reduces to the retained turn0 formula


$$
\phi^n\equiv1+66U\pmod{128},
$$


because $U^2$ is even in the divided-power ring.

### 4.1 The degree-eight correction is explicit

Put


$$
V=\frac{U^2}{2}\in\mathbb Z_2\langle x\rangle.
$$


Its divided-power coefficients in degrees $2,\ldots,8$ are


$$
\boxed{(1,-6,24,-75,180,-315,315).}
\tag{4.2}
$$


Thus


$$
V\equiv x^{[2]}+x^{[5]}+x^{[7]}+x^{[8]}\pmod2.
$$


Equation (4.1) becomes


$$
\boxed{
\phi^n\equiv
1+66U+
128\bigl(x^{[2]}+x^{[5]}+x^{[7]}+x^{[8]}\bigr)
\pmod{256}.
}
\tag{4.3}
$$



This is an actual contact correction, not an optional higher-order remainder.

### 4.2 Precise implication for the outstanding lift

The old operator $\mathscr E_{n,b}$ in the packet is written for the four coefficients of $U$. At modulus $256$, a complete actual contact derivation must additionally transport the divided-power coefficients in (4.3).

It is not sufficient to:

- replace $-2\mathscr E$ by $-66\mathscr E$;
- keep the former degree-four boundary polynomial;
- append only $f_7,f_8$ to the exterior force.

The degree-eight contact insertion and its induced finite-boundary terms are separate from the new factorial tail.

---

# Part II. The entire nine-entry exterior force

## 5. Factorial products and whole-tail cutoff

Let


$$
f_a=\frac{(b+a)!}{b!}.
$$


Since $b\equiv209\pmod{256}$, direct multiplication gives


$$
\boxed{
(f_0,\ldots,f_8)
=(1,210,22,56,152,16,112,128,128)\pmod{256}.
}
\tag{5.1}
$$



The relevant valuations are


$$
\begin{array}{c|rrrrrrrrr}
a&0&1&2&3&4&5&6&7&8\\ \hline
v_2(f_a)&0&1&1&3&3&4&4&7&7.
\end{array}
$$


Because $b+9\equiv218\pmod{256}$,


$$
v_2(f_9)=8.
$$


Every subsequent product contains $f_9$. Therefore


$$
\boxed{f_a\equiv0\pmod{256}\qquad(a\ge9).}
\tag{5.2}
$$



This proves the entire exponential-tail cutoff before application of integral finite operators.

The retained estimate


$$
v_2(h_i^F/b!)
\ge2000b+2-2\lfloor\log_2(8005b-1)\rfloor
$$


is greater than $8$ on the original domain. Thus the **whole logarithmic force**, not selected pieces, is absent at this fixed raw precision.

## 6. All nine exterior values

Define


$$
B_a=\sum_{u=a}^{8}f_u\binom{2n}{u-a},
\qquad0\le a\le8.
\tag{6.1}
$$


Here


$$
2n\equiv644\pmod{1024}.
$$


For $0\le k\le8$,


$$
v_2\left(\binom{2n}{k}-\binom{644}{k}\right)
\ge10-\lfloor\log_2k\rfloor.
$$


For every nonconstant term of (6.1), the accompanying $f_u$ supplies at least one additional bit. Hence replacing the bounded binomial factor by its $644$-value is valid modulo $256$ in every summand.

The needed binomial residues are


$$
\boxed{
\left(\binom{644}{k}\right)_{k=0}^{8}
=(1,132,198,132,225,128,64,128,144)\pmod{256}.
}
\tag{6.2}
$$


Substitution yields


$$
\boxed{
(B_0,\ldots,B_8)
=(197,234,54,56,248,208,112,128,128)
\pmod{256}.
}
\tag{6.3}
$$



Their reduction modulo $128$ is exactly


$$
(69,106,54,56,120,80,112,0,0),
$$


as required by the accepted lower interface.

This agreement is a consistency check. The proof of the new values is the complete nine-term calculation and transfer above.

---

## 7. Complete negative-moment coefficients

The exterior-to-moment transformation is unchanged algebraically:


$$
\beta_k
=\sum_{a=k-1}^{8}(-1)^aB_a\binom a{k-1},
\qquad1\le k\le9.
\tag{7.1}
$$


Using all nine entries in (6.3),


$$
\boxed{
(\beta_1,\ldots,\beta_9)
=(113,202,78,200,248,80,240,128,128)
\pmod{256}.
}
\tag{7.2}
$$



Thus the exterior part before reconstruction has moments


$$
-9\le s\le-1.
$$


Write $Z_{-k}=\beta_k$. The reconstruction identity remains


$$
V_s(x)=Z_s(x)+xZ_s(x-1)+xZ_{s+1}(x-1).
\tag{7.3}
$$



The complete strictly negative coefficients independent of the still-uncomputed nonnegative polynomial lift are


$$
\boxed{
\begin{array}{c|l}
s&V_s(x)\pmod{256}\\ \hline
-10&128x\\
-9&128\\
-8&128+112x\\
-7&240+64x\\
-6&80+72x\\
-5&248+192x\\
-4&200+22x\\
-3&78+24x\\
-2&202+59x\\
-1&113+113x+xZ_0(x-1).
\end{array}}
\tag{7.4}
$$



Here $Z_0$ must come from the complete lifted difference polynomial. It is deliberately not replaced by the old coefficient vector.

Two points are decisive:

- The reconstructed coefficient of $\mathcal M_{-9}$ is the nonzero constant $128$.
- The coefficient of $\mathcal M_{-10}$ is $128x$.

Therefore the former range $-8\le s$ is not an adequate whole-force interface at modulus $256$.

---

# Part III. A rigorous bounded first-forcing prerequisite

## 8. Conservative central truncations modulo $256$

Use the exact central formulas supplied in turn20. Their scalar summation coefficients satisfy


$$
v_2\!\left(\frac{2^s(s!)^2}{(2s)!}\right)
=
v_2\!\left(\frac{2^s(s!)^2}{(2s+1)!}\right)
=v_2(s!).
$$


Since


$$
v_2(10!)=8,
$$


every central summand with $s\ge10$ vanishes modulo $256$. Thus


$$
\boxed{0\le s\le9}
\tag{8.1}
$$


suffices at this precision.

For the central coefficient index, the prefactor for odd $\ell=2j+1$ contains $(h)_{\underline{j+1}}$, and for even $\ell=2j$ it contains $(h)_{\underline j}$.

A falling product of length at least six contains


$$
h-1,\quad h-3,\quad h-5,
$$


whose valuations are respectively


$$
5,\quad1,\quad2.
$$


Its valuation is therefore at least $8$. The central sums are $2$-integral, so


$$
\boxed{
B_\ell^{\rm cen}\equiv0\pmod{256}
\qquad(\ell\ge11).
}
\tag{8.2}
$$


Indices beyond the original central coefficient range remain zero by definition.

This argument establishes a complete tail. It does not extrapolate from finitely many zero entries.

## 9. A complete, conservative forcing-index cutoff

The exact first forcing is


$$
\frac{f_i^0}{R}
=
\sum_{\ell=0}^{i}
\binom i\ell
\left(\prod_{t=\ell+1}^{i}(n+t)\right)
B_\ell^{\rm cen}.
\tag{9.1}
$$


By (8.2), only $\ell\le10$ remains modulo $256$.

For every such $\ell$ and every $i\ge18$, the product in (9.1) contains


$$
\prod_{t=11}^{18}(n+t).
$$


Since $n\equiv322\pmod{512}$, the valuations over this eight-factor block are


$$
(0,1,0,4,0,1,0,2),
$$


whose sum is $8$. Therefore


$$
\boxed{
f_i^0/R\equiv0\pmod{256}
\qquad(i\ge18).
}
\tag{9.2}
$$



Thus a complete signed Newton forcing polynomial modulo $256$ has degree at most $17$. This is a proved conservative degree bound, not the final degree of the inverse solution.

## 10. Parameter transfer for this bounded forcing

To evaluate the bounded central formulas uniformly at modulus $256$, take


$$
h_0\equiv h\pmod{2048},\qquad 0\le h_0<2048,
\qquad n_0=2h_0.
$$


For $s\le9$,


$$
v_2\left(\binom{h+\delta}{s}-\binom hs\right)
\ge11-\lfloor\log_2 9\rfloor=8
$$


when $2048\mid\delta$. The prefactors are integral polynomials, so they introduce no further loss.

Accordingly, every retained central term transfers modulo $256$ to $h_0$. Every product in (9.1), for $i\le17$, is an integral polynomial in $n$, and $n-n_0$ is divisible by $4096$. The complete bounded first forcing therefore transfers as well.

There are only eight possible residues


$$
h_0=161+256a,\qquad0\le a<8,
\tag{10.1}
$$


before imposing any additional original-domain restrictions. Covering all eight is a harmless over-cover for a coefficient certificate.

This closes the **boundedness and uniform transfer prerequisites** for computing the new first forcing. It does not compute the subsequent actual finite contact inverse.

---

# Part IV. New support precision and overflow safeguards

## 11. A valid new high-weight cutoff

The accepted lower moment formulas give, modulo $2$,


$$
\mathcal F_j\equiv
\begin{cases}
0,&j\equiv0\pmod4,\\
\mathcal M_0(j),&j\equiv1,2\pmod4,\\
\mathcal M_{-1}(j),&j\equiv3\pmod4,
\end{cases}
$$


and


$$
\mathcal G_j\equiv
\begin{cases}
\mathcal M_{-1}(j),&j\text{ even},\\
\mathcal M_{-2}(j),&j\text{ odd}.
\end{cases}
$$


Only these retained parity statements are needed here; no new coefficient lift is inferred from them.

Let $w=v_2(W_j)$.

- If $w\ge6$, the raw mixed-defect product has valuation at least $12$, which is more than sufficient.
- If $w=5$, one extra parity factor is needed to make
  

$$
W_j^2\mathcal F_j\mathcal G_j
$$


  divisible by $2^{11}$.

For even $j$, $\mathcal M_{-1}(j)$ is even by the same low-bit carry used in the accepted proof. For $j\equiv3\pmod4$, $\mathcal M_{-2}(j)$ is even.

For $j=4k+1$, use the exact retained identity


$$
w=2+v_2\binom{M-1}{k},\qquad M=\frac{n+2}{4}.
$$


Here $v_2(M-1)=4$. If $k$ were odd, then


$$
\binom{M-1}{k}
=\frac{M-1}{k}\binom{M-2}{k-1}
$$


would have valuation at least $4$, forcing $w\ge6$. Therefore $w=5$ forces $k$ even. Since $m=(b-1)/4$ is even, $\ell=m-k$ is even, and the retained Lucas calculation gives $\mathcal M_0(j)$ even.

Thus in every case $w=5$,


$$
\mathcal F_j\mathcal G_j\equiv0\pmod2.
$$



With the actual reconstruction normalizations, this proves


$$
X_j(Y_j-X_j)\equiv0\pmod{256}
\qquad(w\ge5).
$$


Also $2X_j=W_jD_j^P$, with $D_j^P$ integral, gives


$$
v_2(X_j)\ge w-1\ge4,
$$


so $X_j^2\equiv0\pmod{256}$. Consequently,


$$
\boxed{
v_2(W_j)\ge5
\Longrightarrow
X_j^2\equiv X_jY_j\equiv0\pmod{256}.
}
\tag{11.1}
$$



This is the new precision-specific cutoff. It leaves weight-depth-four coordinates potentially active.

### 11.1 What is not asserted

I have not exhaustively enumerated the residues with actual weight depth at most four. In particular, I do not assert that the old 31 residue classes suffice.

A safe interim range is all residues $0\le\rho<128$, with


$$
j=128t+\rho<b,
$$


that is,


$$
\begin{cases}
0\le t\le D,&0\le\rho\le80,\\
0\le t\le D-1,&81\le\rho\le127.
\end{cases}
\tag{11.2}
$$


The endpoint $j=b=128D+81$ is separate.

---

## 12. Why newly extended negative moments change overflow bookkeeping

For an actual interior coordinate, write


$$
j=128t+\rho,\qquad d=D-t,\qquad k=2C+1,\qquad K=k+d.
$$


The moment remains


$$
M_s(\rho,t)
=
\binom{128K+84-\rho}
      {128d+80-\rho-s}.
\tag{12.1}
$$



For the full negative range $-10\le s\le-1$, define exact low-block floors


$$
a_0=\left\lfloor\frac{84-\rho}{128}\right\rfloor,\qquad
\ell_0=\left\lfloor\frac{80-\rho-s}{128}\right\rfloor,\qquad
c_0=\left\lfloor\frac{4+s}{128}\right\rfloor,
$$


and corresponding remainders $a,\ell,c\in[0,127]$.

Seven-level stripping gives the high factorial quotient


$$
\boxed{
\frac{(K+a_0)!}{(d+\ell_0)!\,(k+c_0)!},
}
\tag{12.2}
$$


multiplied by its explicit power of two and odd $L_7$-quotient. A negative actual lower argument means the original binomial is zero; it must be handled as zero before factorial stripping.

The point is that $a_0,\ell_0,c_0$ need not coincide with the old two overflow patterns.

For example, take


$$
\rho=85,\qquad s=-10.
$$


Then


$$
a_0=-1,\qquad \ell_0=0,\qquad c_0=-1.
$$


The high quotient is


$$
\frac{(K-1)!}{d!(k-1)!}
=\binom{K-1}{d}.
\tag{12.3}
$$


It is **not** the former overflow kernel $\binom{K-1}{d-1}$.

If one attempted to express (12.3) through $\binom Kd$, the factor would be $k/K$, and $K$ need not be odd. Such an expression cannot be used as an odd-unit normalization.

A division-safe common choice is


$$
J_d=\binom{K-1}{d}.
$$


Relative to $J_d/k$, the different factorial patterns supply the appropriate explicit products of $K,d,k$; only the odd number $k$ is inverted. For instance,


$$
\begin{array}{c|c}
(a_0,\ell_0,c_0)&\text{high quotient}\\ \hline
(0,0,0)&KJ_d/k\\
(-1,-1,0)&dJ_d/k\\
(-1,0,-1)&J_d\\
(0,-1,-1)&KdJ_d.
\end{array}
\tag{12.4}
$$



This illustrates a genuine new overflow obligation. A correct next lift must classify it using the actual new moment range, not reuse the old $96,100$ formulas indiscriminately.

---

## 13. Endpoint retained before exclusion

The actual endpoint is


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


The $+1$ remains present.

The retained bounds


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4
$$


give


$$
X_b^2\in2^{10}\mathbb Z_2,\qquad
X_bY_b\in2^9\mathbb Z_2.
$$


Thus both endpoint contributions vanish modulo $256$. This does not delete the endpoint from the construction; it proves its contribution vanishes at the specified scalar precision.

---

# Part V. The precise outstanding lemma

## 14. Why the actual coefficient lift is still incomplete

The report now supplies:

- the contact polynomial through raw modulus $256$;
- the complete exterior force through that modulus;
- the full exterior negative-moment expansion;
- proved bounded first-forcing inputs;
- a valid new sufficient interior cutoff;
- explicit new overflow patterns.

What is still missing is the following actual finite-interface theorem.

> **Complete next-contact transport lemma.**  
> Starting from the original finite contact system on $0\le i,j<b$, transport
> 

$$
> 66U+128V,\qquad
> V\equiv x^{[2]}+x^{[5]}+x^{[7]}+x^{[8]}\pmod2,
>
$$


> through the actual contact conjugation and exterior insertion. Derive the complete first and second finite forcing polynomials, retain every induced boundary term, prove the necessary inverse truncation and coefficient-valued degree bounds, and prove weighted parameter transfer at raw precisions $128$ and $256$.

This is more specific than asking for an unspecified “next lift.” Its input is now explicit.

The displayed degree-four operator in the supplied work strongly suggests the natural linear extension to higher divided-power degrees. But a plausible extension is not a proof that it represents the **actual** finite contact construction with every boundary insertion. I do not substitute that suggestion for the missing derivation.

Only after this lemma is proved should one:

1. compute the complete new polynomial coefficient vectors;
2. reconstruct all moments, including $-10,-9$;
3. establish any sharper support reduction;
4. evaluate the joint carry $\mathcal C(X,Y)$;
5. prove transfer of the whole contracted sum, including its terminal conditions.

The turn0 unit period and original $D$-reachability remain useful inputs. Neither evaluates the missing finite contact transport or the unbounded higher-binomial contraction.

---

# Part VI. Bounded exact arithmetic appropriate at this stage

## 15. A small source-lift certificate—not a mixed–norm table

No joint carry table is justified yet. The following bounded certificate is appropriate because it audits only the newly proved local prerequisites.

### Inputs

1. The divided-power vector
   

$$
U=(-1,2,-3,3).
$$


2. Reference residues $b_0=209$, $A_0=644$.
3. The exact central formulas from turn20.
4. The eight central reference parameters
   

$$
h_0=161+256a,\qquad0\le a<8,
$$


   with $n_0=2h_0$.
5. Ranges
   

$$
0\le s\le9,\qquad0\le\ell\le10,\qquad0\le i\le17.
$$



### Required normalization and divisions

- Compute $U^2/2$ by exact integer division of its divided-power coefficients.
- For central scalar factors
  

$$
\frac{2^s(s!)^2}{(2s)!},
  \qquad
  \frac{2^s(s!)^2}{(2s+1)!},
$$


  first extract their exact powers of two and invert only the remaining odd denominator modulo $256$.
- Evaluate ordinary binomial coefficients exactly, or with a valuation/odd-unit decomposition that never inverts an even denominator.
- Do not divide any contracted norm or mixed sum: no such sum is part of this certificate.

### Expected verifiable output

**A. Contact**


$$
U^2/2=(1,-6,24,-75,180,-315,315)
$$


in degrees $2,\ldots,8$, and the coefficient identity (4.3).

**B. Exterior force**


$$
f=(1,210,22,56,152,16,112,128,128),
$$




$$
B=(197,234,54,56,248,208,112,128,128),
$$




$$
\beta=(113,202,78,200,248,80,240,128,128)
\pmod{256}.
$$


It should also output the reconstructed negative coefficient list (7.4).

**C. Bounded central and first forcing**

For each of the eight $h_0$-states:

- $B^{\rm cen}_{0:10}\bmod256$;
- $(f_i^0/R)_{i=0}^{17}\bmod256$;
- the signed Newton vector
  

$$
g_i=(-1)^i f_i^0/R;
$$


- reductions to the accepted modulus-$64$ forcing vector and its zero tail.

The new higher coefficient residues in this last item are requested outputs, not asserted results of an unexecuted computation. The proofs in §§8–10 certify the omitted infinite tails and the parameter transfer.

### Resource estimate

The central calculation uses at most


$$
8\cdot11\cdot10=880
$$


retained central summands, followed by fewer than $1600$ first-forcing summands. Binomial lower indices are at most $17$; all reference parameters are below $4096$.

This is a small exact-arithmetic calculation—well below a million elementary arithmetic operations in a straightforward implementation. A conservative implementation budget is under a minute and under $100$ MB on an ordinary workstation; these are estimates, not measured timings.

**No large original $b$, large factorial, residue-state table, or high-$t$ convolution is requested.**

---

# Part VII. Actual denominator and global proof status

## 16. No new denominator conclusion follows yet

Keep the least actual coefficient clearer $d_B$, the integer columns


$$
N_B=d_B[u,v],
$$


and


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final gcd and actual primitive pair are


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
$$


The primitive multiplier on the uncleared quadratic pair is


$$
d_B^2/g_B.
$$



With $\alpha=v_2(N)$, $\gamma=v_2(H)$, the retained exact interface is


$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
}
\tag{16.1}
$$



On $N\equiv0\pmod{64}$, the present report does not improve the accepted conclusion


$$
\alpha,\gamma\ge6.
$$


It gives no bound for $\gamma-\alpha$, and hence no new value or bound for the actual dyadic denominator contribution there.

A successful joint lemma proving


$$
N\equiv H\equiv64\pmod{128}
$$


on an infinite original subfamily would give $\alpha=\gamma=6$ on that subfamily. That remains a target, not a result.

All odd-prime contributions to the final gcd remain part of the global obligation.

## 17. Whole evaluated error

The center is unchanged:


$$
c_n=\frac{p_n}{q_n}
=\frac{2b!}{\lambda R}\frac HN.
$$


At the retained scope of the fixed-ratio whole-error theorem,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The complete primitive evaluated form is therefore


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
$$



None of the local lifts proved here shows that this complete, nonzero form tends to zero.

---

# Final ledger

### New rigorous results

- The contact lift is
  

$$
\phi^n\equiv1+66U+64U^2\pmod{256},
$$


  with the explicit degree-eight divided-power correction.
- All nine exterior forcing values and all nine exterior negative-moment coefficients modulo $256$ are evaluated.
- The reconstructed negative range extends to $-10$, with explicit nonzero new coefficients.
- Complete conservative central and first-forcing truncations, with bounded parameter transfer, are proved.
- Weight depth at least five suffices to exclude an interior coordinate from both $N$ and $H$ modulo $256$.
- New overflow patterns and the actual endpoint are retained explicitly.

### Exact remaining mathematical bottleneck

The immediate missing theorem is the **actual finite transport of the degree-eight contact correction**, including its exterior boundary insertion, inverse truncation, and weighted parameter transfer. Until that theorem yields complete lifted coefficient vectors, evaluating $\mathcal C(X,Y)$ or spending a large table on mixed–norm states would be premature.

After that local obligation, the higher-binomial carry-and-unit contraction and its terminal conditions still require proof on an infinite original subfamily.

### Proof status of the objective

**No unconditional proof of rationality or irrationality of $e+\pi$ is obtained.** The new results close explicit exterior and contact-polynomial prerequisites, but do not yet close the complete actual coefficient lift, the relative valuation problem, or the final-denominator/whole-error comparison.
