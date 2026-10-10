> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn16 — A five-digit modulo-$9$ killing word, its original-domain realization, and the exact Jacobi endpoint identity

## Executive conclusion

The inherited carry can be controlled without knowing its numerical suffix table.

The new local theorem is:



$$
\boxed{
m=(1^{25}M01011112)_3,\quad
M\text{ contains the consecutive word }20202
\quad\Longrightarrow\quad
a_m\equiv b_m\equiv0\pmod9.
}
$$



This statement concerns the **actual two endpoint coefficients**, with their inherited carries retained. Its proof uses:

1. an explicit evaluation of the two characteristic-three suffix states;
2. a universal four-digit annihilator for the seventeen-coordinate divided-carry module;
3. the paid modulo-$9$ reduction at the first digit of the word.

The annihilator is an identity of polynomial operators, not a finite sample of middle words.

There is also a valid original-domain realization. The fixed congruence


$$
\boxed{
m\equiv1194953\pmod{1594323}
}
$$


appends $20202$ immediately above the retained suffix $01011112$. It corresponds to a nonempty arithmetic progression of the original $j$'s, compatible with $j\equiv81\pmod{243}$. On that progression the exact real window has positive density. Consequently:



$$
\boxed{
\text{There is an original positive-density real-window family with }c_m\ge2.
}
$$



This does **not** upgrade $c_m\ge2$ to a relative-density-one assertion throughout every original window progression. That stronger assertion would require additional information about word occurrence or about a larger endpoint-killing language.

The normalization issue can also be closed. To eliminate the previous symbol collision, write


$$
X_m=[x^m]\mathcal A(x),\qquad Y_m=[x^m]\mathcal B(x).
$$


Then, exactly in characteristic zero,


$$
\boxed{
X_m=J_m^{[\,2m-1\,]}(-1),\qquad
Y_m=J_{m-1}^{[\,2m-1\,]}(-1).
}
$$


There is **no extra scalar** in either identity. The adjacent polynomial has the same parameter $A_{\mathrm{ind}}=2m-1$, not the parameter $2(m-1)-1$.

Finally, on the scalar Christoffel branch of the old source, the exact projective map is


$$
\boxed{
Z_{\rm src}(-1)
=
\frac{(1+\beta_m+\chi_m)X_m+\rho_mY_m}{A_{\mathrm{ind}}+74},
}
$$


where $\beta_m$ is the monic Jacobi recurrence coefficient and $\chi_m$ is the pole-evaluation Christoffel scalar. These are not the generating-function endpoints.

No code was executed. No result of the coordinator’s forthcoming modulo-$9$ checks is assumed below, and no accepted computation is proposed for repetition.

---

## 1. Scope and notation

Retain the original domain


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A_{\mathrm{ind}}=2m-1,
$$


and


$$
H_{\mathrm{win}}=3^{h-1},\qquad D=H_{\mathrm{win}}-A_{\mathrm{ind}},
$$


with the exact window


$$
\frac1{2C_{16}}<\frac D{H_{\mathrm{win}}}<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
\tag{1.1}
$$



The fixed suffix is


$$
m\equiv851\pmod{6561},
\qquad
851=(01011112)_3.
\tag{1.2}
$$



Throughout this report:

* $X_m,Y_m$ denote the generating-function endpoint coefficients called $a_m,b_m$ in turn15;
* $\beta_m,\gamma_m$ denote the monic Jacobi recurrence coefficients;
* $\chi_m$ denotes the scalar called $a_m$, or $a$, in the old Christoffel normalization;
* $\mathfrak a=\chi_m/3$, when that scalar branch is in force;
* $c_m=\min\{v_3(X_m),v_3(Y_m)\}$.

For the polynomial coordinate, retain


$$
a(u)=1+u,\qquad b(u)=1-u,\qquad Q(u)=1-u^2.
$$



The seventeen-coordinate module and its nine maps are reused from turn15:


$$
\mathscr N_9=(\mathbb Z/9\mathbb Z)[u]_{\le16},
$$




$$
\begin{aligned}
\mathcal T_{r,d}(N)(v)
=Q(v)^3\Lambda_0\Bigl(
&u^{-r}N(u)a(u)^{6-3r}b(u)^{6+r}\\
&-3d\,u^{1-r}N(u)a(u)^{6-3r}b(u)^{4+r}
\Bigr).
\end{aligned}
\tag{1.3}
$$


Here $r$ is the current ternary digit and $d$ the next, more significant digit. Thus the required one-digit lookahead remains explicit.

Write $\overline{\mathcal T}_r$ for reduction modulo $3$. Its dependence on the lookahead disappears, but only after reduction.

The initial endpoint numerators are


$$
N_X=b^7a^8,\qquad N_Y=u\,b^6a^9.
\tag{1.4}
$$



---

## 2. An explicit characteristic-three formula

Let


$$
C_r(F)(v)=\sum_{k\ge0}[u^{3k+r}]F(u)\,v^k.
$$


The seven-coordinate normalization is


$$
\iota(H)=b^6a^4H,\qquad \deg H\le6.
\tag{2.1}
$$



The induced characteristic-three maps have the useful closed form


$$
\boxed{
\Phi_r(H)=b\,a^{2-r}C_r(Hab^r),
\qquad r=0,1,2.
}
\tag{2.2}
$$



### Derivation

The corresponding differential has numerator $H$ and denominator $b^2a^4$. In characteristic three,


$$
\sigma(u)=\frac{\sigma(u^3)}{Q(u)}.
$$


After extracting a digit $r$, the denominator is


$$
a^{5+3r}b^{3-r}.
$$


Padding to $a^{6+3r}b^3$ multiplies the numerator by $ab^r$. Sectioning produces denominator $a^{2+r}b$. Multiplying the numerator by $ba^{2-r}$ restores denominator $a^4b^2$, proving (2.2).

In particular,


$$
\overline{\mathcal T}_r(\iota(H))=\iota(\Phi_r(H)).
\tag{2.3}
$$



This formula will supply operator identities valid for every polynomial in the stated degree range.

---

## 3. The actual suffix states and their inherited carries

Define


$$
R=-b(1+u^3),\qquad P=a^2b,\qquad T=ab^2.
\tag{3.1}
$$



Directly from (2.2),


$$
\begin{array}{c|ccc}
H&\Phi_0(H)&\Phi_1(H)&\Phi_2(H)\\ \hline
R&R&P&0\\
P&-R&P&0\\
T&P&-T&-b^2.
\end{array}
\tag{3.2}
$$



The initial seven-coordinate endpoint numerators are


$$
H_X=ba^4,\qquad H_Y=ua^5.
$$


Their first, units-digit transitions are


$$
\Phi_2(H_X)=T,\qquad \Phi_2(H_Y)=P.
\tag{3.3}
$$



The suffix is read from low to high as


$$
2,1,1,1,1,0,1,0.
$$


Four consecutive $1$'s leave $(T,P)$ unchanged. The last three transitions give


$$
(T,P)\xrightarrow{0}(P,-R)
\xrightarrow{1}(P,-P)
\xrightarrow{0}(-R,R).
$$



Thus the **actual two suffix states**, modulo $3$, are


$$
\boxed{
(N_X^{\rm suf},N_Y^{\rm suf})
\equiv(-\iota(R),\iota(R))\pmod3.
}
\tag{3.4}
$$



This evaluation is independent of the following digit, because lookahead contributes only to the second layer.

### 3.1 Exact modulo-$9$ suffix preparation

For a next digit $d\in\{0,1,2\}$, define the exact suffix operator


$$
\boxed{
\mathcal S_d=
\mathcal T_{0,d}\mathcal T_{1,0}\mathcal T_{0,1}
\mathcal T_{1,0}\mathcal T_{1,1}^{\,3}\mathcal T_{2,1}.
}
\tag{3.5}
$$


Composition is from right to left.

The actual suffix carries are therefore the well-defined elements


$$
\boxed{
C_X^{(d)}
=\frac{\mathcal S_d(N_X)+\iota(R)}3\pmod3,
\qquad
C_Y^{(d)}
=\frac{\mathcal S_d(N_Y)-\iota(R)}3\pmod3.
}
\tag{3.6}
$$



The divisions are justified by (3.4), and their values are defined by modulo-$9$ numerators. No zero residue modulo $3$ is being divided without paying the extra digit.

Equation (3.6) is an exact symbolic description, not a claimed numerical evaluation of the pending suffix-carry table.

### 3.2 Carry propagation before the first $2$

Before an absorbing middle digit occurs, use a common signed representative


$$
H\in\{R,-R,P,-P\}
$$


and write


$$
N_X=-\iota(H)+3C_X,\qquad
N_Y=\iota(H)+3C_Y\pmod9.
\tag{3.7}
$$



For a digit $r\in\{0,1\}$, with lookahead $d$, put


$$
H'=\Phi_r(H)
$$


using the signed representatives in (3.2), and


$$
D_{r,d}(H)
=\frac{\mathcal T_{r,d}(\iota(H))-\iota(H')}3\pmod3.
\tag{3.8}
$$


Then


$$
\boxed{
\begin{aligned}
C_X'&=\overline{\mathcal T}_r(C_X)-D_{r,d}(H),\\
C_Y'&=\overline{\mathcal T}_r(C_Y)+D_{r,d}(H).
\end{aligned}
}
\tag{3.9}
$$



In particular, the carry sum has no injected term:


$$
\boxed{
C_X'+C_Y'
=\overline{\mathcal T}_r(C_X+C_Y).
}
\tag{3.10}
$$



The two carries themselves must still be retained: their difference contains information not recoverable from their sum.

### 3.3 The paid first-$2$ transition

If $H=sR$ or $sP$, $s\in\{1,-1\}$, the turn15 injections give


$$
J_{R,d}=b^2,\qquad J_{P,d}=b(1+da).
$$


Immediately after the first $2$,


$$
N_X=3Z_X,\qquad N_Y=3Z_Y\pmod9,
$$


where


$$
\boxed{
\begin{aligned}
Z_X&=\overline{\mathcal T}_2(C_X)-s\,\iota(J_{H/s,d}),\\
Z_Y&=\overline{\mathcal T}_2(C_Y)+s\,\iota(J_{H/s,d}).
\end{aligned}
}
\tag{3.11}
$$



Both the inherited terms and the new injections occur in this formula. The theorem below will annihilate their **sum**, rather than assuming either part absent.

---

## 4. The explicit terminal quotient after twenty-five leading ones

The divided-carry terminal functional can be evaluated symbolically on the whole seventeen-coordinate space.

### Theorem 4.1 — Leading-ones functional on the divided module

Let


$$
Z(u)=\sum_{i=0}^{16}z_i u^i\in\mathbb F_3[u]_{\le16}.
$$


After processing twenty-five leading digits $1$, the terminal value is


$$
\boxed{
\ell_{25}(Z)=z_{10}+z_{13}-z_9-z_{12}.
}
\tag{4.1}
$$



#### Proof

The two-digit return calculation from turn15 can be written explicitly. Starting with $Z/Q^8$, after a first digit $r$ put


$$
L=C_r(Zb^r).
$$


After a second digit $s$, the seven-coordinate numerator is


$$
H=a^{2-s}C_s\!\left(L a^{2-r}b^{2+s}\right).
\tag{4.2}
$$



For $r=s=1$,


$$
H=aC_1(La b^3)=ab\,C_1(La)=Q\,C_1(La),
\qquad L=C_1(bZ).
$$


Since $\deg L\le5$,


$$
C_1(La)=U+Vu,
$$


where


$$
U=z_1+z_4-z_0-z_3,\qquad
V=z_{10}+z_{13}-z_9-z_{12}.
\tag{4.3}
$$



For every $U,V\in\mathbb F_3$, formula (2.2) gives


$$
\Phi_1\bigl(Q(U+Vu)\bigr)=Q(V+Uu).
\tag{4.4}
$$


The remaining twenty-three $1$'s therefore interchange $U,V$ an odd number of times. The final constant coefficient is $V$, proving (4.1). ∎

As a consistency identity, not as a new finite test,


$$
\boxed{
\ell_{25}(\iota(H))=h_1-h_5
}
\tag{4.5}
$$


for $H=\sum_{i=0}^6h_i u^i$. Thus the new functional agrees with the retained seven-coordinate leading functional.

### 4.1 The target quotient

Suppose the middle word has already sent the actual pair to


$$
(3Z_X,3Z_Y)\pmod9
$$


immediately before the leading $1^{25}$. Then


$$
\boxed{
\left(\frac{X_m}{3},\frac{Y_m}{3}\right)
\equiv
\bigl(\ell_{25}(Z_X),\ell_{25}(Z_Y)\bigr)\pmod3.
}
\tag{4.6}
$$



Consequently the terminal observable quotient is explicitly


$$
\boxed{
\frac{\bigl(\mathbb F_3[u]_{\le16}\bigr)^2}
{\ker(\ell_{25})\times\ker(\ell_{25})}
\cong\mathbb F_3^2.
}
\tag{4.7}
$$



This is a two-coordinate target quotient, not a claim that all its elements are reachable from the actual suffix.

If $V$ is the remaining low-to-high middle word after the first $2$, let $\overline{\mathcal T}_V$ denote its chronological transition product. Combining (3.11) and (4.6) gives the actual inherited-carry observable:


$$
\boxed{
\begin{aligned}
X_m/3&\equiv
\ell_{25}\overline{\mathcal T}_V
\left(\overline{\mathcal T}_2(C_X)-s\iota(J_{H/s,d})\right),\\
Y_m/3&\equiv
\ell_{25}\overline{\mathcal T}_V
\left(\overline{\mathcal T}_2(C_Y)+s\iota(J_{H/s,d})\right)
\pmod3.
\end{aligned}
}
\tag{4.8}
$$



For completeness, the original modulo-$9$ leading operator is


$$
\mathcal T_{1,0}\mathcal T_{1,1}^{24}.
$$


The final lookahead is therefore $0$, as required. Its lookahead corrections disappear in (4.6) because the input has already been proved divisible by $3$, not because they were discarded in advance.

If the pair in (4.6) is nonzero, then $c_m=1$, and it is the actual primitive endpoint pair modulo $3$. If it is zero, the conclusion is only $c_m\ge2$.

---

## 5. A universal divided-carry annihilator

The following is the higher-layer statement that removes the need to evaluate the inherited carry for a useful cylinder.

### Lemma 5.1 — A three-digit annihilator in seven coordinates

For every $H\in\mathbb F_3[u]_{\le6}$,


$$
\boxed{
\Phi_2\Phi_0\Phi_2(H)=0.
}
\tag{5.1}
$$



#### Proof

Write


$$
\Phi_2(H)=bK,\qquad \deg K\le2.
$$


If $K=k_0+k_1u+k_2u^2$, then


$$
\Phi_0(bK)
=ba^2C_0(QK)
=P(k_0-k_1u).
$$


Finally,


$$
\Phi_2\bigl(P(k_0-k_1u)\bigr)
=
b\,C_2\bigl(a^3b^3(k_0-k_1u)\bigr)=0,
$$


because $a^3b^3$ is a polynomial in $u^3$, and the remaining factor has degree at most one. ∎

For arbitrary divided carries, one can do better than merely prepend two unspecified return digits.

### Theorem 5.2 — Universal four-digit annihilator on seventeen coordinates

For every $Z\in\mathbb F_3[u]_{\le16}$,


$$
\boxed{
\overline{\mathcal T}_2
\overline{\mathcal T}_0
\overline{\mathcal T}_2
\overline{\mathcal T}_0(Z)=0.
}
\tag{5.2}
$$



Thus the low-to-high word $0,2,0,2$ kills every divided carry in the entire seventeen-coordinate space.

#### Proof

Apply the explicit two-digit return formula (4.2) with $r=0,s=2$. Put


$$
L=C_0(Z),\qquad \deg L\le5.
$$


The resulting seven-coordinate numerator is


$$
H=C_2(La^2b^4)
=b\,C_2(La^2b)
=bK,
\qquad \deg K\le2.
\tag{5.3}
$$



The next digit $0$ gives $P(k_0-k_1u)$, and the last digit $2$ kills that polynomial, exactly as in Lemma 5.1. Hence the final seventeen-coordinate numerator is zero. ∎

This is an identity on all $3^{17}$ possible divided states, proved without enumerating them.

---

## 6. The actual modulo-$9$ killing word

### Theorem 6.1 — Both endpoints are killed by the middle word $20202$

Let


$$
m=(1^{25}M01011112)_3.
$$


If $M$ contains the consecutive high-to-low word $20202$, then


$$
\boxed{
X_m\equiv Y_m\equiv0\pmod9.
}
\tag{6.1}
$$



#### Proof

The word $20202$ is palindromic, so it is read as


$$
2,0,2,0,2
$$


also in the low-to-high processing order.

By (3.4) and (3.2), before this occurrence the characteristic-three endpoint states are either opposite signed copies of $R$ or $P$, or both zero.

The first digit $2$ therefore makes both actual modulo-$9$ states divisible by $3$. Their quotients include all inherited carry and the paid injection described in (3.11).

Once a state is $3Z\pmod9$,


$$
\frac{\mathcal T_{r,d}(3Z)}3
=\overline{\mathcal T}_r(Z)\pmod3.
\tag{6.2}
$$


The remaining digits are $0,2,0,2$. Theorem 5.2 kills **every** possible $Z$, separately for each endpoint.

Thus both actual states are zero modulo $9$ after the word. All subsequent transitions, including the complete leading block, preserve zero. ∎

Several scope points are important.

* The theorem does not assume a favorable inherited direction.
* It does not use cancellation between the two endpoints.
* It does not replace the inherited carry by the first-$2$ injection.
* It does not require a modulo-$9$ suffix table.
* It proves a sufficient condition for $c_m\ge2$, not an exact valuation and not a primitive direction at depth two.

---

## 7. Original-domain realization and density

The new killing word can be realized as a **fixed trailing extension**, for which a realizability theorem is available. No assertion about arbitrary unlocated middle words is needed.

### 7.1 An explicit compatible congruence

Since


$$
(20202)_3=182,
$$


placing this word immediately above the eight-digit suffix gives


$$
m\equiv851+3^8\cdot182\pmod{3^{13}}.
$$


That is,


$$
\boxed{
m\equiv1194953\pmod{1594323}.
}
\tag{7.1}
$$



The residue is $2\pmod3$, and it retains $m\equiv851\pmod{6561}$.

The group $1+3\mathbb Z/3^{13}\mathbb Z$ is cyclic of order $3^{12}$, generated by $4$. Hence there is a unique


$$
j_*\pmod{3^{12}}
$$


such that


$$
4^{j_*}\equiv2\cdot1194953
\equiv795583\pmod{1594323}.
\tag{7.2}
$$



This progression is compatible with the original congruence. Indeed,


$$
2\cdot1194953\equiv244\pmod{729},
$$


and


$$
4^{81}\equiv244\pmod{729}.
$$


Because $4$ has order $243$ modulo $729$, (7.2) implies


$$
\boxed{j_*\equiv81\pmod{243}.}
\tag{7.3}
$$



Thus (7.1) is not an arbitrary formal cylinder: it is realized by infinitely many positive original indices


$$
j\equiv j_*\pmod{531441}.
\tag{7.4}
$$



### 7.2 Independent check of the exact window squeeze

Put


$$
\alpha=\log_3 4,\qquad
a_0=\frac1{2C_{16}},\qquad b_0=\frac1{C_{16}}.
$$


For an index satisfying the window, set $k=h-1$. For all sufficiently large such indices,


$$
k=\lceil j\alpha\rceil.
$$


In fact, $D>0$ gives $4^j<3^k$, while the lower bound on $A_{\mathrm{ind}}/3^k$ gives $4^j>3^{k-1}$.

With $\theta=\{j\alpha\}$,


$$
\frac D{3^k}=1-3^{\theta-1}+3^{-k}.
\tag{7.5}
$$


The exact window therefore corresponds, for sufficiently large $k$, to


$$
1+\log_3(1-b_0+3^{-k})
<
\theta
<
1+\log_3(1-a_0+3^{-k}).
\tag{7.6}
$$



The $3^{-k}$ term has not been dropped. These endpoints tend to those of


$$
I=
\left(
1+\log_3(1-b_0),\
1+\log_3(1-a_0)
\right).
$$


Fixed inner and outer intervals squeeze (7.6). Since $\alpha$ is irrational, equidistribution on every fixed arithmetic progression gives relative density


$$
\boxed{
\delta=\log_3\frac{1-a_0}{1-b_0}>0.
}
\tag{7.7}
$$



In particular, the progression (7.4) has real-window density


$$
\boxed{\delta/531441}
\tag{7.8}
$$


among all positive $j$.

### 7.3 Independent check of the prefix constant

The numerical comparison needed for the prefix is exactly


$$
147968>3^{10}=59049.
$$


Therefore


$$
C_{16}>3^{25},\qquad b_0<3^{-25}.
$$



Writing $\varepsilon=D/3^k$,


$$
\frac m{3^k}=\frac{1-\varepsilon+3^{-k}}2.
$$


For sufficiently large $k$, $3^{-k}<a_0<\varepsilon$, so


$$
\frac{1-3^{-25}}2
<
\frac m{3^k}
<
\frac12.
\tag{7.9}
$$


The ternary cylinder with first twenty-five digits $1$ is


$$
\left[
\frac{1-3^{-25}}2,\,
\frac{1+3^{-25}}2
\right).
$$


Thus (7.9) lies strictly inside that cylinder. For sufficiently large indices, the prefix and the fixed thirteen-digit tail are disjoint.

### Theorem 7.1 — Positive-density original family with $c_m\ge2$

On the nonempty progression (7.4), every sufficiently large exact-window index satisfies


$$
\boxed{c_m\ge2.}
\tag{7.10}
$$



#### Proof

The exact window supplies the leading $1^{25}$. Congruence (7.1) supplies the trailing word


$$
20202\,01011112.
$$


Theorem 6.1 applies, and (7.8) proves positive density. ∎

### 7.4 Compatibility with other fixed-depth conditions

The same construction works inside any nonempty compatible fixed-depth original progression.

Choose a depth $s$ large enough to retain all its prescribed trailing digits and the original suffix. If $r_s$ is its fixed residue modulo $3^s$, impose


$$
m\equiv r_s+3^s\cdot182\pmod{3^{s+5}}.
\tag{7.11}
$$


The new word lies above the prescribed lower digits. The cyclic-group parametrization gives a compatible refinement of the original progression, and irrational rotation supplies a positive-density exact-window subset.

If an exact resonance valuation is prescribed, retain the additional digit that certifies exactness before appending the word.

This is a fixed-depth theorem. It does not supply uniform density estimates for a resonance depth increasing with $j$, nor does it automatically preserve every quantitative controlled-growth condition from turn1.

### 7.5 What Lagarias does and does not add

The retained Lagarias Theorem 1.1, with $\lambda=3^{-8}$, still proves that the middle-digit-$2$-omitting exceptions have sublinear count. Combined with the exact squeeze above, it gives the earlier relative-density-one conclusion $c_m\ge1$ in every compatible fixed progression.

The new $c_m\ge2$ theorem requires no new digit-occurrence estimate because its word is forced at a fixed trailing location.

However, the supplied Lagarias theorem does **not** bound the number of powers whose middle word avoids $20202$. Avoiding that word is not the same as omitting digit $2$. Therefore:



$$
\boxed{
\text{Positive-density }c_m\ge2\text{ is proved; relative-density-one }c_m\ge2
\text{ in every window class is not.}
}
$$



No general sublinear theorem for arbitrary finite-automaton languages is being asserted.

---

## 8. The exact Jacobi normalization bridge

The uncertainty stated in turn15 about an absent Jacobi normalization bridge should be removed. The attached turn1 source provides the required normalization.

For fixed $A$, write


$$
J_s^{[A]}(y)=
\sum_{k=0}^s
\binom{s+A}{k}
\binom{s-\tfrac12}{s-k}
y^k(y-1)^{s-k}.
\tag{8.1}
$$



### Theorem 8.1 — Common characteristic-zero endpoint identity

For every integer $m\ge1$,


$$
\boxed{
X_m=J_m^{[\,2m-1\,]}(-1),\qquad
Y_m=J_{m-1}^{[\,2m-1\,]}(-1).
}
\tag{8.2}
$$



#### Proof

The exact differentials in turn15 give


$$
X_m=[u^m]\,b^{m-\frac12}a^{\frac12-3m},
\tag{8.3}
$$




$$
Y_m=[u^{m-1}]\,b^{m-\frac32}a^{\frac32-3m}.
\tag{8.4}
$$



In the corresponding residues make the formal change of variable


$$
u=-\frac z{1+z}.
$$


Then


$$
a=\frac1{1+z},\qquad
b=\frac{1+2z}{1+z},\qquad
\frac{du}{u}=\frac{dz}{z(1+z)}.
$$



Equation (8.3) becomes


$$
X_m=(-1)^m[z^m]
(1+z)^{3m-1}(1+2z)^{m-\frac12}.
\tag{8.5}
$$


Similarly,


$$
Y_m=(-1)^{m-1}[z^{m-1}]
(1+z)^{3m-2}(1+2z)^{m-\frac32}.
\tag{8.6}
$$



At $y=-1$, (8.1) reads


$$
J_s^{[A]}(-1)
=(-1)^s[z^s](1+z)^{s+A}(1+2z)^{s-\frac12}.
\tag{8.7}
$$


Taking $(s,A)=(m,2m-1)$ and $(m-1,2m-1)$ proves both identities. ∎

The adjacent Bernstein expansion is therefore exactly


$$
\boxed{
J_{m-1}^{[\,2m-1\,]}(y)
=
\sum_{k=0}^{m-1}
\binom{3m-2}{k}
\binom{m-\tfrac32}{m-1-k}
y^k(y-1)^{m-1-k}.
}
\tag{8.8}
$$



On the original family $m$ is even. Hence the sign in (8.5) is $+1$, while the sign in (8.6) is $-1$. Both signs are already included in the common identities; no sign adjustment or unit scalar remains to be supplied.

This identifies the endpoint normalization. It does **not** identify


$$
c_m
\quad\text{with}\quad
\operatorname{cont}_3(J_m^{[A]})
\quad\text{or}\quad
\operatorname{cont}_3(J_{m-1}^{[A]}).
$$



---

## 9. Exact induced Christoffel projective map

Use the old source’s monic recurrence


$$
p_{m+1}(y)=(y-\beta_m)p_m(y)-\gamma_m p_{m-1}(y),
$$


where, writing $A=A_{\mathrm{ind}}$,


$$
\beta_m=
\frac{3(2A^2+4A+1)}{(4A+1)(4A+5)},
\tag{9.1}
$$




$$
\gamma_m=
\frac{3A^2(A+1)(3A+1)}
{(4A+1)^2(4A-1)(4A+3)}.
\tag{9.2}
$$



The actual integral-column coefficient is


$$
\boxed{
\rho_m=
\gamma_m\frac{\kappa_m}{\kappa_{m-1}}
=
\frac{A(3A+1)}{(4A+1)(4A+3)}.
}
\tag{9.3}
$$



Let


$$
\eta=A+71,\qquad
\chi_m=\frac{p_{m+1}(\eta/3)}{p_m(\eta/3)}
$$


where the scalar is defined, and retain the source polynomial


$$
(3y-\eta)Z_{\rm src}(y)
=
(y-\beta_m-\chi_m)J_m^{[A]}(y)
-\rho_mJ_{m-1}^{[A]}(y).
\tag{9.4}
$$



Evaluating at $-1$, with all signs retained, gives


$$
\boxed{
Z_{\rm src}(-1)
=
\frac{(1+\beta_m+\chi_m)X_m+\rho_mY_m}{A+74}.
}
\tag{9.5}
$$



Therefore the exact projective map is


$$
\boxed{
[X_m:Y_m]\longmapsto
[(A+74)X_m:
(1+\beta_m+\chi_m)X_m+\rho_mY_m].
}
\tag{9.6}
$$



Its determinant is $(A+74)\rho_m$, up to the displayed common projective scaling. On the original domain,


$$
v_3(A)=5,\qquad v_3(\rho_m)=4,\qquad A+74\in\mathbb Z_3^\times.
$$


Thus the map is invertible over $\mathbb Q_3$, but is not an integral unimodular change of endpoint coordinates.

### 9.1 A useful content consequence on the integral scalar branch

Suppose $\chi_m\in3\mathbb Z_3$, as on the retained scalar branch. Put


$$
\lambda_m=\frac{1+\beta_m+\chi_m}{A+74},\qquad
\mu_m=\frac{\rho_m}{A+74}.
$$


Then


$$
\lambda_m\in\mathbb Z_3^\times,\qquad v_3(\mu_m)=4,
\qquad \lambda_m\equiv-1\pmod3.
$$



Writing


$$
X_m=3^{c_m}\bar X,\qquad Y_m=3^{c_m}\bar Y
$$


with primitive $(\bar X,\bar Y)$, invariance of the generated ideal under subtracting $\lambda_m\bar X$ gives


$$
\begin{aligned}
\min\{v_3(X_m),v_3(Z_{\rm src}(-1))\}
&=c_m+\min\{v_3(\bar X),4+v_3(\bar Y)\}\\
&=\boxed{c_m+\min\{v_3(\bar X),4\}.}
\end{aligned}
\tag{9.7}
$$



This is an endpoint-pair content law, not a polynomial-content theorem. Recovering $\bar Y$ from the transformed pair requires paying the four-digit division by $\mu_m$.

### 9.2 Hypotheses that remain separate

The new endpoint identity does not establish, on the density-selected family,

* $\mathfrak a=\chi_m/3\equiv25\pmod{27}$;
* equality of the two full polynomial contents;
* the normalized inverse-loss hypotheses used in turn8;
* proximity to, or avoidance of, the exceptional scalar root lines;
* preservation under the complete actual force.

The norm-unit assertion itself should not be listed as wholly missing: turn1 gives an explicit formula proving $N_m\in\mathbb Z_3^\times$ on its stated original branch. But that fact does not supply the other scalar and polynomial-content hypotheses.

The corrected turn8 factorial residue remains


$$
\frac{K_c-K_J}{3^{h-2s+2g-2}}
\equiv2L^2\zeta^2J(-1)^2\pmod3,
$$


under its stated normalized-branch hypotheses. The coefficient-free executive version in that source is not the final formula.

---

## 10. Consequences and limits of the new endpoint theorem

The actual observation law from A4 remains


$$
c(V_{m-1})-c_m
=
4+\min\{2,v_3(\bar Y-3\bar X)\}.
\tag{10.1}
$$



On the new family,


$$
c_m\ge2,
$$


so one may conclude


$$
\boxed{c(V_{m-1})\ge6.}
\tag{10.2}
$$



One may not yet conclude:

* that $c_m=2$;
* a primitive endpoint direction modulo $3$;
* loss $4$, $5$, or $6$ in (10.1);
* a scalar-root separation bound;
* a value of the actual primitive denominator.

For the new killing family, a primitive endpoint direction at content exactly two requires endpoints modulo $27$. If the endpoint content is larger, the precision bill increases accordingly. The retained general bills


$$
3^{r+K}\quad\text{for endpoints},\qquad
3^{r+K+6}\quad\text{for the observed state}
$$


are not reduced by a modulo-$9$ zero.

---

## 11. The complete finite producers remain unchanged

The local endpoint theorem does not alter the finite construction.

Retain


$$
0\le v\le2n-2,
$$




$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
\qquad
d=\frac{3D}{2}-1,\quad \nu=\frac D2-1.
$$



Both corrected columns remain


$$
\widehat Z^{\,\mathrm{act}}
=\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$


with the full Schur correction


$$
S_{\mathrm{act}}-S_c
=
3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R.
$$


Also retain


$$
Q_{\mathrm{act}}=Q_c+3^6R_{\mathrm{prod}},
\qquad
R_{\mathrm{prod}}=R_{25}+3^{25}\Delta_{25}.
$$



The complete force includes the full pole pair, both leading extractions, every permitted lower pole, factorial forcing, LOW subtraction, all correction layers and the unpaired finite-boundary terms. In the old matrix notation, the actual perturbation is still the complete finite expression


$$
\begin{aligned}
\Delta_{ad}
={}&-\frac{3^h}{4}\mathfrak f(Q_{\mathrm{act}}y^{a+d})\\
&+3^{h+6}
\sum_{2v+1\le4n-3}
\frac{
[y^v]\bigl(R_{\mathrm{prod}}y^{a+d}
-(-1)^{a+d}R_{\mathrm{prod}}(-1)\bigr)/(y+1)
}{2v+1},
\end{aligned}
$$


for $0\le a,d\le m$.

The terminal return remains


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


There is no extra moment beyond $D-4$, and $\omega_{\nu-1}$ remains.

The old rank-one perturbation example continues to show why entrywise precision modulo $3^6$ alone cannot determine the actual endpoint response in the large-loss regime. The new digit theorem does not repair that structured-force obstruction.

After all actual row contents, the actual multiplier and the least actual clearer, retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole same-index error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{11.1}
$$



The weighted producer likewise retains


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


and


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{11.2}
$$



Neither final gcd, actual $q$, nor whole evaluated error is determined by the local modulo-$9$ result.

---

## 12. Proof status, bounded arithmetic, and next bottleneck

### 12.1 Status ledger

| Statement | Status |
|---|---|
| Seventeen-coordinate modulo-$9$ transition and degree bound | Reused from turn15 |
| Actual characteristic-three suffix pair $(-\iota R,\iota R)$ | Proved symbolically here |
| Exact inherited-carry recurrence with lookahead | Explicitly derived here |
| Divided leading-$25$-ones functional $z_{10}+z_{13}-z_9-z_{12}$ | Proved here |
| Universal seventeen-coordinate divided-carry annihilator $0202$, low to high | Proved here |
| Actual endpoint modulo-$9$ killing word $20202$ | Proved here |
| Original positive-density family with $c_m\ge2$ | Proved here by fixed-tail realization and exact-window equidistribution |
| Relative-density-one $c_m\ge2$ in every original window class | Not proved |
| Exact Jacobi identities for both endpoints, with no scalar | Proved here |
| Exact $Z_{\rm src}(-1)$ projective map | Derived from the actual source normalization |
| Equality of endpoint and full polynomial contents | Not asserted |
| Primitive direction on the new killing family | Open; modulo $27$ or more is needed |
| Actual-force transfer, final all-prime gcd and whole-error comparison | Open |

### 12.2 What bounded arithmetic is actually needed

No further computation is needed for the symbolic theorems above. The coordinator’s announced new modulo-$9$ checks remain independent corroboration when received; their outcome has not been anticipated.

If a numerical representative of the new original progression is desired, the only additional bounded arithmetic is the small discrete-log lifting problem:

**Inputs**


$$
M_0=1594323=3^{13},\qquad
u_0=795583.
$$



**Expected verifiable output**

An integer $j_*$ with


$$
0\le j_*<531441,
$$


together with the directly checkable congruences


$$
4^{j_*}\equiv795583\pmod{1594323},
\qquad
j_*\equiv81\pmod{243}.
$$



Existence and uniqueness in this range are already proved by the cyclic-group argument. An evaluated numerical representative is not used as a premise.

### 12.3 Concrete next lemma

The modulo-$9$ cylinder now supplies divisibility, not a primitive direction. A concrete higher-precision continuation is:

> **Divided killing-cylinder lemma.**  
> On the actual suffix cylinder containing $20202$, determine the image of
> 

$$
> \left(X_m/9,\;Y_m/9\right)\pmod3
>
$$


> using a paid modulo-$27$ lift, retaining the actual suffix carry and the same leading functional. Prove either a nonzero direction on a compatible original progression or a further universal cancellation identity.

Separately, the scalar comparison requires the already identified structured-residual endpoint lemma for the complete finite force. Even a successful modulo-$27$ endpoint classification would not by itself prove that transfer.

---

## Conclusion

The new higher-layer result is not merely another transition-existence statement. It is an explicit annihilation theorem:



$$
\boxed{
\overline{\mathcal T}_2
\overline{\mathcal T}_0
\overline{\mathcal T}_2
\overline{\mathcal T}_0=0
\quad\text{on }\mathbb F_3[u]_{\le16},
}
$$


which yields


$$
\boxed{
20202\subset M
\quad\Longrightarrow\quad
X_m\equiv Y_m\equiv0\pmod9.
}
$$



The inherited carry is included and annihilated. The condition is realized on an explicit compatible fixed-tail progression, giving an unconditional original positive-density family with $c_m\ge2$.

The old normalization bridge is also now exact:


$$
\boxed{
X_m=J_m^{[\,2m-1\,]}(-1),\qquad
Y_m=J_{m-1}^{[\,2m-1\,]}(-1),
}
$$


with no scalar, and with the actual induced Christoffel projective map displayed in (9.6).

The remaining local arithmetic bottleneck is primitive-direction control beyond the newly forced two endpoint digits, followed by the separately required polynomial-content and scalar hypotheses. The global bottleneck remains control of the **actual all-prime primitive denominator against the whole nonzero same-index error** on an infinite original sequence.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


