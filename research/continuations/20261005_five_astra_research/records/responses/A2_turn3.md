> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Matched $b=4$: full exclusion; matched $b=5$: new contiguous content and a root-safe normalization

The supplied four-prime certificate is sufficient to exclude **the entire eventual matched-$b=4$ family**, not just a positive-density subset. The missing infinite implication is supplied below.

For the distinct matched-$b=5$ family, I obtain a stronger normalization than merely reusing $2n+5$. In the raw-row convention of the supplied sources, all three contractions have the universal factor


$$
\boxed{1152(n+3)(2n+5)(2n+7).}
$$


There is an explicit integral replacement basis, valid even where one of these factors vanishes modulo a prime. Its normalized contractions have all-depth transfer at every $p\ge5$.

These are exclusions and arithmetic reductions for particular approximation families. They do **not** decide whether $e+\pi$ is irrational.

Throughout, the nonalternating partial-factorial sum used below is denoted $\mathscr D_j$. It is distinct from the derangement sequence in A1’s moment argument; there is no counterexample to that moment bound here.

---

## 1. The exact contact families and common notation

For $b=4$ or $5$, the family is


$$
R_n(z)=A_n(z)+B_n(z)e^z+C_n(z)F(z),
\qquad
F(z)=4\arctan\frac{z}{2-z},
$$


with


$$
\deg A_n,\deg C_n\le n,\qquad \deg B_n\le b,
$$




$$
R_n(z)=O(z^{2n+b+1}),\qquad B_n(1)=C_n(1)=Y_n.
$$


Thus:

* $b=4$: caps $(n,4,n)$, contact $2n+5$, actual domain $n\ge4$;
* $b=5$: caps $(n,5,n)$, contact $2n+6$, actual domain $n\ge5$.

Write $X_n=A_n(1)$. Where $Y_n\ne0$, define the actual rational center by


$$
c_n=-\frac{X_n}{Y_n}=\frac{p_n}{q_n},
\qquad q_n>0,\qquad \gcd(p_n,q_n)=1.
$$


Since $F(1)=\pi$,


$$
\boxed{\frac{R_n(1)}{Y_n}=e+\pi-c_n.}
\tag{1.1}
$$


This is the whole evaluated remainder.

Put


$$
H_j(x)=j![z^j]e^{xz}\left(1-z+\frac{z^2}{2}\right)^j,
\qquad
\mathscr F_j(x)=x^jH_j(x),
\qquad
E_{j,r}=\mathscr F_j^{(r)}(1).
$$


The integer contractions are


$$
\mathcal A_n=I(\mathscr F_n),\qquad
\mathcal M_n=I(x\mathscr F_n),\qquad
\mathcal B_n=\mathcal M_n+H_n(1)-H_n'(1),
$$


where


$$
I(P)=\int_1^\infty e^{1-x}P(x)\,dx.
$$



Scalar indices $0\le n<b$ will be used only as congruence seeds, never as admissible approximants.

---

# Part I. Completion of the matched-$b=4$ theorem

## 2. A short independent derivation of the contiguous identity

The following derivation also provides the new $b=5$ factors.

The supplied monic reference polynomials satisfy


$$
p_{j+1}(y)=\left(y-\frac12\right)p_j(y)
+\frac{j^2}{4(4j^2-1)}p_{j-1}(y).
\tag{2.1}
$$


Their Rodrigues transform is


$$
\sum_m [y^m]p_j(y)\frac{x^{j+m}}{(j+m)!}
=\frac{\mathscr F_j(x)}{(2j)!}.
\tag{2.2}
$$



Let $\mathcal I$ denote integration from zero. Applying (2.2) to (2.1) gives


$$
\frac{\mathscr F_{j+1}}{(2j+2)!}
=
\mathcal I^2\frac{\mathscr F_j}{(2j)!}
-\frac12\mathcal I\frac{\mathscr F_j}{(2j)!}
+\frac{j^2}{4(4j^2-1)}
 \mathcal I^2\frac{\mathscr F_{j-1}}{(2j-2)!}.
$$


Differentiating twice and simplifying the factorial coefficients proves


$$
\boxed{
\frac{\mathscr F_{j+1}''}{j+1}
=(2j+1)(2\mathscr F_j-\mathscr F_j')
+j^3\mathscr F_{j-1}.
}
\tag{2.3}
$$



Set


$$
k=n+1,\qquad F=\mathscr F_k,\qquad G=\mathscr F_{k+1},
\qquad z=\frac{G'}{k+1}.
$$


Then (2.3), at $j=k+1$, becomes


$$
\boxed{
\frac{\mathscr F_{k+2}''}{k+2}
=(k+1)^3F+(2k+3)w,
\qquad
w=2G-(k+1)z.
}
\tag{2.4}
$$



This is exactly the previous replacement row. Indeed, with the operators $T_k,B_k,C_k$ specified in the prior source,


$$
G=T_kF,\qquad z=B_kF,
$$


and direct coefficient comparison gives


$$
\boxed{C_k=2T_k-(k+1)B_k.}
\tag{2.5}
$$


Thus $w=C_kF$. In particular, (2.4) independently identifies the same normalization used by the supplied $46$-row certificate.

The functions $F,G,z,w$ are integer polynomials. For $z$, either use the proved coefficient divisibility $G'/(k+1)\in\mathbb Z[x]$, or the division-free expression $z=B_kF$.

---

## 3. The precise $b=4$ normalization and its transfer

For a polynomial $P$, define the length-five row


$$
J_4(P)=
\left(
P(1),\,
[t^0](P'-P)(1+t),\ldots,
[t^3](P'-P)(1+t)
\right).
$$


Define


$$
\mathcal E=(1,0,0,0,0),
$$




$$
\mathcal P=
\left(0,[t^0]\mathscr F_n(1+t),\ldots,[t^3]\mathscr F_n(1+t)\right),
$$




$$
\mathcal U=
\left(0,[t^0]\frac{F'(1+t)}k,\ldots,
[t^3]\frac{F'(1+t)}k\right).
$$



The normalization used in the certificate is


$$
\begin{aligned}
\widehat\sigma_n
&=-\det[J_4(F);J_4(z);J_4(w);\mathcal E;\mathcal U],\\
\widehat\chi_n
&=-\det[J_4(F);J_4(z);J_4(w);\mathcal E;\mathcal P],\\
\widehat\kappa_n
&=\det[J_4(F);J_4(z);J_4(w);\mathcal U;\mathcal P],
\end{aligned}
\tag{3.1}
$$


and


$$
\widehat V_n
=\widehat\sigma_n\mathcal A_n
-\widehat\chi_n\mathcal B_n-\widehat\kappa_n.
\tag{3.2}
$$



If $(\sigma_n,\chi_n,\kappa_n)$ are the raw contractions from the three high rows


$$
(E_{n+1,j})_{j=0}^4,\quad
\left(\frac{E_{n+2,j+1}}{n+2}\right)_{j=0}^4,\quad
\left(\frac{E_{n+3,j+2}}{n+3}\right)_{j=0}^4,
$$


then


$$
\boxed{
(\sigma_n,\chi_n,\kappa_n)
=12(2n+5)(\widehat\sigma_n,\widehat\chi_n,\widehat\kappa_n).
}
\tag{3.3}
$$



The factor $2n+5$ follows from (2.4). After subtracting each original column from its successor, the last four columns have entries divisible by


$$
0!,1!,2!,3!,
$$


respectively. Their product is $12$, and division gives precisely (3.1). These are integral divisions before reduction.

### 3.1 Why normalized transfer holds at all four selected primes

Here are the necessary ingredients, including the support issue.

Let


$$
a_s(n)=[z^s]\left(1-z+\frac{z^2}{2}\right)^n.
$$


For odd $p$, if $m\equiv n\pmod{p^a}$, the binomial expansion gives


$$
v_p(a_s(m)-a_s(n))
\ge a-\lfloor\log_p s\rfloor\qquad(s\ge1).
\tag{3.4}
$$


Also


$$
v_p((x)_s)\ge v_p(s!)\ge\lfloor\log_p s\rfloor
\tag{3.5}
$$


for integral $x$.

Consequently the sums


$$
H_n^{(d)}(1)=\sum_{s\ge0}(n)_{s+d}a_s(n)
$$


transfer modulo $p^a$, in particular for $d=0,1,2$.

For the integral contractions, use


$$
\mathscr D(x)=\sum_{r\ge0}(x)_r,\qquad x\in\mathbb Z_p.
$$


This converges uniformly, since $v_p((x)_r)\ge v_p(r!)\to\infty$, and is $1$-Lipschitz. For nonnegative integers $j$,


$$
\mathscr D(j)=j!\sum_{r=0}^j\frac1{r!}.
$$


The common-index formulas are


$$
\mathcal A_n
=\sum_{s\ge0}(n)_sa_s(n)\mathscr D(2n-s),
$$




$$
\mathcal M_n
=\sum_{s\ge0}(n)_sa_s(n)\mathscr D(2n+1-s).
\tag{3.6}
$$


Terms beyond the original finite support vanish through $(n)_s$. Thus negative arguments introduced when comparing unequal supports are legitimate $p$-adic arguments, not undefined factorial expressions. Equations (3.4)–(3.6) prove all-depth transfer of


$$
n,\ H_n(1),\ H_n'(1),\ H_n''(1),\ \mathcal A_n,\ \mathcal M_n.
$$



Finally, the finite derivative recurrences and the division-free formula for $F'/k$ express every entry in (3.1) polynomially in these coordinates, with coefficient denominators involving only $2$ and $3$. Hence, for every $p\ge5$,


$$
\boxed{
m\equiv n\pmod{p^a}
\ \Longrightarrow\
(\widehat\sigma,\widehat\chi,\widehat\kappa,\widehat V)_m
\equiv
(\widehat\sigma,\widehat\chi,\widehat\kappa,\widehat V)_n
\pmod{p^a}.
}
\tag{3.7}
$$



There is no division by $2n+5$ in this transfer argument. In particular it remains valid on its modular root.

---

## 4. The finite certificate now has an all-index consequence

For


$$
\mathcal P_4=\{5,11,13,17\},
$$


the supplied independently reconstructed normalized $V$-vectors are


$$
\begin{array}{c|l}
p&(\widehat V_0,\ldots,\widehat V_{p-1})\pmod p\\ \hline
5&(2,2,2,2,2)\\
11&(5,7,2,7,8,9,6,8,2,1,7)\\
13&(10,12,11,2,2,1,5,9,6,12,6,6,7)\\
17&(5,12,9,4,5,4,3,10,11,12,9,4,7,13,1,3,14).
\end{array}
\tag{4.1}
$$


Every entry is nonzero.

These are the $46$ supplied finite checks; I do not claim a new execution. The infinite step is (3.7), which proves


$$
\boxed{v_p(\widehat V_n)=0
\quad(n\ge0,\ p\in\mathcal P_4).}
\tag{4.2}
$$



This includes the removed-factor roots:


$$
(p,n)=(5,0),(11,3),(13,4),(17,6).
$$


Their normalized $V$-values are respectively $2,7,2,3$, all nonzero.

### 4.1 Removal of all remaining contraction content

Set


$$
d_n=\gcd(|\widehat\sigma_n|,|\widehat\chi_n|,
                         |\widehat\kappa_n|).
$$


The triple is nonzero at every scalar index, by (4.2). Since $d_n\mid\widehat V_n$,


$$
v_p(d_n)=0\qquad(p\in\mathcal P_4).
\tag{4.3}
$$


Define the actual primitive contraction triple


$$
(\sigma_n^*,\chi_n^*,\kappa_n^*)
=\frac1{d_n}
(\widehat\sigma_n,\widehat\chi_n,\widehat\kappa_n),
$$


and


$$
V_n^*=\sigma_n^*\mathcal A_n-\chi_n^*\mathcal B_n-\kappa_n^*.
$$


Therefore


$$
\boxed{v_p(V_n^*)=0\qquad(p\in\mathcal P_4,\ n\ge0).}
\tag{4.4}
$$



Moreover, the exact raw contraction gcd is


$$
\gcd(|\sigma_n|,|\chi_n|,|\kappa_n|)
=12(2n+5)d_n,
$$


so at these four primes its depth is exactly


$$
\boxed{
v_p\!\left(\gcd(|\sigma_n|,|\chi_n|,|\kappa_n|)\right)
=v_p(2n+5).
}
\tag{4.5}
$$


This accounts for any further row, maximal-minor, or contraction content: it is contained in $d_n$, not omitted.

No periodicity of the globally primitive triple is needed or asserted.

---

## 5. The whole numerator and the final endpoint gcd

Let


$$
\mathsf P_j=L_j(1)
$$


and let $w_j$ be the rational second-kind endpoint from the supplied endpoint identities. Define


$$
\begin{aligned}
D_n^*&=(n+1)\mathsf P_{n+1}\chi_n^*
              -2\mathsf P_n\sigma_n^*,\\
Q_n^*&=2w_n\sigma_n^*
              -(n+1)w_{n+1}\chi_n^*,\\
S_n^*&=Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*.
\end{aligned}
\tag{5.1}
$$


The exact endpoint quotient is


$$
\boxed{\frac{X_n}{Y_n}=\frac{S_n^*}{D_n^*},
\qquad n\ge4,\quad D_n^*\ne0.}
\tag{5.2}
$$



For emphasis, with $f_n=2^n/(n!)^2$,


$$
T_P=f_n\mathcal A_n,\qquad
T_U=\frac{2f_n}{n+1}\mathcal B_n,
$$


the complete numerator is equivalently


$$
S_n^*
=
2(w_n+T_P)\sigma_n^*
-(n+1)(w_{n+1}+T_U)\chi_n^*
-2f_n\kappa_n^*.
\tag{5.3}
$$


Thus neither the second-kind contribution nor the $-\kappa_n^*$ contribution has been discarded.

The moment formula shows that


$$
2^n\operatorname{lcm}(1,\ldots,n+1)
$$


clears both $w_n,w_{n+1}$. Take


$$
\lambda_n=
\operatorname{lcm}\!\left(
(n!)^2,\,
2^n\operatorname{lcm}(1,\ldots,n+1)
\right).
$$


Then


$$
N_n=\lambda_nS_n^*,\qquad Z_n=\lambda_nD_n^*
$$


are integers. Define the **final endpoint gcd**


$$
g_n=\gcd(|N_n|,|Z_n|).
$$


Exactly,


$$
\boxed{
q_n=\frac{|Z_n|}{g_n},
\qquad
p_n=-\operatorname{sign}(Z_n)\frac{N_n}{g_n}.
}
\tag{5.4}
$$


The contraction gcd $d_n$ and final endpoint gcd $g_n$ are different objects.

### 5.1 Strict whole-numerator valuation separation

Fix $p\in\mathcal P_4$, and put


$$
F_p=v_p(n!),\qquad \ell_p=\lfloor\log_p(n+1)\rfloor.
$$


The moment denominators give


$$
v_p(Q_n^*)\ge-\ell_p.
$$


By (4.4),


$$
v_p\!\left(\frac{2^{n+1}}{(n!)^2}V_n^*\right)=-2F_p.
$$



For every odd $p$ and $n\ge p$,


$$
2v_p(n!)>\lfloor\log_p(n+1)\rfloor.
\tag{5.5}
$$


Indeed, if the right side is $1$, then $v_p(n!)\ge1$. If it is $a\ge2$, then


$$
n\ge p^a-1,\qquad v_p(n!)\ge p^{a-1}-1,
$$


and $2(p^{a-1}-1)>a$.

Consequently the two summands in $S_n^*$ have strictly different valuations, and


$$
\boxed{
v_p(S_n^*)=-2v_p(n!),\qquad n\ge p.
}
\tag{5.6}
$$


In particular, the complete numerator is nonzero.

Applying (5.4), or equivalently the valuation of the reduced rational quotient, gives


$$
\boxed{
v_p(q_n)
=2v_p(n!)+v_p(D_n^*)
\ge2v_p(n!).
}
\tag{5.7}
$$


The common arithmetic domain for all four primes is


$$
\boxed{n\ge17,\qquad D_n^*\ne0.}
\tag{5.8}
$$


No effective analytic normality cutoff is being claimed.

Thus


$$
q_n\ge\prod_{p\in\mathcal P_4}p^{2v_p(n!)}.
$$


With


$$
W_4=\sum_{p\in\mathcal P_4}\frac{2\log p}{p-1},
$$


Legendre’s formula yields


$$
\boxed{
q_n\ge
\frac{e^{W_4n}}{n^8\left(\prod_{p\in\mathcal P_4}p\right)^2}
}
\tag{5.9}
$$


on (5.8). This is a bound for the actual primitive denominator after its final gcd.

---

## 6. Eventual normality, nonvanishing, and the full exclusion

The supplied fixed-exponential-degree theorem applies to exactly the contact family in Section 1. At the fixed value $b=4$, it gives:

1. eventual uniqueness of the projective solution;
2. eventual $Y_n\ne0$, equivalently $D_n^*\ne0$;
3. eventual nonvanishing of the entire evaluated remainder; and
4.
   

$$
\frac{(-1)^nR_n(1)}{Y_n\epsilon_n}
   \longrightarrow(\sqrt2-1)^4,
   \qquad
   \log\epsilon_n=-\tau n+o(n),
$$


   where
   

$$
\tau=2\log(1+\sqrt2).
$$



The normality argument uses the nonzero fixed-size endpoint jet determinant; the remaining determinant in the whole remainder has an additional factorially small row. Thus the theorem applies to the complete $R_n(1)$, not its first nonzero Taylor coefficient. The row normalizations above are nonzero rational changes at every admissible integer index, so they do not alter this projective solution or its normalized error.

Using (1.1), the conclusion is


$$
e+\pi-c_n
=(-1)^n\epsilon_n(\sqrt2-1)^4(1+o(1)).
\tag{6.1}
$$



The supplied rational rate certificate gives


$$
W_4-\tau>
\frac{947481451}{3125000000}
=0.30319406432.
\tag{6.2}
$$


Combining (5.9) and (6.1),


$$
\begin{aligned}
\log|q_n(e+\pi)-p_n|
&=\log q_n+\log|e+\pi-c_n|\\
&\ge (W_4-\tau)n-8\log n
-2\sum_{p\in\mathcal P_4}\log p+o(n).
\end{aligned}
$$



### Full matched-$b=4$ exclusion theorem

For the endpoint-matched caps-$(n,4,n)$, contact-$2n+5$ family,


$$
\boxed{
\liminf_{n\to\infty}
\frac1n\log|q_n(e+\pi)-p_n|
\ge W_4-\tau>0.30319406432.
}
\tag{6.3}
$$


In particular,


$$
\boxed{|q_n(e+\pi)-p_n|>e^{3n/10}}
$$


for every sufficiently large integer $n$.

Therefore **no unbounded-index subsequence of this matched family produces shrinking primitive endpoint forms**.

If an integral representative of the same projective solution has endpoints $X,Y$, then


$$
-X/Y=p_n/q_n
$$


forces $Y=kq_n$, $X=-kp_n$ for a nonzero integer $k$. Its evaluated remainder is $k$ times the primitive form. Thus coefficient primitiveness cannot evade the exclusion.

This completes the full-family implication of the supplied finite certificate. No further $b=4$ primes or root disks are required.

---

# Part II. The distinct matched-$b=5$ normalization

## 7. Two contiguous factors and an additional degree factor

Now take the matched caps-$(n,5,n)$, contact-$2n+6$ family.

The four raw high-row functions, whose derivatives at $1$ form the rows, are


$$
R_1=F,\qquad R_2=z,
$$




$$
R_3=\frac{\mathscr F_{k+2}''}{k+2},
\qquad
R_4=\frac{\mathscr F_{k+3}'''}{k+3},
\qquad k=n+1.
$$


They are used with derivatives $j=0,\ldots,5$.

Define one more integral polynomial


$$
z_2=\frac{\mathscr F_{k+2}'}{k+2}=B_{k+1}G.
\tag{7.1}
$$


The last expression is division-free.

Equation (2.4) gives


$$
R_3=(k+1)^3F+(2k+3)\bigl(2G-(k+1)z\bigr).
\tag{7.2}
$$


Differentiate (2.3) at the next index. This gives


$$
\begin{aligned}
R_4
&=(k+2)^3G'
 +(2k+5)\bigl(2\mathscr F_{k+2}'-\mathscr F_{k+2}''\bigr)\\
&=(k+1)(k+2)^3z
 +(k+2)(2k+5)(2z_2-R_3).
\end{aligned}
\tag{7.3}
$$



Equations (7.2)–(7.3) are polynomial row identities, valid for every derivative column simultaneously.

Relative to the integral replacement basis


$$
\boxed{F,\ z,\ G,\ z_2,}
\tag{7.4}
$$


the triangular high-row change has determinant


$$
\boxed{4(k+2)(2k+3)(2k+5).}
\tag{7.5}
$$


Indeed, after eliminating the first two rows, the third contributes $2(2k+3)G$. Eliminating the first three rows from the fourth leaves


$$
2(k+2)(2k+5)z_2.
$$



In terms of $n$, the additional high-row factor is therefore


$$
\boxed{4(n+3)(2n+5)(2n+7).}
\tag{7.6}
$$



The factor $n+3$ is genuinely additional to the initial degree divisions in the raw rows. It comes from differentiating $2\mathscr F_{k+2}-\mathscr F_{k+2}'$: both derivatives have coefficients divisible by $k+2$.

---

## 8. Factorial-column content and a root-safe integral basis

Define


$$
J_5(P)=
\left(
P(1),\
[t^0](P'-P)(1+t),\ldots,
[t^4](P'-P)(1+t)
\right).
$$


Also put


$$
\mathcal E_5=(1,0,0,0,0,0),
$$




$$
\mathcal P_5=
\left(0,[t^0]\mathscr F_n(1+t),\ldots,[t^4]\mathscr F_n(1+t)\right),
$$




$$
\mathcal U_5=
\left(0,[t^0]\frac{F'(1+t)}k,\ldots,
[t^4]\frac{F'(1+t)}k\right).
$$



Define


$$
\begin{aligned}
\widetilde\sigma_n
&=-\det[J_5(F);J_5(z);J_5(G);J_5(z_2);
                 \mathcal E_5;\mathcal U_5],\\
\widetilde\chi_n
&=-\det[J_5(F);J_5(z);J_5(G);J_5(z_2);
                 \mathcal E_5;\mathcal P_5],\\
\widetilde\kappa_n
&=\det[J_5(F);J_5(z);J_5(G);J_5(z_2);
                 \mathcal U_5;\mathcal P_5].
\end{aligned}
\tag{8.1}
$$


Every entry is integral.

After taking successive column differences, the five remaining columns have the factorial divisors


$$
0!,1!,2!,3!,4!.
$$


Their product is


$$
0!1!2!3!4!=288.
$$


Combining this with (7.5), the raw $b=5$ contractions satisfy


$$
\boxed{
(\sigma_n^{(5)},\chi_n^{(5)},\kappa_n^{(5)})
=
1152(n+3)(2n+5)(2n+7)
(\widetilde\sigma_n,\widetilde\chi_n,\widetilde\kappa_n).
}
\tag{8.2}
$$



This is an exact integral normalization. It is not claimed to exhaust all universal or evaluated content.

In particular, at a modular root of $n+3$, $2n+5$, or $2n+7$, one evaluates the basis (7.4) and the determinants (8.1). **One never divides a zero residue by one of those factors.**

---

## 9. Normalized all-depth transfer for $b=5$

Set


$$
\widetilde V_n
=\widetilde\sigma_n\mathcal A_n
-\widetilde\chi_n\mathcal B_n-\widetilde\kappa_n.
\tag{9.1}
$$



The basis functions in (7.4) are obtained by finitely many applications of $T_k,B_k$ and the derivative recurrences. Their jets are polynomial over $\mathbb Z[1/2]$ in $n,H_n(1),H_n'(1),H_n''(1)$. The expression for $F'/k$ is the exact normalized-derivative circuit, not inversion of $k$.

The factorial-column normalization introduces only powers of $2$ and $3$. The scalar transfer proved in Section 3 therefore implies:



$$
\boxed{
m\equiv n\pmod{p^a}
\Longrightarrow
(\widetilde\sigma,\widetilde\chi,\widetilde\kappa,
 \widetilde V)_m
\equiv
(\widetilde\sigma,\widetilde\chi,\widetilde\kappa,
 \widetilde V)_n
\pmod{p^a}
}
\tag{9.2}
$$


for every $p\ge5$, every $a\ge1$, and all $m,n\ge0$.

A safe version at $3$ loses two digits, because $v_3(288)=2$:


$$
m\equiv n\pmod{3^{a+2}}
\Longrightarrow
(\widetilde\sigma,\widetilde\chi,\widetilde\kappa,
 \widetilde V)_m
\equiv
(\widetilde\sigma,\widetilde\chi,\widetilde\kappa,
 \widetilde V)_n
\pmod{3^a}.
\tag{9.3}
$$



For actual primitive contractions, retain


$$
d_n^{(5)}
=\gcd(|\widetilde\sigma_n|,|\widetilde\chi_n|,
                         |\widetilde\kappa_n|).
$$


Where this triple is nonzero,


$$
(\sigma_n^{(5)*},\chi_n^{(5)*},\kappa_n^{(5)*})
=\frac1{d_n^{(5)}}
(\widetilde\sigma_n,\widetilde\chi_n,\widetilde\kappa_n).
$$


At any prime,


$$
\boxed{
v_p(V_n^{(5)*})
=v_p(\widetilde V_n)
-\min\{v_p(\widetilde\sigma_n),
       v_p(\widetilde\chi_n),
       v_p(\widetilde\kappa_n)\}.
}
\tag{9.4}
$$


Again, this is a local valuation statement, not global-gcd periodicity.

---

## 10. An exact seed and a genuine $5$-adic obstruction

At the scalar seed $n=0$, $k=1$,


$$
F=x^2-x,\qquad
G=x^4-4x^3+4x^2,
$$




$$
z=2x^3-6x^2+4x,
\qquad
z_2=2x^5-15x^4+36x^3-24x^2.
$$


The four transformed high rows are


$$
\begin{pmatrix}
0&1&1&-1&0&0\\
0&-2&2&6&-2&0\\
1&-1&-4&2&4&-1\\
-1&11&18&-26&-16&15
\end{pmatrix}.
$$


The lower rows are


$$
\mathcal P_5=(0,1,0,0,0,0),
\qquad
\mathcal U_5=(0,1,2,0,0,0).
$$


Direct determinants give


$$
\boxed{
(\widetilde\sigma_0,\widetilde\chi_0,\widetilde\kappa_0)
=(76,-276,-56).
}
\tag{10.1}
$$


Since $\mathcal A_0=1$, $\mathcal B_0=3$,


$$
\boxed{\widetilde V_0=960.}
\tag{10.2}
$$


The evaluated contraction gcd is $4$, so the primitive seed is


$$
(\sigma_0^{(5)*},\chi_0^{(5)*},\kappa_0^{(5)*})
=(19,-69,-14),\qquad V_0^{(5)*}=240.
$$



This proves a concrete limitation: **$5$ cannot be an all-residue primitive-unit prime for this family.** At $n\equiv0\pmod5$, normalized transfer gives


$$
\widetilde\sigma_n\equiv1\pmod5,\qquad
\widetilde V_n\equiv0\pmod5.
$$


Thus the numerator zero is not removed by contraction content.

There is also a new all-index valuation lemma. Since


$$
960\equiv10\pmod{25},
$$


transfer modulo $25$ proves


$$
\boxed{
v_5(V_n^{(5)*})=1
\qquad(n\ge0,\ n\equiv0\pmod{25}).
}
\tag{10.3}
$$



For $n\ge5$, the complete endpoint quotient is still (5.1)–(5.4), using the $b=5$ primitive contractions. Hence, on


$$
n\equiv0\pmod{25},\qquad n\ge25,\qquad D_n^{(5)*}\ne0,
$$


strict separation gives


$$
\boxed{
v_5(q_{n,5})
=2v_5(n!)+v_5(D_n^{(5)*})-1
\ge2v_5(n!)-1.
}
\tag{10.4}
$$


The complete numerator is nonzero there.

The inherited fixed-$b$ theorem supplies eventual normality and


$$
e+\pi-c_{n,5}
=(-1)^n\epsilon_n(\sqrt2-1)^5(1+o(1)).
$$


However, (10.4) alone does not give enough denominator growth for a full exclusion, and it certainly is not a favorable small-denominator theorem for proving irrationality.

---

# Concluding ledger

## (1) New result and proof status

### Completed: full matched-$b=4$ exclusion

Using the supplied $46$-row finite certificate and the proved normalized transfer:

* the four selected primes are normalized numerator units at **every** scalar index;
* all contraction content is retained and removed correctly;
* the two terms of the **whole** numerator have strictly separated valuations for $n\ge17$;
* the lower bound is for the **actual primitive denominator after the final endpoint gcd**;
* the inherited analytic theorem supplies eventual normality, endpoint nonvanishing, and the whole-error rate.

Therefore


$$
\liminf_{n\to\infty}
\frac1n\log|q_n(e+\pi)-p_n|
>0.30319406432.
$$


This excludes every unbounded-index subsequence of the eventual matched-$b=4$ family from producing shrinking primitive forms.

The finite certificate was supplied and independently computed by the coordinator; no new execution is claimed here.

### New paper-level $b=5$ results

For the distinct matched caps-$(n,5,n)$, contact-$2n+6$ family:

* new contiguous factors $2n+7$ and $n+3$, in addition to $2n+5$;
* an integral replacement basis $F,z,G,z_2$;
* exact universal raw contraction factor
  

$$
1152(n+3)(2n+5)(2n+7);
$$


* normalized all-depth transfer at every $p\ge5$, including all modular roots of the removed factors;
* exact normalized seed $(76,-276,-56,960)$;
* a genuine primitive numerator root at $n\equiv0\pmod5$;
* the proved valuation $v_5(V_n^{(5)*})=1$ on $n\equiv0\pmod{25}$.

No full matched-$b=5$ exclusion or favorable denominator theorem is claimed.

## (2) Exact remaining bottleneck

The irrationality of $e+\pi$ remains unresolved.

For matched $b=5$, the next concrete obstruction is whether the newly normalized determinant contractions have further universal polynomial content. After that is resolved, one needs either:

* enough normalized unit or bounded-valuation primes to control the actual primitive denominator from below; or
* genuinely favorable control of the final endpoint gcd and whole numerator, sufficient for a small-denominator argument.

The prime $5$ already has a genuine numerator-root disk. It cannot simply replace the role it played in the successful $b=4$ unit certificate.

## (3) Bounded exact computation request

No further $b=4$ computation is requested.

For **matched $b=5$**, request the following fixed symbolic computation first.

### A. Symbolic content check

**Inputs:** the fixed six-column determinant circuit (8.1), with


$$
F=\mathscr F_{n+1},\quad
G=T_{n+1}F,\quad
z=B_{n+1}F,\quad
z_2=B_{n+2}G,
$$


and the finite jet recurrences from the supplied sources.

**Expected verifiable output:**

1. The gcd over $\mathbb Q[n,h,u,v]$ of
   

$$
\widetilde\sigma,\widetilde\chi,\widetilde\kappa.
$$


2. Exact factor/recomposition identities.
3. Common numerical coefficient content after clearing only powers of $2$ and $3$.
4. Confirmation of
   

$$
(\widetilde\sigma_0,\widetilde\chi_0,
     \widetilde\kappa_0,\widetilde V_0)
   =(76,-276,-56,960).
$$



If a nonconstant common factor remains, return its exact quotients and stop before any prime scan; its root-safe removal is then the next proof obligation.

### B. Conditional finite normalized certificate

If A confirms that no further nonconstant common factor remains, and any common coefficient content has been removed by an exact circuit, evaluate only


$$
\boxed{\{7,11,13,17,19\}}
$$


at all $0\le r<p$: exactly


$$
7+11+13+17+19=\boxed{67}
$$


residue rows.

Return:

* the full normalized contraction and $V$-vectors;
* numerator-zero sets and joint-contraction-zero sets separately;
* the exact normalization used;
* the aggregate rationally bounded weight of the primes with empty normalized numerator-zero sets.

This is a bounded normalized test for the new $b=5$ objects, not an unnormalized prime atlas and not a finite-computation claim about the irrationality of $e+\pi$.
