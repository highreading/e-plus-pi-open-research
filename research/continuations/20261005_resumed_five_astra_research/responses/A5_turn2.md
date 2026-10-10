> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — finite transport of the degree-eight contact correction and a bounded coefficient certificate

## Executive result

The finite Pascal contact algebra admits an exact operator for every divided-power monomial. With the row and column conventions of the supplied degree-four contact theorem, that operator is


$$
\boxed{
\mathscr C_{s;n,b}f(x)
=
\sum_{v=0}^{s}
(-1)^{s-v}\binom{x}{s-v}\binom nv\,
\mathscr T_{v,b}f(x-s+v),
}
\tag{1}
$$


where


$$
\mathscr T_{0,b}f=f,\qquad
\mathscr T_{v,b}f(y)
=
\sum_{k=y}^{b-1}\binom{v+k-y-1}{v-1}f(k)
\quad(v\ge1)
\tag{2}
$$


is interpreted by its integer-valued polynomial continuation.

The upper limit in (2) is the **actual finite endpoint $b-1$**. The formula is not an infinite-suffix approximation.

Consequently, put


$$
\mathscr E=\sum_{s=1}^{4}u_s\mathscr C_s,
\qquad (u_1,u_2,u_3,u_4)=(-1,2,-3,3),
$$


and


$$
\mathscr F=\mathscr C_2+\mathscr C_5+\mathscr C_7+\mathscr C_8.
$$


Then the transported contact correction at modulus $256$ is


$$
\boxed{\mathscr K=66\mathscr E+128\mathscr F\pmod{256}.}
\tag{3}
$$



Below I derive the exact finite identity, including the lower boundary and exterior columns, and obtain complete, bounded formulas for $P_{128}$ and $Q_{256}$. In particular, the single degree-eight exterior insertion survives and is explicitly


$$
\boxed{128\left(x+\binom{x}{7}\right)\pmod{256}.}
\tag{4}
$$



The resulting coefficient calculation needs only the reference parameters


$$
\boxed{n_0=322,\qquad b_0=209,}
\tag{5}
$$


but this reduction requires—and below receives—a coefficient-depth-sensitive proof. A naive unweighted estimate would not justify it.

**No computation is executed here.** The completed eight-state source calculation is reused, not requested again. The new requested output is the complete Newton coefficient pair through degree $27$, with explicit residual certificates.

This closes the finite Pascal transport and gives a fully specified bounded coefficient calculation, at the scope of the retained original contact-conjugation and reconstruction interfaces. It does not evaluate the subsequent joint norm–mixed carry, prove a new alignment beyond modulus $64$, or settle irrationality of $e+\pi$.

---

## 1. Scope, overlap gate, and unchanged objects

The original domain remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


In particular,


$$
b\equiv209\pmod{256},\qquad n\equiv322\pmod{512}.
\tag{6}
$$



Keep


$$
h=n/2,\qquad R=2^h\binom{2h}{h},\qquad
\lambda=\frac{(n!)^2}{2^n},
$$




$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad N=X^TX,\qquad H=X^TY,
$$


and the original metric


$$
W_j=\binom{n+2}{j},\qquad
\Omega=\operatorname{diag}\bigl((n+2)_{\underline j}^{\,2}\bigr)_{0\le j\le b}.
$$



Every actual inverse below has indices


$$
0\le i,j<b.
$$



### Verification and dependency gate

I compared the displayed old contact operator, the row-kernel identity in the assignment, the completed local-force receipt, and the retained reconstruction formulas. No external browsing, archive search, hash verification, or arithmetic execution is available in this response. Thus:

* the overlap check is bounded to the supplied material;
* no fresh primary-literature search is claimed;
* no exhaustive novelty claim is made;
* finite Pascal differentiation, Newton summation, and binomial translation are reused classical algebra.

The original contact-conjugation theorem and the actual column reconstruction are retained at their established scope. The derivation below identifies the arbitrary monomial in that same row algebra; it does not reconstruct unrelated original matrices absent from the packet.

The paired-derangement determinant family remains separate.

---

# Part I. Exact arbitrary-monomial transport

## 2. Matching the generating-function convention

Let


$$
\partial^{[s]}=\frac1{s!}\frac{d^s}{dz^s}.
$$


In the contact row convention fixed by the supplied degree-four formula, a divided-power symbol $x^{[s]}$ acts on the Pascal row $z^k(1+z)^n$ by $\partial^{[s]}$, followed by multiplication by $(1+z)^{-n}$.

This convention matters: the row operator is the **divided derivative**, not the unnormalized derivative.

Leibniz’s rule gives


$$
\begin{aligned}
\partial^{[s]}\!\left[z^k(1+z)^n\right](1+z)^{-n}
&=
\sum_{v=0}^{s}
\binom{k}{s-v}\binom nv
z^{k-s+v}(1+z)^{-v}.
\end{aligned}
\tag{7}
$$


Taking the coefficient of $z^\ell$,


$$
\boxed{
C_s(k,\ell)=
\sum_{v=0}^{s}
\binom{k}{s-v}\binom nv
\binom{-v}{\ell-k+s-v}.
}
\tag{8}
$$



Here a binomial with negative lower index is zero. For $v=0$,


$$
\binom0m=\mathbf1_{m=0}.
$$



### Agreement with the old contact matrix

The supplied old matrix is


$$
E_{ij}=
\sum_{s=1}^{4}u_s
\sum_{v=0}^{s}
\binom i{s-v}\binom nv
\binom{-v}{j+s-i-v}.
$$


This is exactly


$$
E=\sum_{s=1}^{4}u_sC_s.
\tag{9}
$$



Thus all three conventions match:

1. row index $k=i$;
2. column index $\ell=j$;
3. divided-power coefficient $u_s$ multiplying the divided-derivative kernel $C_s$.

There is no transpose, missing $s!$, or extra sign in reusing the graded-kernel identity.

---

## 3. Exact signed finite suffix identity

Define


$$
(\mathcal S_bf)_j=(-1)^jf(j),\qquad 0\le j<b.
$$



For $v\ge1$ and $m\ge0$,


$$
\binom{-v}{m}=(-1)^m\binom{v+m-1}{v-1}.
$$


Set


$$
y=i-s+v.
$$


Then, in a nonzero summand,


$$
m=j-y,
$$


and


$$
(-1)^i(-1)^j(-1)^{j-y}=(-1)^{s-v}.
$$



Therefore


$$
\boxed{
C_s^{\,II}\mathcal S_bf
=
\mathcal S_b(\mathscr C_{s;n,b}f),
}
\tag{10}
$$


with $\mathscr C_s$ given by (1). The superscript $II$ means restriction to the actual interior block $0\le i,j<b$.

### Lower boundary

If $i<s-v$, then


$$
\binom{i}{s-v}=0.
$$


Thus any polynomial continuation in (1) evaluated at a negative shifted argument is multiplied by zero.

If $i\ge s-v$, then $y=i-s+v\ge0$, and the original row sum really begins at $j=y$. Consequently the suffix is exactly


$$
\sum_{j=y}^{b-1},
$$


not a sum requiring an unaccounted lower-boundary correction.

For $v=0$, the kernel is a single shifted entry:


$$
(-1)^s\binom{i}{s}f(i-s).
$$


Again, when $i<s$, the binomial factor kills it.

This proves the lower-boundary statement for every $s$, not only $s\le4$.

### Upper boundary

For $0\le i<b$,


$$
i-s+v\le i<b.
$$


Hence the true suffix always ends at $b-1$. No value $f(b)$ or fictitious continuation beyond $b-1$ is inserted in (10).

The polynomial continuation is a representation of this finite sum, not a change of matrix range.

---

## 4. Integrality and degree

Write $\operatorname{Int}(\mathbb Z)$ for the ring of integer-valued rational polynomials, equivalently the integral Newton span


$$
\bigoplus_{r\ge0}\mathbb Z\binom xr.
$$



For $v\ge1$, the summand in (2), viewed as a polynomial in $k$, has degree at most


$$
\deg f+v-1.
$$


Expanding it in Newton polynomials in $k$ and using


$$
\sum_{k=y}^{b-1}\binom kr=\binom b{r+1}-\binom y{r+1}
\tag{11}
$$


proves:

* $\mathscr T_{v,b}f$ is an integer-valued polynomial;
* its degree in the evaluation variable is at most $\deg f+v$;
* its upper-endpoint dependence uses only $\binom br$ with
  

$$
r\le \deg f+v.
$$



Multiplication by $\binom{x}{s-v}$ now gives


$$
\boxed{
\mathscr C_s\operatorname{Int}(\mathbb Z)
\subseteq\operatorname{Int}(\mathbb Z),\qquad
\deg(\mathscr C_sf)\le\deg f+s.
}
\tag{12}
$$



All reductions in this report are **Newton-coefficient reductions**, not ordinary-monomial reductions.

---

## 5. Specialization to degrees $1,\ldots,8$

For a compact explicit implementation, put


$$
L_a f(x)=(-1)^a\binom xa f(x-a).
$$


Then


$$
\boxed{
\mathscr C_s=\sum_{v=0}^{s}\binom nv\,L_{s-v}\mathscr T_{v,b}.
}
\tag{13}
$$



Thus the eight required operators are obtained by taking $s=1,\ldots,8$ in the following finite rule:


$$
\begin{aligned}
\mathscr C_1&=L_1+\binom n1\mathscr T_1,\\
\mathscr C_2&=L_2+\binom n1L_1\mathscr T_1+\binom n2\mathscr T_2,\\
\mathscr C_3&=L_3+\binom n1L_2\mathscr T_1
+\binom n2L_1\mathscr T_2+\binom n3\mathscr T_3,\\
\mathscr C_4&=L_4+\binom n1L_3\mathscr T_1
+\binom n2L_2\mathscr T_2+\binom n3L_1\mathscr T_3
+\binom n4\mathscr T_4,
\end{aligned}
\tag{14}
$$


and, for $5\le s\le8$,


$$
\mathscr C_s
=
L_s+\binom n1L_{s-1}\mathscr T_1+\cdots+
\binom n{s-1}L_1\mathscr T_{s-1}
+\binom ns\mathscr T_s.
\tag{15}
$$



This is an explicit finite operator prescription involving at most nine summands per monomial.

At $n=2$, combining (14) with $u=(-1,2,-3,3)$ gives exactly the supplied operator (15) of prior turn17. This supplies an additional convention check.

---

# Part II. Exterior transport and the complete correction

## 6. Exact exterior insertion

Let an exterior vector have entries $B_a$ at columns $b+a$, $0\le a\le8$. Define


$$
\mathscr A_s(x)=(-1)^x\sum_{a=0}^{8}C_s(x,b+a)B_a
$$


on interior integer rows; its polynomial formula is


$$
\boxed{
\mathscr A_s(x)=
\sum_{a=0}^{8}\sum_{v=1}^{s}
(-1)^{b+a+s-v}B_a
\binom{x}{s-v}\binom nv
\binom{b+a-x+s-1}{v-1}.
}
\tag{16}
$$



There is no $v=0$ exterior term: its kernel would require


$$
b+a=x-s,
$$


impossible for $x<b$ and $s\ge0$.

Each term of (16) has degree at most


$$
(s-v)+(v-1)=s-1.
$$


Consequently,


$$
\boxed{\deg\mathscr A_s\le s-1.}
\tag{17}
$$



This proves the complete exterior-boundary formula. In particular, the exterior insertion has degree one less than the corresponding interior operator.

Put


$$
\mathscr A=\sum_{s=1}^{4}u_s\mathscr A_s,\qquad
\mathscr J=\mathscr A_2+\mathscr A_5+\mathscr A_7+\mathscr A_8.
\tag{18}
$$


Then


$$
\deg\mathscr A\le3,\qquad \deg\mathscr J\le7.
\tag{19}
$$



The sign in (16) agrees with the old $a_{32}$ convention. For example, at $n=2,x=0$, the old exterior kernel gives


$$
\mathscr A(0)=-2\sum_a(b+a)(-1)^aB_a,
$$


which reproduces the prior boundary constant $10\bmod32$ from the old seven-entry data.

---

## 7. Transport of $66U+128V$

The accepted contact-polynomial lift is


$$
\phi^n\equiv1+66U+128V\pmod{256},
$$


where


$$
V\equiv x^{[2]}+x^{[5]}+x^{[7]}+x^{[8]}\pmod2.
$$



Linearity of (7)–(8) and integrality of every $C_s$ prove the actual interior and exterior reductions


$$
K^{II}=66E^{II}+128F^{II}\pmod{256},
\tag{20}
$$




$$
\mathcal S_b^{-1}K^{IE}B
=
66\mathscr A+128\mathscr J\pmod{256}.
\tag{21}
$$



The degree-eight term is therefore transported through both blocks, not just through an interior polynomial ansatz.

### Mixed insertions really vanish

Because all matrix entries are integral,


$$
(66E^{II})(128F^{II}),\quad
(128F^{II})(66E^{II})
$$


are divisible by


$$
66\cdot128=8448\in256\mathbb Z.
$$


The same holds for compositions involving an exterior insertion and an additional interior insertion.

Thus the statement “one $128V$ insertion survives, but any additional $66U$ insertion kills it modulo $256$” follows from the **actual finite block matrices**.

No multiplicativity of the map $U\mapsto E$ is needed or asserted. In particular, $\mathscr F$ is not replaced by $\mathscr E^2/2$.

---

## 8. The surviving degree-eight exterior insertion

At modulus $2$, the supplied exterior vector has only one odd entry:


$$
B_0\equiv1,\qquad B_a\equiv0\quad(a\ge1).
$$


Moreover


$$
n\equiv322\equiv2\pmod{16},
$$


so among $1\le v\le8$, the only odd $\binom nv$ is $v=2$.

Equation (16), modulo $2$, therefore gives


$$
\mathscr A_s(x)\equiv
\binom{x}{s-2}(b-x+s-1)
\qquad(s=2,5,7,8).
$$


Since $b$ is odd,


$$
\begin{aligned}
\mathscr J(x)
&\equiv
x+(1+x)\binom x3+(1+x)\binom x5+x\binom x6\\
&\equiv x+\binom x7\pmod2.
\end{aligned}
\tag{22}
$$


For the last step, use


$$
x\binom xr=r\binom xr+(r+1)\binom x{r+1}.
$$



Hence


$$
\boxed{128\mathscr J=128\left(x+\binom x7\right)\pmod{256}.}
\tag{23}
$$



This is the new exterior contact insertion. It is distinct from merely appending the new factorial entries $f_7,f_8$.

---

# Part III. Complete forces and finite inverses

## 9. Reuse of the completed local source lift

The completed receipt, together with the prior all-index truncation and parameter-transfer proofs, supplies the complete first forcing


$$
\boxed{
g=
66+247\binom x1+115\binom x2+135\binom x3
+76\binom x4+92\binom x5
+176\binom x6+112\binom x7
+192\binom x9+64\binom x{10}+64\binom x{11}
\pmod{256}.
}
\tag{24}
$$



The coefficient of $\binom x8$ is zero. All coefficients from degree $12$ onward vanish at this precision.

Its coefficient-depth decomposition is


$$
\boxed{
g=g^{(0)}+4g^{(2)}+16g^{(4)}+64g^{(6)},
}
\tag{25}
$$


with respective degree bounds


$$
3,\quad5,\quad7,\quad11.
$$


For example, one exact representative decomposition uses


$$
\begin{aligned}
g^{(0)}&=66+247\binom x1+115\binom x2+135\binom x3,\\
g^{(2)}&=19\binom x4+23\binom x5,\\
g^{(4)}&=11\binom x6+7\binom x7,\\
g^{(6)}&=3\binom x9+\binom x{10}+\binom x{11}.
\end{aligned}
$$



No repeat of the eight-state central calculation is needed.

---

## 10. Complete second forcing

The complete exterior values are


$$
\boxed{
B=(197,234,54,56,248,208,112,128,128)\pmod{256}.
}
\tag{26}
$$


All nine are inserted in (16).

The complete polynomial second forcing after the retained exterior decomposition is


$$
\boxed{
q_{\rm force}=66\mathscr A+128\left(x+\binom x7\right)\pmod{256}.
}
\tag{27}
$$



The entire logarithmic force is absent only by the retained whole-force bound, which exceeds the required eight bits on the original domain. The entire exponential tail beyond $b+8$ is absent because


$$
v_2((b+9)!/b!)=8.
$$



Thus (27) is a complete forcing statement at the stated raw precision.

---

## 11. Finite inverse formulas

The correction matrix is even, so its finite inverse has a terminating geometric expansion modulo every fixed power of two.

### First column

Modulo $128$, $128F$ disappears. Therefore


$$
\boxed{
P_{128}=
\sum_{\ell=0}^{6}(-66)^\ell\mathscr E^\ell g
\pmod{128}.
}
\tag{28}
$$



Using (25), only


$$
\ell\le6,\quad4,\quad2,\quad0
$$


are required for the pieces of depths $0,2,4,6$, respectively. Hence


$$
\boxed{\deg P_{128}\le27.}
\tag{29}
$$


The four piecewise degree bounds are $27,21,15,11$.

### Second column

Modulo $256$, every word containing $128F$ and any additional contact insertion vanishes. Thus


$$
\boxed{
Q_{256}
=
66\sum_{\ell=0}^{6}(-66)^\ell\mathscr E^\ell\mathscr A
+
128\left(x+\binom x7\right)
\pmod{256}.
}
\tag{30}
$$



Since $\deg\mathscr A\le3$,


$$
\boxed{\deg Q_{256}\le27.}
\tag{31}
$$



Equations (28) and (30) include every surviving inverse term.

---

## 12. Actual reconstruction and exterior moments

The actual large kernel is not replaced:


$$
\boxed{
\theta=T(-2n)\mathcal S_bP_{128}\pmod{128},
}
\tag{32}
$$




$$
\boxed{
\eta_i=
-\sum_{a=0}^{8}B_a\binom{-2n}{b+a-i}
+\bigl(T(-2n)\mathcal S_bQ_{256}\bigr)_i
\pmod{256}.
}
\tag{33}
$$



Extend the actual interior solutions by


$$
\theta_{-1}=\theta_b=\eta_{-1}=\eta_b=0
$$


for reconstruction. Then


$$
\boxed{
2X_j\equiv W_j(j\theta_{j-1}-\theta_j)\pmod{128},
}
\tag{34}
$$




$$
\boxed{
4Y_j\equiv
W_b\mathbf1_{j=b}+W_j(j\eta_{j-1}-\eta_j)
\pmod{256}.
}
\tag{35}
$$



The endpoint $+1$ is retained.

For the complete difference polynomial, set


$$
d=Q_{256}-2P_{128}\pmod{256}.
$$


This is well-defined: knowing $P\pmod{128}$ determines $2P\pmod{256}$.

The nine negative-moment coefficients remain


$$
\beta=(113,202,78,200,248,80,240,128,128)\pmod{256}.
$$


After reconstruction, the strictly negative part is exactly


$$
\begin{array}{c|l}
s&V_s(x)\\ \hline
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
\end{array}
\pmod{256}.
\tag{36}
$$



Here $Z_0$ comes from the newly computed $d$, not from the old fifth-precision vector.

For later moment reconstruction, bounded factors such as


$$
\binom{2n+s-1}{s}
$$


should initially be retained with their actual parameters. No automatic substitution by the old $\binom{s+3}{3}$ is claimed at the new degree and precision.

---

# Part IV. Coefficient-valued cylinder transfer

## 13. Parameter estimates

For integer $z,\delta$ and $r\ge1$,


$$
v_2\!\left(\binom{z+\delta}{r}-\binom zr\right)
\ge v_2(\delta)-\lfloor\log_2r\rfloor.
\tag{37}
$$



For an operator applied to a polynomial of degree $d$:

* changing $n$ in $\mathscr E$ involves only lower binomial indices at most $4$;
* changing $b$ involves lower indices at most $d+4$;
* changing $b$ in $\mathscr A$ involves lower indices at most $3$, because of (16).

These estimates are coefficient-valued. One way to verify that assertion is to prove the divisibility uniformly at integer $x$, then take finite differences:


$$
[\binom xr]f=\Delta^rf(0).
$$


Integral finite differences do not lose powers of two.

For iterates, use a telescoping difference of compositions. Every unchanged operator is integral and preserves the divisibility already obtained.

---

## 14. Why $b=209$ is valid for $P_{128}$

Consider a forcing component of depth $a$ and degree $d_a$, where


$$
(a,d_a)\in\{(0,3),(2,5),(4,7),(6,11)\}.
$$


Its $\ell$-th inverse term has scalar depth $a+\ell$. For $\ell\ge1$, a safe maximum endpoint-binomial index is


$$
d_a+4\ell.
$$


Thus, under $b\mapsto b+256z$, its coefficient change has depth at least


$$
\boxed{
a+\ell+8-\lfloor\log_2(d_a+4\ell)\rfloor.
}
\tag{38}
$$



For every retained term $a+\ell\le6$, this is at least $7$. The sharp initial case is


$$
a=0,\quad\ell=1:\qquad 1+8-\lfloor\log_27\rfloor=7.
$$


The depth-two and depth-four forcing pieces have enough extra powers of two to absorb their larger binomial indices.

The depth-six piece has only $\ell=0$, so it has no endpoint dependence at all.

For $n\mapsto n+512z$, each changed $U$-operator has depth at least


$$
9-\lfloor\log_24\rfloor=7
$$


before the inverse scalar is counted, more than sufficient.

Therefore


$$
\boxed{
P_{128}(n,b)\equiv P_{128}(322,209)\pmod{128}
}
\tag{39}
$$


coefficientwise on the original domain.

This is precisely where the graded forcing split is essential.

---

## 15. Why $b=209$ is also valid for $Q_{256}$

Write $m=\ell+1$ for the total number of $U$-insertions, counting the exterior insertion. Its scalar depth is $m$, with $1\le m\le7$.

The maximum endpoint-binomial index is


$$
4m-1.
$$


Thus a $256$-shift in $b$ changes the weighted term by depth at least


$$
\boxed{
m+8-\lfloor\log_2(4m-1)\rfloor.
}
\tag{40}
$$


For $m=1,\ldots,7$, these lower bounds are


$$
8,\ 8,\ 8,\ 9,\ 9,\ 10,\ 10.
$$


Every one meets the required eight bits.

For $n$, the lower indices in each $U$-insertion are at most $4$, and


$$
m+9-2\ge8.
$$



The $128V$ insertion needs only parity. Its $n$-indices are at most $8$ and its exterior $b$-indices at most $7$, so the same cylinders are amply sufficient.

The exterior vector $B$ has already been proved constant modulo $256$ on the original domain. Hence


$$
\boxed{
Q_{256}(n,b)\equiv Q_{256}(322,209)\pmod{256}
}
\tag{41}
$$


coefficientwise.

### Proven sufficient cylinder

The complete bounded coefficient pair depends only on


$$
\boxed{n\bmod512,\qquad b\bmod256}
\tag{42}
$$


within the specified forcing and exterior-data class. This is a sufficient cylinder, not a claim of minimal period.

On the original affine relation $n=4002b$, a shift of $b$ by $256$ shifts $n$ by a multiple of $512$. The original family occupies the single cylinder (6).

This coefficient transfer does **not** make the actual $T(-2n)$, weights, or high-binomial sums periodic. Those remain actual.

---

# Part V. The next bounded calculation

## 16. Exact inputs

The next computation should not recompute the eight central states. Its inputs are:

1. Reference parameters
   

$$
n_0=322,\qquad b_0=209.
$$


2. The forcing vector
   

$$
g=(66,247,115,135,76,92,176,112,0,192,64,64).
$$


3. The exterior vector
   

$$
B=(197,234,54,56,248,208,112,128,128).
$$


4. The operators (1)–(2), or equivalently (13).
5. The exact exterior polynomial (16).
6. The coefficients $u=(-1,2,-3,3)$.
7. Formulas (28) and (30).

All operations can be performed in exact rational polynomial arithmetic followed by Newton conversion, or directly in integral Newton arithmetic. No even modular denominator may be inverted.

---

## 17. Required outputs and verifiable assertions

Compute:

### A. Complete boundary polynomial


$$
\mathscr A=\sum_{s=1}^{4}u_s\mathscr A_s.
$$


Output all four Newton coefficients modulo $128$. Its degree is proved to be at most $3$.

Independently verify its defining finite exterior sum at four integer rows, for example $x=0,1,2,3$. Since both sides are degree at most $3$, this gives an exact polynomial check when done before modular reduction.

### B. Complete coefficient vectors


$$
(p_0,\ldots,p_{27})\pmod{128},
$$




$$
(q_0,\ldots,q_{27})\pmod{256},
$$


from (28) and (30), and


$$
d_r=q_r-2p_r\pmod{256}.
$$



The expected verifiable outputs are the coefficient vectors themselves and the following residual identities:


$$
\boxed{
(I+66\mathscr E)P_{128}-g\equiv0\pmod{128},
}
\tag{43}
$$




$$
\boxed{
(I+66\mathscr E+128\mathscr F)Q_{256}
-\bigl(66\mathscr A+128\mathscr J\bigr)
\equiv0\pmod{256}.
}
\tag{44}
$$



For a full polynomial residual certificate, allow degree through $35$: applying the degree-eight operator to a degree-$27$ polynomial can formally reach that degree, even though its weighted terms should vanish.

### C. Explicit new insertion
Verify


$$
128\mathscr J
=
128\left(\binom x1+\binom x7\right)\pmod{256}.
\tag{45}
$$



### D. Lower-precision consistency
The reductions should agree with the retained complete vectors:


$$
P_{128}\bmod64
=
(34,31,7,5,48,12,4,4,32,8,56,8,0,\ldots),
\tag{46}
$$




$$
Q_{256}\bmod128
=
(52,36,24,6,112,48,64,8,32,32,64,112,0,\ldots).
\tag{47}
$$



These are consistency assertions, not replacements for (43)–(44).

### E. Optional direct finite-block check

At the bounded reference $b_0=209$, form the actual matrices $C_s^{II}$ from (8) for $s=1,\ldots,8$, and the nine exterior columns. Check the signed polynomial action against the matrix action for the computed vectors.

This is a $209$-row bounded audit of the finite identity. The proof of (10) and (16), not that finite audit, supplies arbitrary-$b$ validity.

No original enormous $b$, high-$t$ sum, norm, or mixed contraction is needed.

---

# Part VI. Precision and the remaining global obstruction

## 18. What the new coefficient calculation will determine

The output gives


$$
2X\bmod128,\qquad4Y\bmod256,
$$


hence


$$
X,Y\bmod64.
$$



Because $X,Y$ are even, this determines


$$
N\bmod256,\qquad H\bmod128.
$$


It does **not** automatically determine $H\bmod256$.

Indeed, if


$$
X=x+64a,\qquad Y=y+64b,
$$


then


$$
XY-xy\equiv64(ay+bx)\pmod{256}.
$$


With even $x,y$, the right side can have valuation exactly $7$.

Thus the immediate next task is the complete joint carry at modulus $128$. A full modulus-$256$ mixed theorem requires extra column precision or a separate proof of cancellation of the remaining correction.

The new weight-depth cutoff remains valid at its stated scope:


$$
v_2(W_j)\ge5
\Longrightarrow X_j^2\equiv X_jY_j\equiv0\pmod{256}.
$$


It does not reinstate the old 31-class support. All actual low-weight coordinates, new overflow patterns, and terminal boundaries must be retained in the next contraction.

---

## 19. Final gcd, actual denominator, and whole error

No normalization has changed. With the least actual clearer $d_B$, write


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
$$


The primitive multiplier on the uncleared quadratic pair is


$$
\frac{d_B^2}{g_B}.
$$



Retaining the established binary interface,


$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\},
}
$$


where


$$
\alpha=v_2(N),\qquad\gamma=v_2(H).
$$



The finite transport result does not itself improve a bound on $\gamma-\alpha$.

At the retained scope of the whole signed-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The complete primitive evaluated form remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
$$



Neither a contact coefficient congruence nor finitely many aligned carries proves that this whole nonzero form tends to zero.

---

# Final ledger

## New result and proof status

**Proved in the retained finite Pascal contact convention:**

* the arbitrary divided-power monomial kernel and signed finite-suffix operator;
* exact lower-boundary handling and the true upper boundary $b-1$;
* the complete exterior-column insertion;
* transport of $66U+128V$, including degrees $5,7,8$;
* matrix-level vanishing of all mixed $128V$/additional-$66U$ insertions;
* the surviving single exterior insertion
  

$$
128\left(x+\binom x7\right);
$$


* complete finite formulas for $P_{128}$ and $Q_{256}$;
* degree bounds $27,27$;
* coefficient-valued transfer to $n=322,b=209$, with a sufficient cylinder $n\bmod512,b\bmod256$.

**Finite computation still to be performed:** the actual new coefficient vectors and their residual certificates (43)–(47). This is a bounded polynomial calculation, not the completed eight-state local source calculation.

## Exact next mathematical bottleneck

After those coefficients are obtained, the remaining local-to-global task is to evaluate the complete joint norm–mixed carry using:

* actual $T(-2n)$ and weights;
* all nine exterior entries;
* reconstructed negative moments through $-10$;
* the newly admitted weight-depth-four coordinates;
* correct overflow kernels and actual terminal ranges.

Coefficient-cylinder transfer does not evaluate that unbounded contraction.

## Status of the research objective

The finite contact-transport obstruction is resolved at the stated algebraic interfaces, and the next coefficient computation is fully specified. The joint carry, unrestricted relative valuation, full final-gcd control, and same-index whole-error comparison remain outstanding.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi\text{ is obtained.}}
$$


