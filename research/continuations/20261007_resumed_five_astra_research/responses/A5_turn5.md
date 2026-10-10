> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 5 — The actual modulo-$4$ inverse, exclusion of content zero, and a paid source consequence

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved. The new result here is an unconditional statement about the **actual original binary family**


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$



Write


$$
h=\frac n2,\qquad d=\frac{b-1}{4},\qquad
g=\frac{h+1}{2}=\frac{n+2}{4},
$$


and let $z^f=A^{-1}\mathfrak f$ be the original finite contact solution. I prove the following explicit inverse formulas:


$$
\boxed{
z^f_{4s}\equiv
\begin{cases}
2\displaystyle\binom{h+d-s}{d-s}\pmod4,&s\ \text{even},\\[4pt]
0\pmod4,&s\ \text{odd},
\end{cases}
\qquad 0\le s\le d,
}
\tag{A}
$$


and


$$
\boxed{
z^f_{4s+2}\equiv
\bigl(2+(-1)^s\bigr)
\binom{h+d-s-1}{d-s-1}\pmod4,
\qquad 0\le s<d.
}
\tag{B}
$$


These formulas include the effects of the finite upper boundary. They are not infinite-matrix inversions.

The original parameter congruences force every residue in (A) on the odd-weight Lucas mask to vanish:


$$
\boxed{
\binom{n+2}{j}\ \text{odd}
\quad\Longrightarrow\quad
z^f_j\equiv0\pmod4.
}
\tag{C}
$$


Consequently the actual first-column content satisfies


$$
\boxed{a\ge1\quad\text{for every original }u\ge0.}
\tag{D}
$$


Thus the two previously computed rows $j=0,4$ were consistent with a universal obstruction: **there is no content-zero witness anywhere on the Lucas mask.**

There are three further concrete advances.

* The entire actual force, not just a finitely checked head, is evaluated modulo $8$:
  

$$
\boxed{
  \mathfrak f_i\equiv
  \begin{cases}
  2,1,3,1,4,4,&i=0,1,2,3,4,5,\ \text{respectively},\\
  0,&i\ge6
  \end{cases}\pmod8.
  }
  \tag{E}
$$


* The physical row $b-1$ gives an exact nonzero reconstructed digit:
  

$$
\boxed{
  v_2(x_{b-1})=v_2\binom gd.
  }
  \tag{F}
$$


  In particular, the supplied original $u=0$ weight valuations imply the improved bound
  

$$
\boxed{1\le a(0)\le21,}
$$


  rather than the previous upper bound $23$.
* For the complete exponential source, including its finite returns, the vector
  

$$
\tau_j=W_j\Delta_jz^k\quad(j<b),\qquad
  \tau_b=W_b(bz^k_{b-1}+1)
$$


  is divisible by $4$ in every physical row. Hence
  

$$
\boxed{
  Q=x_0^Tx_0,\qquad E=x_0^T(\tau/4)\in\mathbb Z_2.
  }
  \tag{G}
$$


  This is a paid primitive integrality result. It is **not** a nonzero primitive digit or a relative scalar law.

The sharp value of $a$, and an independently defined $r(u)$ satisfying a useful law $E-r(u)Q$, remain open. A four-state, whole-word binary calculation is specified below to seek a sharp $a=1$ witness without constructing the original matrix.

---

## 1. Original objects and scope

Throughout,


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The contact indices are exactly $0\le i,j<b$; physical reconstruction has exactly $0\le j\le b$.

Retain


$$
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n},\qquad
\phi(z)=1-z+\frac{z^2}{2},
$$




$$
\lambda_s=s![z^s]\phi(z)^n,\qquad W_j=\binom{n+2}{j},
$$


and


$$
A_{ij}
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j}.
$$


The normalized force is


$$
\mathfrak f_i
=
\frac{(n+i)!}{n!R}
[t^n](1+2t+2t^2)^n(1+t)^i.
$$



With


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),\qquad z_{-1}=z_b=0,
$$


the corrected columns remain


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


No logarithmic force is removed from $y$.

Write


$$
x=2^ax_0,\qquad z^f=A^{-1}\mathfrak f,
$$


where $a$ is the actual first-column binary content, and


$$
z^k=A^{-1}k,\qquad
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$



The complete raw observations are


$$
\mathcal U
=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
\tag{1.1}
$$




$$
\mathcal V
=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)(\Delta_jz^k)
+W_b^2bz^f_{b-1}(bz^k_{b-1}+1),
\tag{1.2}
$$


and


$$
Q=2^{-2a-2}\mathcal U,\qquad
E=2^{-a-3}\mathcal V.
\tag{1.3}
$$



### Source assessment

The parent-authored receipts establish their stated finite computations:

* the $u=0$ paid force head modulo $256$;
* the two supplied endpoint weight valuations $25,24$;
* the selected inverse residues at $u=0,\ldots,4$;
* the auxiliary coefficient and $b=17$ inverse comparisons.

Their authorship fields and hashes are not mathematical proofs. Their finite outputs are not extrapolated here. In particular, the absence of a witness among the selected rows did not establish $a\ge1$.

The completed-boundary theorem and its bounded-precision hypotheses are reused, not re-proved. The derivative-image quotient is also reused: derivative certificates are sufficient but strictly stronger than terminal acceptance. No actual derivative-image membership is asserted.

---

## 2. The actual force head on every original index

The supplied exact force identities and recurrence are sufficient, but the recurrence has a useful additional integrality feature.

Let $F_i=\mathfrak f_i$. The established recurrence is


$$
\begin{aligned}
2F_{i+2}={}&(4n+4i+6)F_{i+1}\\
&-(3i+n+2)(n+i+1)F_i\\
&+i(n+i)(n+i+1)F_{i-1}.
\end{aligned}
\tag{2.1}
$$



### 2.1 The recurrence division can be paid in its coefficients

Because $n$ is even,


$$
(3i+n+2)(n+i+1)\equiv i(i+1)\equiv0\pmod2,
$$


and


$$
i(n+i)(n+i+1)\equiv i^2(i+1)\equiv0\pmod2.
$$


Thus (2.1) is the integral recurrence


$$
\begin{aligned}
F_{i+2}={}&(2n+2i+3)F_{i+1}\\
&-\frac{(3i+n+2)(n+i+1)}2F_i\\
&+\frac{i(n+i)(n+i+1)}2F_{i-1}.
\end{aligned}
\tag{2.2}
$$



The displayed divisions are exact integer divisions of the coefficients. They need not cause a loss of one force bit at every step.

More precisely, if two even parameters $n,n'$ satisfy


$$
n\equiv n'\pmod{2^{L+1}},
$$


then every coefficient of (2.2) agrees modulo $2^L$. The numerators are integer polynomials in $n$, and their differences are divisible by $n-n'$; dividing by $2$ therefore leaves divisibility by $2^L$.

This does not invalidate the paid seed receipt: its per-step payment was safe, although more conservative than necessary for this recurrence.

### 2.2 Comparison with an exactly evaluable auxiliary parameter

On the original family,


$$
h\equiv1\pmod{32},\qquad n\equiv2\pmod{64}.
$$


The previously proved central and adjacent force identities give


$$
F_0\equiv2,\qquad F_1\equiv1\pmod8.
\tag{2.3}
$$



For the auxiliary value $n'=2$, one has $R'=4$ and


$$
(1+2t+2t^2)^2=1+4t+8t^2+8t^3+4t^4.
$$


Consequently its force is exactly


$$
F_i^{(2)}
=
\frac{(i+2)!}{8}
\left(\binom i2+4i+8\right).
\tag{2.4}
$$


The first values are


$$
2,\ 9,\ 51,\ 345,\ 2700,\ 23940.
$$


For $i\ge6$,


$$
v_2((i+2)!)-3\ge4,
$$


so (2.4) is zero modulo $8$.

The original recurrence coefficients agree with the $n'=2$ coefficients modulo $8$, and the two seeds agree modulo $8$. Induction in (2.2) proves:

### Theorem 2.1 — Whole original force modulo $8$

For every original index and every $i\ge0$,


$$
\boxed{
F_i\equiv
\begin{cases}
2,&i=0,\\
1,&i=1,\\
3,&i=2,\\
1,&i=3,\\
4,&i=4,5,\\
0,&i\ge6
\end{cases}\pmod8.
}
\tag{2.5}
$$



This is a proof on the original family, not an extrapolation from the $u=0$ receipt. The auxiliary parameter was used only to solve a congruent integral recurrence.

In particular,


$$
\boxed{\mathfrak f\equiv(2,1,3,1,0,0,\ldots)^T\pmod4.}
\tag{2.6}
$$



---

## 3. A finite modulo-$4$ inverse with its boundary retained

The goal is now the actual inverse on the Lucas mask. Only a small operator calculation is needed.

### 3.1 Divided-power operators

Use divided powers


$$
z^{[j]}=\frac{z^j}{j!},
$$


and let


$$
D=\partial_z,\qquad U_\gamma=(1+D)^\gamma.
$$


These operators are well-defined on each finite polynomial, including for negative $\gamma$.

Let $\pi$ denote restriction to $0,\ldots,b-1$, and $\iota$ zero-padding from those contact coordinates. The finite operators below always retain these maps.

The established factorization is


$$
A=P_bM_b,\qquad
M_b=\pi U_nH_\lambda U_n\iota,
\tag{3.1}
$$


where $P_b$ is the finite Pascal matrix and $H_\lambda$ is multiplication by $\phi(z)^n$ in the divided-power basis.

At modulus $4$,


$$
(\lambda_0,\ldots,\lambda_4)\equiv(1,2,0,2,2),
\qquad \lambda_s\equiv0\quad(s>4).
$$


Thus


$$
H_\lambda=1+2H_\gamma\pmod4,
\qquad
\gamma=z^{[1]}+z^{[3]}+z^{[4]}
\quad\text{over }\mathbb F_2.
\tag{3.2}
$$



### 3.2 The relevant conjugation

Over $\mathbb F_2$,


$$
U_n=(1+D^2)^h.
$$


Since


$$
\gamma''=z^{[1]}+z^{[2]},\qquad \gamma^{(4)}=1,
$$


the divided-power Leibniz rule gives


$$
U_nH_\gamma U_{-n}
=
H_\gamma
+hH_{\gamma''}(1+D^2)^{-1}
+\binom h2(1+D^2)^{-2}.
$$


Here $h$ is odd and $h\equiv1\pmod4$, so


$$
\boxed{
C:=U_nH_\gamma U_{-n}
=
H_\gamma+H_{\gamma''}U_{-2}
\quad\text{over }\mathbb F_2.
}
\tag{3.3}
$$



It follows that


$$
M_b=(1+2C_b)U_{4h}^{(b)}\pmod4,
\qquad C_b=\pi C\iota.
\tag{3.4}
$$


Therefore, for $q=P_b^{-1}\mathfrak f$,


$$
\boxed{
z^f
=
U_{-4h}^{(b)}q
-2U_{-4h}^{(b)}C_bq
\pmod4.
}
\tag{3.5}
$$



This is a finite inverse identity. The projections in $C_b$ are compulsory. In particular, (3.4) was obtained by conjugating the full operator before contact restriction; it includes the paths that leave the contact range under multiplication and return under $U_n$.

### 3.3 The complete transformed force

From (2.6),


$$
q_j
=
(-1)^j
\left(2-j+3\binom j2-\binom j3\right)
\pmod4.
\tag{3.6}
$$


It has period $8$, with table


$$
\begin{array}{c|rrrrrrrr}
j\bmod8&0&1&2&3&4&5&6&7\\ \hline
q_j\bmod4&2&3&3&1&0&3&1&1.
\end{array}
\tag{3.7}
$$


The whole prefix $0\le j<b$ is retained. It has not been truncated to the original four nonzero force entries.

In particular,


$$
q_{4t}=0,\qquad q_{4t+1}=q_{4t+2}=q_{4t+3}=1
\pmod2.
\tag{3.8}
$$



### 3.4 The finite correction vanishes in every even coordinate

Write $b=4d+1$. The original family has $d$ even.

For an even coordinate $i=4t$, all terms in


$$
(C_bq)_i=(H_\gamma q)_i+(H_{\gamma''}U_{-2}q)_i
$$


vanish modulo $2$: the only potentially nonzero multiplier from $H_\gamma$ is $\binom{i}{4}$, and it multiplies $q_{i-4}=0$.

For $i=4t+2$,


$$
(H_\gamma q)_{4t+2}\equiv t\pmod2.
$$


Also,


$$
(U_{-2}q)_{4t}
=
\sum_{\substack{r\ge0\\4t+2r<b}}q_{4t+2r}
\equiv d-t\pmod2.
\tag{3.9}
$$


This count uses the actual endpoint $b-1=4d$. Hence


$$
(C_bq)_{4t+2}\equiv t+(d-t)=d\equiv0\pmod2.
$$



Finally,


$$
U_{-4h}\equiv(1+D^4)^{-h}\pmod2,
$$


so it preserves coordinate classes modulo $4$. The correction in (3.5) is therefore zero in every even coordinate:


$$
\boxed{
z^f_j\equiv(U_{-4h}^{(b)}q)_j\pmod4
\quad(j\ \text{even}).
}
\tag{3.10}
$$



This is the point where the finite return calculation simplifies. No return was assumed zero in advance.

---

## 4. Evaluation of the even inverse coordinates

The generating series for the coefficients of $U_{-4h}$ satisfies


$$
(1+X)^{-4h}
\equiv
(1+X^4)^{-h}
-2hX^2(1+X^4)^{-h-1}
\pmod4.
\tag{4.1}
$$


Thus its coefficients are zero at odd indices, while


$$
[X^{4t}](1+X)^{-4h}=\binom{-h}{t}\pmod4,
$$




$$
[X^{4t+2}](1+X)^{-4h}
=-2h\binom{-h-1}{t}\pmod4.
\tag{4.2}
$$



### 4.1 Coordinates $4s$

Put $R=d-s$. Using (3.7) and (4.2),


$$
\begin{aligned}
z^f_{4s}\equiv{}&
\sum_{t=0}^{R}(-1)^t\binom{h+t-1}{t}
\bigl(1+(-1)^{s+t}\bigr)\\
&+2\sum_{t=0}^{R-1}\binom{h+t}{t}
\pmod4.
\end{aligned}
\tag{4.3}
$$


The second sum is zero when $R=0$.

Let


$$
B_R=\binom{h+R}{R},\qquad
O_R=\sum_{\substack{0\le t\le R\\t\text{ odd}}}
\binom{h+t-1}{t}.
$$


Hockey-stick summation transforms (4.3) into


$$
z^f_{4s}\equiv
(1+(-1)^s)B_R
+2\left(\binom{h+R}{R-1}-O_R\right)
\pmod4.
\tag{4.4}
$$



The expression in parentheses is even. To verify this explicitly, write $h=2H+1$. Lucas reduction gives


$$
\binom{h+2v}{2v+1}\equiv\binom{H+v}{v}\pmod2.
$$


If $R=2r$, then


$$
O_R\equiv\binom{H+r}{r-1}
\equiv\binom{h+R}{R-1}\pmod2.
$$


If $R=2r+1$, then


$$
O_R\equiv\binom{H+r+1}{r}
\equiv\binom{h+R}{R-1}\pmod2.
$$


The $R=0$ case follows from the zero convention.

We obtain


$$
\boxed{
z^f_{4s}\equiv
(1+(-1)^s)\binom{h+d-s}{d-s}\pmod4.
}
\tag{4.5}
$$



### 4.2 Coordinates $4s+2$

Here put $R=d-s-1$. In the $4t+2$ part of (4.2), the corresponding $q$-coordinate is a multiple of $4$, hence even; that contribution vanishes modulo $4$.

For the $4t$ part,


$$
q_{4(s+t)+2}=2+(-1)^{s+t}\pmod4.
$$


Consequently


$$
\begin{aligned}
z^f_{4s+2}
&\equiv
\sum_{t=0}^{R}
(-1)^t\binom{h+t-1}{t}
\bigl(2+(-1)^{s+t}\bigr)\\
&\equiv
\bigl(2+(-1)^s\bigr)
\sum_{t=0}^{R}\binom{h+t-1}{t}\pmod4,
\end{aligned}
$$


which proves


$$
\boxed{
z^f_{4s+2}\equiv
\bigl(2+(-1)^s\bigr)
\binom{h+d-s-1}{d-s-1}\pmod4.
}
\tag{4.6}
$$



Equations (4.5)–(4.6) are evaluated finite-inverse formulas, not merely names for an unevaluated $b$-term sum.

---

## 5. Every odd-weight residue vanishes: $a\ge1$

The original exponent supplies more information than the previously used congruence modulo $32$:


$$
9^{18+32u}\equiv209\pmod{256}.
\tag{5.1}
$$


Indeed, $9^{32}\equiv1\pmod{256}$ and $9^{18}\equiv209\pmod{256}$.

It follows that


$$
d=\frac{b-1}{4}\equiv52\pmod{64},
$$




$$
h=2001b\equiv33\pmod{128},
\qquad
g=\frac{h+1}{2}\equiv17\pmod{64}.
\tag{5.2}
$$



Since $n+2=4g$, Lucas’s theorem says


$$
W_j\ \text{odd}
\quad\Longleftrightarrow\quad
j=4s,\quad s\ \text{a binary submask of }g.
\tag{5.3}
$$



If $s$ is odd, (4.5) gives $z^f_{4s}=0\pmod4$.

Suppose $s$ is even and a submask of $g$. The low six bits of $g$ are those of $17$, so


$$
s\equiv0\ \text{or }16\pmod{64}.
$$


Therefore


$$
d-s\equiv52\ \text{or }36\pmod{64}.
$$


Both residues have binary bit $5$ equal to $1$. The same is true of $h$, because $h\equiv33\pmod{128}$. Thus


$$
h\mathbin{\&}(d-s)\ne0.
$$


The no-carry form of Lucas’s theorem yields


$$
\binom{h+d-s}{d-s}\equiv0\pmod2.
$$


Equation (4.5) again gives $z^f_{4s}=0\pmod4$.

We have proved:

### Theorem 5.1 — Actual Lucas-mask vanishing

For every original $u\ge0$,


$$
\boxed{
0\le j<b,\quad W_j\ \text{odd}
\quad\Longrightarrow\quad z^f_j\equiv0\pmod4.
}
\tag{5.4}
$$



The already proved sharp criterion was


$$
a=0
\iff
\exists\,j<b:\ W_j\ \text{odd and }z^f_j\equiv2\pmod4.
$$


Together with the established nonnegativity of $a$, Theorem 5.1 proves


$$
\boxed{a\ge1\quad\text{on the entire unchanged original family}.}
\tag{5.5}
$$



The proof does not choose a freely extendable binary suffix. It first evaluates the actual finite inverse and then finds an obstruction in bits that every original parameter necessarily has.

---

## 6. An actual nonzero reconstructed digit and an improved bound

Set $s=d$ in (4.5). Since $d$ is even,


$$
z^f_{b-1}=z^f_{4d}\equiv2\pmod4.
\tag{6.1}
$$


Also $b-1$ is divisible by $16$. Hence


$$
\Delta_{b-1}z^f
=(b-1)z^f_{b-2}-z^f_{b-1}\equiv2\pmod4.
$$


This proves the exact valuation


$$
v_2(\Delta_{b-1}z^f)=1.
\tag{6.2}
$$


Therefore


$$
\boxed{
v_2(x_{b-1})=v_2(W_{b-1})
=v_2\binom{4g}{4d}
=v_2\binom gd.
}
\tag{6.3}
$$


The last equality follows directly from the binary digit-sum formula for binomial valuations.

Thus


$$
\boxed{
1\le a\le v_2\binom gd.
}
\tag{6.4}
$$


Moreover,


$$
2^{-v_2(\binom gd)}x_{b-1}
$$


is an odd $2$-adic unit. This is an actual evaluated nonzero reconstructed digit, although it is not yet proved to be the first nonzero digit of the entire column.

### 6.1 Consequence at the already computed original index $u=0$

There is no need to repeat the weight computation. Exactly,


$$
\frac{W_{b-1}}{W_{b-3}}
=
\frac{(4001b+5)(4001b+6)}{(b-2)(b-1)}.
$$


On the original family,


$$
v_2(4001b+5)=1,\quad
v_2(4001b+6)=0,\quad
v_2(b-2)=0,\quad v_2(b-1)=4.
$$


Consequently


$$
v_2(W_{b-1})=v_2(W_{b-3})-3.
\tag{6.5}
$$


The supplied $u=0$ value $v_2(W_{b-3})=24$ therefore gives


$$
\boxed{v_2(x_{b-1})=21,\qquad 1\le a(0)\le21.}
\tag{6.6}
$$



The sharp actual $a(0)$ has not been determined.

---

## 7. Seeking the next digit: a concrete $a=1$ witness pattern

Formula (4.5) gives a useful sufficient condition requiring only binary arithmetic.

Suppose


$$
s\ \text{is even},\qquad 0\le s\le d,
$$




$$
h\mathbin{\&}(d-s)=0,\qquad v_2\binom gs=1.
\tag{7.1}
$$


Then


$$
z^f_{4s}\equiv2\pmod4,\qquad
v_2(W_{4s})=v_2\binom gs=1.
$$


Since $4s\,z^f_{4s-1}\equiv0\pmod4$,


$$
v_2(x_{4s})=1.
$$


Combined with Theorem 5.1, this proves $a=1$.

There is an especially explicit row pattern. The original family has


$$
g\equiv81\pmod{128}.
$$


For


$$
\boxed{
s=32+16\varepsilon+128t,\qquad \varepsilon\in\{0,1\},
}
\tag{7.2}
$$


assume that $t$ is a binary submask of $\lfloor g/128\rfloor$. In subtracting $s$ from $g$, the low bits produce exactly one borrow, from bit $6$ to bit $5$, and the higher submask condition produces no further borrow. Therefore


$$
v_2\binom gs=1.
$$



We obtain the concrete sufficient witness lemma:

### Lemma 7.1 — A row pattern certifying sharp content one

If, at an original index, some $\varepsilon\in\{0,1\}$ and integer $t\ge0$ satisfy


$$
t\subseteq\left\lfloor\frac g{128}\right\rfloor,\qquad
s=32+16\varepsilon+128t\le d,
$$




$$
\boxed{h\mathbin{\&}(d-s)=0,}
\tag{7.3}
$$


then


$$
\boxed{
a=1,\qquad
j=4s=128+64\varepsilon+512t
}
$$


is an actual physical-row witness.

No existence claim for these $t$ is being inferred from the available receipts.

### 7.2 A four-state whole-word calculation

There is a small exact dynamic program that finds the best witness supplied by (4.5). It does not inspect $b$ rows.

Seek nonnegative integers $s,R,T_0$ satisfying


$$
s+R=d,\qquad s+T_0=g,\qquad s\ \text{even},\qquad R\mathbin{\&}h=0.
\tag{7.4}
$$


At binary position $k$, let the digits of $s,R,T_0$ be $\sigma,\rho,\tau$, and let the incoming carries in the two additions be $\alpha,\beta\in\{0,1\}$. The transition equations are


$$
\sigma+\rho+\alpha=d_k+2\alpha',
$$




$$
\sigma+\tau+\beta=g_k+2\beta'.
\tag{7.5}
$$


Impose


$$
\rho h_k=0,
$$


and $\sigma=0$ at $k=0$. Give the transition cost $\beta'$.

There are four carry states $(\alpha,\beta)$, and at most eight digit triples per state. Start and finish in state $(0,0)$, processing the **entire** binary words of $d,g,h$, with zero padding beyond their highest bits.

Kummer’s theorem identifies the total cost with


$$
v_2\binom gs.
$$


Thus an accepting path of cost $1$ supplies an exact $a=1$ certificate. More generally, a minimum-cost path of cost $\mu$ supplies an explicit row with


$$
v_2(x_{4s})=\mu,\qquad a\le\mu.
\tag{7.6}
$$



This is an explicit four-state algorithm with witnesses and a proof of its output meaning, not an unspecified minimum over the original matrix rows.

Its limitation is equally important:

> If the minimum cost is larger than $1$, that does not prove $a>1$. Odd-weight rows at the next inverse digit, and other reconstructed rows, may give a smaller valuation.

Accordingly, the sharp-content problem has not simply been renamed. We have a proved universal lower bound, an exact nonzero endpoint digit, an explicit immediate-witness pattern, and a bounded whole-word method for testing that pattern.

---

## 8. The complete exponential source modulo $4$

There is a useful paid consequence for $E$. It requires the complete source, not just the first exterior column.

At modulus $4$, the factorial prefix is


$$
a_0=1,\qquad a_1\equiv2,\qquad a_2\equiv2,\qquad
a_t\equiv0\quad(t\ge3).
$$


Indeed, $b+1$ has valuation $1$, $b+2$ is odd, and $b+3$ has valuation $2$.

Thus the complete paid exterior source at this precision is


$$
s_{\mathrm{ext}}=e_b+2e_{b+1}+2e_{b+2}\pmod4.
\tag{8.1}
$$


This is only a modulo-$4$ simplification. It is not a replacement for the longer source prefix at higher precision.

Use the finite factorization (3.4), and put


$$
v=U_{4h}s_{\mathrm{ext}}.
$$


The transformed source is $q^k=\pi(1+2C)v$. Applying the finite inverse gives


$$
z^k
=
U_{-4h}^{(b)}
\left(\pi v+2\pi C v_{\mathrm{ext}}\right)\pmod4.
\tag{8.2}
$$


The second term is the retained exterior return.

Since


$$
\binom{4h}{1}\equiv0,\qquad
\binom{4h}{2}\equiv2\pmod4,
$$


one checks directly that


$$
v_{\mathrm{ext}}=s_{\mathrm{ext}}\pmod4,\qquad
v_{\mathrm{ext}}\equiv e_b\pmod2.
$$


Because $U_{-4h}v=s_{\mathrm{ext}}$, whose contact part is zero, (8.2) becomes


$$
z^k
=
-\pi U_{-4h}s_{\mathrm{ext}}
+2U_{-4h}^{(b)}\pi Ce_b
\pmod4.
\tag{8.3}
$$



For a row $j\equiv0\pmod4$, the first term vanishes:

* $b-j$ and $b+2-j$ are odd, so their inverse-binomial coefficients vanish modulo $4$;
* the coefficient at $b+1-j\equiv2\pmod4$ is even and is multiplied by $2$.

For the return term, $H_\gamma e_b$ has no contact part. The contact part of


$$
H_{\gamma''}U_{-2}e_b
$$


is supported only on $j\equiv3\pmod4$. Since $U_{-4h}$ modulo $2$ preserves coordinate classes modulo $4$, it cannot contribute to $j\equiv0\pmod4$.

Therefore


$$
\boxed{
z^k_j\equiv0\pmod4\qquad(j\equiv0\pmod4,\ j<b).
}
\tag{8.4}
$$



### 8.1 Divisibility of the whole physical source vector

Define


$$
\tau_j=W_j\Delta_jz^k\quad(0\le j<b),
\qquad
\tau_b=W_b(bz^k_{b-1}+1).
\tag{8.5}
$$



If $W_j$ is odd, then $j\equiv0\pmod4$, so (8.4) gives $\Delta_jz^k\equiv0\pmod4$.

If $v_2(W_j)=1$, then $j$ is even. The established source parity is supported only on $j\equiv1\pmod4$; hence $\Delta_jz^k$ is even at even $j$.

If $v_2(W_j)\ge2$, divisibility by $4$ is immediate. Finally, $v_2(W_b)\ge2$, so the physical terminal in (8.5) is also divisible by $4$.

Thus


$$
\boxed{\tau\in4\mathbb Z_2^{b+1}.}
\tag{8.6}
$$



Since $\mathcal Rz^f=2^{a+1}x_0$,


$$
\mathcal V=(\mathcal Rz^f)^T\tau
=2^{a+1}x_0^T\tau.
$$


All divisions are now explicit:


$$
\boxed{
E=2^{-a-3}\mathcal V=x_0^T(\tau/4)\in\mathbb Z_2,
\qquad
Q=x_0^Tx_0\in\mathbb Z_2.
}
\tag{8.7}
$$



This proves actual primitive integrality in the exponential channel. It does not show that either scalar is odd. A primitive vector can have an even sum of coordinate squares.

---

## 9. Paid relative precision and the scalar-law obstruction

Because $a\ge1$, the common payment simplifies:


$$
c=\max(2a+2,a+3)=2a+2.
$$


For an independently specified integral candidate $r(u)$,


$$
\boxed{
E-r(u)Q
=
2^{-2a-2}
\left(2^{a-1}\mathcal V-r(u)\mathcal U\right).
}
\tag{9.1}
$$



At the requested precision


$$
\boxed{L\ge2a+K+3,}
\tag{9.2}
$$


the raw observation has at least one guard bit beyond the common division needed for a congruence modulo $2^K$.

If a sharp $a=1$ witness is obtained, then


$$
Q=\mathcal U/16,\qquad E=\mathcal V/16,
$$


and the relative law is exactly


$$
\mathcal V-r(u)\mathcal U\equiv0\pmod{2^{K+4}}.
\tag{9.3}
$$


Neither (9.3) nor an independently defined $r(u)$ is proved here.

The actual obstruction is now more specific than before:

* the force head and the Lucas-mask inverse at modulus $4$ have been evaluated;
* the source return needed for primitive integrality has also been evaluated;
* but the scalar acceptance of
  

$$
2^{a-1}\mathcal V-r(u)\mathcal U
$$


  after the actual content division remains unknown.

The established derivative quotient cannot remove this obligation. It says that derivative membership is stronger than acceptance, not that the actual paid polynomial has zero acceptance.

Nor does a finite-depth binary law by itself give an all-prime denominator saving. For example, for fixed $K,r$ and arbitrarily large odd primes $q$,


$$
H=rq+2^K
$$


satisfies $H-rq\equiv0\pmod{2^K}$, yet $\gcd(q,H)=1$. This is only a logical limitation of the local congruence; it is **not** a disproof of a deeper source-specific law.

No proof is given that this particular producer can never yield the desired saving. Such an impossibility claim would require additional source-dependent information.

---

## 10. Retained higher-precision assembly, clearers, and whole error

The new low-precision simplifications must not be substituted into higher-precision observations.

At raw precision $2^L$, retain


$$
I=\min(b-1,8L-2),\qquad m=4(L-1),
$$




$$
T=\min(2L-1,2n-1),\qquad V=T+m,
$$


and impose the established bounded-precision condition


$$
\boxed{n>4(I+2m+T+4)+2.}
\tag{10.1}
$$



The complete source remains


$$
k=\sum_{t=0}^{2n-1}\frac{(b+t)!}{b!}\mathbf a_{b+t},
$$


with its paid prefix through $T$. The full return data remain


$$
\eta_f=U_n^{(m)}KS^{-1}D_f,
$$




$$
\xi_v=
\sum_{t=0}^Ta_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m}}
\binom n{t-r}\lambda_{v-r}\binom{b+v}{v-r},
$$




$$
\delta=KS^{-1}G^{[V]}\xi-\xi,\qquad
\theta_v=\sum_{w=v}^V\binom n{w-v}\delta_w.
\tag{10.2}
$$


The completed identities


$$
\widehat z^f=\overline z^f,\qquad
\widehat z^k=\overline z^k-s
\pmod{2^L}
$$


and the accepted whole-boundary cancellation are reused at that scope. Both differential boundaries and both physical terminal summands remain part of the construction.

### 10.1 Logarithmic guard

Retain


$$
\mathcal L_s=s![z^s]\frac{F(z)}{1-z},
\qquad
B_\star=n-v_2(b!)-1-2s_2(n)-\ell.
$$


The logarithmic contribution may be suppressed only where the original guard protects the requested observation **after all divisions**. The new content theorem does not extend that guard.

### 10.2 Actual least simultaneous clearer and final gcd

Retain


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j},
$$


and the actual least simultaneous clearer


$$
\boxed{
d_B=\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
}
\tag{10.3}
$$


No reconstructed row content is divided out.

With


$$
\mathcal N=x^Tx,\qquad \mathcal H=x^Ty,
$$


retain


$$
A_B=d_B^2\,4\Lambda^2R^2\mathcal N,\qquad
H_B=d_B^2\,8\Lambda Rb!\mathcal H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{10.4}
$$


This is the **all-prime** final gcd.

The retained primewise denominator identity is


$$
v_p(q_n)=
\max\left\{
v_p\!\left(\frac{\Lambda R}{2b!}\right)
+v_p(\mathcal N)-v_p(\mathcal H),0
\right\}.
$$


The previously established ternary law is retained only at its stated original-family scope:


$$
v_3(q_n)=n-\frac{b+15}{2}.
$$


It is not recomputed or strengthened here.

### 10.3 Same-index whole error

The relevant error remains


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
q_n(e+\pi)-p_n=-q_n\epsilon_n.
\tag{10.5}
$$


A producer-based irrationality proof still needs, on the **same infinitely many original indices**, both nonvanishing and a favorable bound involving the actual primitive denominator. For example,


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


would suffice: under rationality, these nonzero quantities would be bounded below by the reciprocal of a fixed denominator.

No result above evaluates or bounds that whole error.

---

## 11. A bounded new exact-arithmetic task

No tools were used for this report. The following proposed calculation is new; it does not repeat the paid $140$-term seed calculation or the closed inverse audit.

### Inputs

For $u=0,1,2,3,4$, form exactly


$$
b=9^{18+32u},\qquad
d=(b-1)/4,\qquad
h=2001b,\qquad g=(h+1)/2.
$$


Run the four-state binary procedure (7.5) on the entire input words.

All these integers have fewer than $480$ bits. The powers can be formed using at most $80$ ordinary integer multiplications in total, with a safe $1000$-bit intermediate-product bound.

For each case, the dynamic program has at most $481$ bit positions, four states, and eight candidate digit triples per state. Thus the five cases require fewer than


$$
\boxed{5\cdot481\cdot4\cdot8<77\,000}
$$


small transition tests and cost additions. Costs require at most nine bits. No original-size matrix, long coefficient vector, or large factorial is constructed.

### Expected verifiable output

For each original $u$, output:

1. the exact input integers $b,d,h,g$;
2. the minimum accepting cost $\mu$;
3. an accepting predecessor path and the reconstructed integer $s$;
4. the exact checks
   

$$
0\le s\le d,\qquad s\ \text{even},\qquad
   h\mathbin{\&}(d-s)=0;
$$


5. the carry count, independently checked by
   

$$
\mu=s_2(s)+s_2(g-s)-s_2(g);
$$


6. the resulting physical row $j=4s$ and certified valuation
   

$$
v_2(x_j)=\mu.
$$



At $u=0$, the output must satisfy $\mu\le21$, since $s=d$ is an admissible endpoint witness with the already derived cost $21$.

If $\mu=1$, the output certifies the sharp actual value $a=1$ at that finite original index. If $\mu>1$, it certifies only a stronger upper bound and an actual nonzero row digit. Neither outcome proves an infinite sharp-content law.

The concrete infinite follow-on lemma is now:

> Prove that the whole original words $b=9^{18+32u}$, on an explicitly specified infinite original subfamily, admit the row pattern of Lemma 7.1—or evaluate the next odd-weight inverse digit when they do not.

A computation on freely chosen binary suffixes would not address this lemma.

---

## 12. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Supplied $u=0$ force receipt and $u=0,\ldots,4$ selected-row receipt | Finite evidence at exactly their stated scope |
| Completed boundary theorem and corrected evaluator | Reused at their bounded-precision scope |
| Derivative-image quotient | Reused; no new membership claim |
| Whole actual force modulo $8$ | **Newly proved on every original index** |
| Explicit even-coordinate finite inverse modulo $4$ | **Newly proved** |
| Vanishing on every odd-weight Lucas-mask row | **Newly proved on every original index** |
| Actual content lower bound $a\ge1$ | **Newly proved** |
| Exact endpoint digit $v_2(x_{b-1})=v_2\binom gd$ | **Newly proved** |
| Original $u=0$ bound $1\le a(0)\le21$ | Proved from the new identity and the supplied finite weight valuation |
| Complete physical exponential source divisible by $4$ | **Newly proved at modulus $4$** |
| Paid integrality $Q,E\in\mathbb Z_2$ | **Proved** |
| Sharp actual $a$ on an infinite original subfamily | Open |
| Independently defined scalar law $E-r(u)Q$ | Open |
| Actual all-prime denominator versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The principal original-family content obligation at modulus $4$ is now closed:


$$
\boxed{
W_j\ \text{odd}\Longrightarrow z^f_j\equiv0\pmod4,
\qquad a\ge1.
}
$$



The next bottleneck is not another general boundary or quotient theorem. It is the **next paid digit of the actual reconstructed column and the actual scalar observation**. The four-state whole-word calculation above can provide a concrete sharp $a=1$ witness when one exists in the evaluated even-row family. Failing that, a genuine next-digit inverse calculation is required; the endpoint upper bound must not be relabeled as the actual content.

Even after a sharp local content theorem or a primitive relative congruence is obtained, the global objective still requires the actual least clearer, the all-prime final gcd, the resulting primitive denominator, and a nonzero whole error controlled on the same infinite original indices. No unconditional conclusion about $e+\pi$ follows yet.
