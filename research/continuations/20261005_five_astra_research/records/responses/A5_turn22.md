> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — contraction of the remaining depth-one fifth mixed terms

## Result and proof status

The remaining unit dependence can be contracted **before the higher-index sum**. The decisive step is to express all moments at a fixed residue through the **same odd unit**, rather than treating their stripped units independently.

Using the audited complete $P_{64}$, $Q_{128}$, and moment-reconstruction interfaces, I obtain


$$
\boxed{
H\equiv N\pmod{64}
\qquad
\left(b=9^{18+32u},\ n=4002b,\ u\ge0\right).
}
\tag{1}
$$



Thus the requested fifth alignment holds on the true common-zero locus, including positive even $T$. The argument actually establishes the discrepancy congruence on the whole original parent domain.

The new contraction does **not** use turn21’s paired-column identity (32). In particular, the $v_2(E_t)\ge2$ sector no longer needs to remain conditional on that identity’s audit.

This is a fifth-precision theorem, not an unrestricted relative-valuation theorem and not a proof of irrationality of $e+\pi$.

---

## 1. Verification gate and retained scope

I compared the displayed formulas, coefficient vectors, and finite certificates in the supplied packet. No external archive-search, browsing, or code-execution facility is available here, so I do not claim a fresh primary-literature search, independent hash verification, or execution of the JSON computations.

The proof below uses elementary factorial stripping, exact adjacent-binomial ratios, and prime-power binomial translation. These are classical methods; no global novelty claim is made.

The dependencies are:

* A4turn29’s audited complete $P_{64}$ and retained complete $Q_{128}$ transfers;
* the actual moment reconstruction and high-weight exclusion;
* the displayed fixed coefficient data, with their finite scope;
* the actual endpoint bound.

The coordinator’s 1023 passing inequalities are used only as fixed coefficient information. The 32 auxiliary contractions are not used to prove an infinite statement.

The paired-derangement determinant construction is a separate family. Its determinant coefficients, final content, and actual primitive denominator are not substituted for the present columns.

---

## 2. Actual domain, coordinates, and complete forces

Throughout,


$$
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,
$$




$$
D=\frac{9^{18+32u}-81}{128},\qquad
C=4002D+2532,
$$


so


$$
b=128D+81,\qquad n=128C+66,
\qquad D\ \text{odd},\quad C\equiv2\pmod4.
\tag{2}
$$



Retain the original quantities


$$
h=\frac n2,\qquad R=2^h\binom{2h}{h},
\qquad \lambda=\frac{(n!)^2}{2^n},
$$




$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad N=X^TX,\qquad H=X^TY.
$$


The metric and ranges remain


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2)_{0\le j\le b}.
$$


Every actual contact inverse has range $0\le i,j<b$.

The complete coefficient inputs are


$$
\mathbf p=(34,31,7,5,48,12,4,4,32,8,56,8)\pmod{64},
$$




$$
\mathbf d=(112,102,10,124,16,24,56,0,96,16,80,96)
\pmod{128},
$$




$$
\boldsymbol\beta=(113,74,78,72,120,80,112)\pmod{128}.
\tag{3}
$$



Here $\mathbf d=\mathbf q-2\mathbf p$. The exterior coefficients retain all seven values


$$
(B_0,\ldots,B_6)=(69,106,54,56,120,80,112)\pmod{128}.
$$


Later factorial tails vanish only after the complete-tail estimate


$$
v_2\!\left(\frac{(b+7)!}{b!}\right)=7.
$$


The logarithmic force is absent at this precision by the retained whole-force bound


$$
v_2(h_i^F/b!)
\ge2000b+2-2\lfloor\log_2(8005b-1)\rfloor>7.
\tag{4}
$$



Define, with zero extension outside the stated indices,


$$
F_s(x)=\binom{s+3}{3}\sum_{r=s}^{11}p_r\binom{x}{r-s},
$$




$$
G_s(x)=\binom{s+3}{3}\sum_{r=s}^{11}d_r\binom{x}{r-s},
$$




$$
Z_{-k}(x)=\beta_k\quad(1\le k\le7),\qquad Z_s(x)=G_s(x)\quad(s\ge0),
$$


and


$$
U_s(x)=F_s(x)+xF_s(x-1)+xF_{s+1}(x-1),
$$




$$
V_s(x)=Z_s(x)+xZ_s(x-1)+xZ_{s+1}(x-1).
\tag{5}
$$



The audited reconstruction gives, for $0\le j<b$,


$$
2X_j\equiv(-1)^{j+1}W_j\mathcal F_j\pmod{64},
$$




$$
4(Y_j-X_j)\equiv(-1)^{j+1}W_j\mathcal G_j\pmod{128},
$$


and hence


$$
\boxed{
8X_j(Y_j-X_j)\equiv W_j^2\mathcal F_j\mathcal G_j
\pmod{512}.
}
\tag{6}
$$



All negative moments in $\mathcal G_j$, including the complete exterior forcing, remain present at this stage.

---

# Part I. Synchronizing the odd units

## 3. One common moment unit at each non-overflow residue

Write


$$
j=128t+\rho,\qquad d=D-t,\qquad k=2C+1,\qquad K=k+d.
$$


For the 29 retained residues $\rho\le68$, put


$$
a_\rho=84-\rho.
$$


Their actual range is


$$
0\le t\le D.
\tag{7}
$$



The actual moment is


$$
M_s(\rho,t)
=\binom{128K+a_\rho}{128d+a_\rho-(s+4)}.
\tag{8}
$$


In particular,


$$
M_{-4}(\rho,t)=\binom{128K+a_\rho}{128d+a_\rho}.
$$



Let


$$
B_d=\binom{k+d}{d},
\qquad
\tau_{\rho,t}=\frac{M_{-4}(\rho,t)}{B_d}.
\tag{9}
$$


Then


$$
\boxed{\tau_{\rho,t}\in\mathbb Z_2^\times.}
\tag{10}
$$



Indeed, seven-level factorial stripping leaves the same low remainder $a_\rho$ in the upper factorial and the first lower factorial, and remainder $0$ in the other lower factorial. The low power of two therefore cancels, while the remaining high factorial quotient is exactly $B_d$. The quotient in (9) is consequently an odd rational unit.

This common unit is the essential replacement for independent $u_{\rho s}$.

### Exact ratios

For $c=s+4\ge0$,


$$
\boxed{
\frac{M_s(\rho,t)}{M_{-4}(\rho,t)}
=
R_c(d,k;a_\rho)
:=
\frac{\binom{128d+a_\rho}{c}}
     {\binom{128k+c}{c}}.
}
\tag{11}
$$


Only $0\le c\le15$ occurs.

For the four negative-complement terms, write $c=-q$, $1\le q\le4$. Their exact ratios are


$$
\boxed{
R_{-q}(d,k;a_\rho)
=
\frac{(128k)_{\underline q}}
     {(128d+a_\rho+1)^{\overline q}}.
}
\tag{12}
$$


Thus the factors involving $k$ and the negative-complement borrow have not been deleted.

Define the complete normalized factors


$$
\widehat F_{\rho,t}
=\sum_{s=-1}^{11}U_s(\rho)R_{s+4}(d,k;a_\rho),
$$




$$
\widehat G_{\rho,t}
=\sum_{s=-8}^{11}V_s(\rho)R_{s+4}(d,k;a_\rho).
\tag{13}
$$


Then, exactly for the selected coefficient representatives,


$$
\mathcal F_{\rho,t}=B_d\tau_{\rho,t}\widehat F_{\rho,t},
\qquad
\mathcal G_{\rho,t}=B_d\tau_{\rho,t}\widehat G_{\rho,t}.
\tag{14}
$$



All moments at a given residue therefore carry the same external odd unit.

---

## 4. The bounded ratios transfer uniformly

For $1\le c\le15$, set


$$
q_c=7-\lfloor\log_2c\rfloor.
$$


The binomial translation inequality gives


$$
\binom{128d+a}{c}\equiv\binom ac\pmod{2^{q_c}},
$$


and


$$
\binom{128k+c}{c}\equiv\binom cc=1\pmod{2^{q_c}}.
$$


The denominator is odd, so inversion is legitimate. Therefore


$$
\boxed{
R_c(d,k;a)\equiv\binom ac
\pmod{2^{q_c}}.
}
\tag{15}
$$



This statement is uniform in the actual, unbounded $d,k$. It does not replace the higher binomial $B_d$ by a reference value.

Define the fixed integer contractions


$$
F_\rho^\circ
=\sum_{s=-1}^{11}U_s(\rho)\binom{a_\rho}{s+4},
$$




$$
G_\rho^\circ
=\sum_{s=-4}^{11}V_s(\rho)\binom{a_\rho}{s+4}.
\tag{16}
$$



The coefficient precisions imply


$$
\boxed{
\widehat F_{\rho,t}\equiv F_\rho^\circ\pmod{32},
\qquad
\widehat G_{\rho,t}\equiv G_\rho^\circ\pmod{64}.
}
\tag{17}
$$



Here are the necessary checks.

* For $c\le7$, (15) supplies at least five bits. For $c\ge8$, the relevant $U_s$, $s\ge4$, are divisible by $4$, supplying more than the one additional bit needed for $F$.
* For $G$, $c\le3$ supplies at least six bits. For $4\le c\le7$, the relevant $V_s$ are even. For $c\ge8$, $V_s$, $s\ge4$, are divisible by $8$.
* The four terms in (12) are checked before omission. The displayed fixed coefficient rows give
  

$$
v_2\!\left(V_s(\rho)R_{s+4}(d,k;a_\rho)\right)\ge8
  \quad(-8\le s\le-5)
  \tag{18}
$$


  for the 29 retained non-overflow residues. These are precisely the negative-complement coefficient-depth checks already contained in the supplied certificate. Since $k$ is odd, their low valuations are independent of the higher digits.

Thus the complete negative-complement force vanishes at the modulus in (17), rather than being removed by a parity assumption.

---

## 5. The weight unit also enters as a square

For $\rho\le68$, let


$$
b_\rho=v_2\binom{68}{\rho}.
$$


Exact stripping of the actual weight gives


$$
W_{\rho,t}
=2^{b_\rho}w_{\rho,t}\binom Ct,
\qquad w_{\rho,t}\in\mathbb Z_2^\times.
\tag{19}
$$



Put


$$
E_t=\binom Ct\binom{k+D-t}{D-t},
\qquad
\xi_{\rho,t}=w_{\rho,t}\tau_{\rho,t}.
$$


Then


$$
\boxed{
W_{\rho,t}^2\mathcal F_{\rho,t}\mathcal G_{\rho,t}
=
2^{2b_\rho}E_t^2\xi_{\rho,t}^{\,2}
\widehat F_{\rho,t}\widehat G_{\rho,t}.
}
\tag{20}
$$



The formerly troublesome low units now occur through the **single odd square**
$\xi_{\rho,t}^{\,2}$.

Also,


$$
\boxed{E_t\in2\mathbb Z\qquad(0\le t\le D).}
\tag{21}
$$


If $t$ is odd, $\binom Ct$ is even because $C$ is even. If $t$ is even, $D-t$ is odd; since $k$ is odd, adding $D-t$ to $k$ causes a binary carry, so the second binomial is even.

Consequently, a coefficient congruence modulo $128$ in (20) determines the complete raw contribution modulo $512$.

---

# Part II. Evaluating the requested normalized products

## 6. The critical fixed contractions

The following small congruences are the only cancellations beyond coefficientwise depth bounds:


$$
\begin{array}{c|c|c}
\rho&F_\rho^\circ&G_\rho^\circ\\ \hline
0,64&2\pmod8&48\pmod{64}\\
2,66&\text{divisible by }4&0\pmod8\\
32&\text{divisible by }2&0\pmod{16}\\
1,65&6\pmod8&1\pmod4
\end{array}
\tag{22}
$$



I give the arithmetic explicitly.

### 6.1 Residues $0,64$

Their low upper arguments are $84,20$. In $F_\rho^\circ\bmod8$, only the $s=0$ term survives:


$$
U_0(0)=34,\qquad U_0(64)=2,
$$


and


$$
\binom{84}{4}\equiv\binom{20}{4}\equiv1\pmod4.
$$


Hence $F_\rho^\circ\equiv2\pmod8$.

In $G_\rho^\circ\bmod64$, the surviving terms are $s=-4,-3,-2,-1,0,2,4$. For either residue their respective contributions are


$$
8,\quad24,\quad44,\quad52,\quad48,\quad32,\quad32.
$$


Their sum is $240\equiv48\pmod{64}$.

For example, the required binomial residues are


$$
\begin{array}{c|cc}
& a=84&a=20\\ \hline
\binom a1\bmod64&20&20\\
\binom a2\bmod64&30&62\\
\binom a3\bmod64&52&52\\
\binom a4\bmod4&1&1\\
\binom a6\bmod16&8&8\\
\binom a8\bmod4&2&2.
\end{array}
$$


The differing $\binom a2$ residues give the same product modulo $64$, because the relevant coefficient is $10\bmod64$.

In particular, the complete normalized mixed factor at both residues has the stronger depth


$$
\boxed{\widehat G_{\rho,t}\in16\mathbb Z_2\qquad(\rho=0,64).}
\tag{23}
$$



### 6.2 Residues $2,66$

Here $a=82,18$. Modulo $8$, only $s=-4,-3$ can remain in $G_\rho^\circ$:


$$
116+126a\equiv4+4\equiv0\pmod8.
\tag{24}
$$


All other terms have depth at least three.

### 6.3 Residue $32$

Here $a=52$. Modulo $16$, the only surviving contributions are


$$
8,\qquad78\cdot52,\qquad42\binom{52}{2},
\qquad17\binom{52}{3}.
$$


Since


$$
\binom{52}{2}\equiv14,\qquad
\binom{52}{3}\equiv4\pmod{16},
$$


their residues are


$$
8+8+12+4\equiv0\pmod{16}.
\tag{25}
$$



### 6.4 Residues $1,65$

Here $a=83,19$. Modulo $8$, the $s=-1,0$ contributions to $F_\rho^\circ$ are $2,4$, while all remaining contributions vanish. Thus


$$
F_\rho^\circ\equiv6\pmod8.
$$



Modulo $4$, the $s=-4,-3,-2,-1$ contributions to $G_\rho^\circ$ are


$$
2,\quad2,\quad3,\quad2,
$$


and all others vanish. Hence


$$
G_\rho^\circ\equiv1\pmod4.
\tag{26}
$$



---

## 7. The other nine-class and twelve-class terms

The displayed fixed coefficient rows give the following stronger coefficientwise bounds. These hold before cancellation and therefore retain all odd units:


$$
\begin{array}{c|c|c}
\rho&v_2(\widehat F_{\rho,t})\text{ at least}
&v_2(\widehat G_{\rho,t})\text{ at least}\\ \hline
3,67&3&1\\
16,48&1&2\\
20,52&5&5\\
34&2&2
\end{array}
\tag{27}
$$



For example, the minima for $\rho=16,48$ in the mixed column occur at $s=-2,-1$, both with combined depth two. For $\rho=34$, the first-column minimum is two and the mixed-column minimum is two.

For all twelve $b_\rho=3$ residues,


$$
\rho\in\{8,12,18,24,28,33,35,40,44,50,56,60\},
$$


the first-column coefficient rows give the improved bound


$$
\boxed{\widehat F_{\rho,t}\in2\mathbb Z_2.}
\tag{28}
$$


The earlier bound $f_\rho\ge0$ was sufficient for turn21, but not sharp.

Finally, the already retained bounds $f_\rho,g_\rho\ge4$ eliminate


$$
\rho=4,36,68.
\tag{29}
$$



---

## 8. Actual required unit-sensitive products

To compare directly with turn21’s last precision table, write its stripped factors as


$$
\mathfrak f_\rho=\tau_{\rho,t}\widehat F_{\rho,t},
\qquad
\mathfrak g_\rho=\tau_{\rho,t}\widehat G_{\rho,t}.
$$


At $v_2(E_t)=1$, the required normalized products are therefore:



$$
\boxed{
\begin{array}{c|c|c}
\rho&
\text{actual normalized product}&\text{evaluated residue}\\ \hline
0,64&
w_\rho^2(\mathfrak f_\rho/2)(\mathfrak g_\rho/4)
&12\pmod{16}\\
2,66&
w_\rho^2(\mathfrak f_\rho/4)(\mathfrak g_\rho/4)
&0\pmod2\\
32&
w_\rho^2(\mathfrak f_\rho/2)(\mathfrak g_\rho/4)
&0\pmod4\\
1,65&
w_\rho^2(\mathfrak f_\rho/2)\mathfrak g_\rho
&3\pmod4\\
3,16,20,34,48,52,67&
w_\rho^2(\mathfrak f_\rho/2)\mathfrak g_\rho
&0\pmod4\\
8,12,18,24,28,33,35,40,44,50,56,60&
w_\rho^2\mathfrak f_\rho\mathfrak g_\rho
&0\pmod2
\end{array}}
\tag{30}
$$



These are unit-sensitive evaluations, not parity counts.

For the first row, (22) gives


$$
(\widehat F/2)(\widehat G/4)\equiv12\pmod{16}.
$$


The external factor is $(w_\rho\tau_{\rho,t})^2$. Every odd square is $1\bmod8$, and


$$
12(z^2-1)\equiv0\pmod{16}
\qquad(z\text{ odd}).
$$


Thus its unknown higher unit bits genuinely disappear.

For $\rho=1,65$,


$$
(\widehat F/2)\widehat G\equiv3\pmod4,
$$


and the external odd square is $1\bmod4$.

The zero rows follow from (24), (25), (27), and (28). No independent choice or suppression of the individual moment units is involved.

---

# Part III. Contraction before the higher sum

## 9. A fixed low-polynomial identity

An equivalent compact form of the calculation is


$$
\boxed{
2^{2b_\rho}F_\rho^\circ G_\rho^\circ
\equiv
\begin{cases}
96\pmod{128},&\rho\in\{0,1,64,65\},\\
0\pmod{128},&\text{the other 25 non-overflow residues}.
\end{cases}}
\tag{31}
$$



The passage from (17) to the product modulo $128$ is justified:

* when $b_\rho=0$, the retained bounds give $v_2(\widehat F)\ge1$ and $v_2(\widehat G)\ge2$, so errors of depths five and six contribute product errors of depth at least seven;
* when $b_\rho\ge1$, the weight factor $2^{2b_\rho}$ itself supplies the remaining precision.

Multiplication by the actual odd square $\xi_{\rho,t}^2$ does not alter (31), since


$$
96(\xi_{\rho,t}^2-1)\equiv0\pmod{128}.
$$



Combining (20), (21), and (31),


$$
\boxed{
W_{\rho,t}^2\mathcal F_{\rho,t}\mathcal G_{\rho,t}
\equiv
\begin{cases}
96E_t^2\pmod{512},&\rho\in\{0,1,64,65\},\\
0\pmod{512},&\text{the other 25 non-overflow residues}.
\end{cases}}
\tag{32}
$$



This formula is valid for every actual $0\le t\le D$, not only for depth-one $E_t$.

### The depth-one contraction

If $E_t=2e_t^\ast$, with $e_t^\ast$ odd, each of the four potentially nonzero coordinates contributes


$$
96E_t^2\equiv384\pmod{512}.
$$


Consequently, at this same $t$,


$$
384+384+384+384=1536\equiv0\pmod{512}.
\tag{33}
$$



Equivalently,


$$
\sum_{\rho\ {\rm nonoverflow}}
W_{\rho,t}^2\mathcal F_{\rho,t}\mathcal G_{\rho,t}
\equiv384E_t^2\equiv0\pmod{512},
\tag{34}
$$


because $E_t$ is even.

No complementary $t$-pairing is used. The cancellation takes place among the original coordinates


$$
128t,\quad128t+1,\quad128t+64,\quad128t+65,
$$


all of which remain strictly below $b$, including at $t=D$.

### The sector $v_2(E_t)\ge2$

Equation (32) also proves that each of these four coordinates vanishes individually when $4\mid E_t$. The other 25 classes already vanish.

Thus the required all-$E$-depth-$\ge2$ conclusion is now obtained directly, without turn21’s identity (32).

---

## 10. Overflow, excluded coordinates, and the actual endpoint

The overflow residues remain


$$
\rho=96,100,\qquad 0\le t\le D-1.
$$


Their shared higher factor is


$$
(C-t)\binom Ct B_d^-,
\qquad
B_d^-=\binom{k+d-1}{d-1},
$$


and $d\ge1$ on this exact range.

Because


$$
(C-t)\binom Ct=C\binom{C-1}{t},
$$


this higher factor is even. With $b_\rho=2$, the retained low bounds give


$$
\rho=96:\quad 2b_\rho+2+f_\rho+g_\rho
=4+2+1+2=9,
$$


and a stronger bound for $\rho=100$. Both overflow contributions vanish modulo $512$, with their borrow factors retained.

Every interior coordinate outside the 31 retained classes is covered by the audited high-weight mixed exclusion. This is the mixed-product exclusion, not a norm-support substitution.

At the actual endpoint,


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


The $+1$ is retained. The established bounds


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4
$$


give


$$
X_b(Y_b-X_b)\in2^9\mathbb Z_2.
\tag{35}
$$



Combining the non-overflow contraction, overflow terms, excluded coordinates, and endpoint proves


$$
\boxed{\mathscr S_{\rm raw}\equiv0\pmod{512}.}
\tag{36}
$$


Since the audited complete reconstruction gives


$$
\mathscr S_{\rm raw}\equiv8(H-N)\pmod{512},
$$


we conclude


$$
\boxed{H-N\equiv0\pmod{64}}
\tag{37}
$$


on every original exponent $r=18+32u$.

---

## 11. Consequences on the true common-zero locus

The proof does not require evaluating $T$ or pairing its admissible indices. It therefore covers positive even $T$ directly.

If the retained norm formula


$$
N\equiv48T+32\chi\pmod{64}
$$


is used, then for even $T$,


$$
N\equiv32\left(\frac T2+\chi\right)\pmod{64}.
$$



The exact valuation implications are:

* If
  

$$
N\equiv32\pmod{64},
$$


  then (37) gives $H\equiv32\pmod{64}$, so
  

$$
\boxed{\alpha=\gamma=5,\qquad\gamma-\alpha=0.}
  \tag{38}
$$



* If
  

$$
N\equiv0\pmod{64},
$$


  then
  

$$
\boxed{\alpha,\gamma\ge6.}
  \tag{39}
$$


  This gives no upper bound, lower bound, or equality assertion for
  $\gamma-\alpha$.

In particular, fifth whole alignment does not establish unrestricted relative alignment.

---

## 12. Final gcd, actual primitive denominator, and whole error

The center and normalization remain unchanged:


$$
c_n=\frac{2b!}{\lambda R}\frac HN.
$$



Let $d_B$ be the least common denominator of the actual two-column lift and set


$$
N_B=d_B[u,v].
$$


Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
\tag{40}
$$


The primitive multiplier on the uncleared quadratic pair is


$$
\boxed{\frac{d_B^2}{g_B},}
$$


and $q_n$, not a row-clearer or an unreduced quadratic coefficient, is the actual denominator.

With $s=s_2(n)$, retain the exact dyadic interface


$$
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\,
\frac{3n}{2}-s+v_2(b!)+3+\gamma
\right\},
$$




$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s-1-(\gamma-\alpha)
\right\}.
}
\tag{41}
$$



At indices satisfying $N\equiv32\pmod{64}$, equation (38) permits setting
$\gamma-\alpha=0$ in (41). At indices satisfying $N\equiv0\pmod{64}$, it does not.

At the retained scope of the complete signed-error theorem,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The whole primitive evaluated error remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
\tag{42}
$$



The fifth congruence supplies no estimate proving that this complete nonzero integer linear form tends to zero.

---

# Concluding ledger

## 1. New result and proof status

**Proved from the audited complete fifth-precision interfaces:**


$$
\boxed{
H\equiv N\pmod{64}
\quad\text{for every }b=9^{18+32u},\ n=4002b,\ u\ge0.
}
$$



The new proof supplies:

* a common-unit representation for all retained moments at each residue;
* a uniform, proved transfer of the normalized ratios to bounded binomial polynomials;
* the actual normalized products at every precision requested in turn21’s table;
* contraction of the four surviving depth-one coordinate terms before the high $t$-sum;
* an independent elimination of the $v_2(E_t)\ge2$ sector;
* the original overflow ranges and full endpoint.

Turn21’s disputed paired-column identity is not needed for this proof.

## 2. Exact remaining mathematical bottleneck

The fifth mixed convolution is closed.

The remaining arithmetic problem is now genuinely beyond fifth precision: obtain an unrestricted relative-valuation estimate, or another sufficient same-index control of the actual denominator after the final gcd.

A concrete next lemma is


$$
\boxed{v_2(H-N)>v_2(N)}
$$


on an explicitly specified infinite original-domain family. Such a lemma would imply $\gamma=\alpha$ there. The present result proves this comparison only where $v_2(N)=5$, not where $v_2(N)\ge6$.

For irrationality, the decisive requirement remains a same-index estimate for the **whole nonzero primitive form**


$$
q_n(e+\pi)-p_n.
$$


No such estimate follows here. Irrationality of $e+\pi$ remains unresolved.

## 3. Bounded exact-arithmetic certificate

No growing-index calculation is required for the new contraction.

A compact independent certificate has inputs:

* the vectors $\mathbf p,\mathbf d,\boldsymbol\beta$ in (3);
* the exact definitions of $U_s,V_s$ in (5);
* the 29 non-overflow residues;
* $a_\rho=84-\rho$ and $b_\rho=v_2\binom{68}{\rho}$.

Compute


$$
F_\rho^\circ=\sum_{s=-1}^{11}U_s(\rho)\binom{84-\rho}{s+4},
\qquad
G_\rho^\circ=\sum_{s=-4}^{11}V_s(\rho)\binom{84-\rho}{s+4}.
$$



The expected verifiable output is


$$
2^{2b_\rho}F_\rho^\circ G_\rho^\circ\bmod128
=
\begin{cases}
96,&\rho=0,1,64,65,\\
0,&\text{the other 25 residues}.
\end{cases}
$$



In pseudocode:
```text
for rho in the 29 non-overflow residues:
    a = 84 - rho
    F = sum(U_s(rho) * binom(a, s+4), s=-1,...,11)
    G = sum(V_s(rho) * binom(a, s+4), s=-4,...,11)
    expected = 96 if rho in {0,1,64,65} else 0
    assert (2^(2*b_rho) * F * G) mod 128 == expected
```

The four nonzero outputs sum to $384\equiv0\pmod{128}$. The proved common-unit transfer and the actual factor $E_t^2\in4\mathbb Z$ are what convert this bounded identity into the original-domain raw congruence modulo $512$; the finite calculation alone would not do so.
