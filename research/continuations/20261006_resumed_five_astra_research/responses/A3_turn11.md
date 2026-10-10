> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 11 — Exact support of the reference-filter excess, complete-force Bézout identities, and boundary-prime audits

## Executive conclusions

The irrationality or rationality of $e+\pi$ remains unresolved.

The completed $3375$ calculations are substantially stronger than the formerly pending scalar certificate. I accept them at their stated finite scope:



$$
|\Theta_{3375}|=U_{3375}D_{3375}^{>},
\qquad
U_{3375}=2^{14}\cdot31\cdot67\cdot211\cdot239,
$$


with


$$
\operatorname{bits}(\Theta_{3375})=110096,\qquad
\operatorname{bits}(D_{3375}^{>})=110055,
$$


and


$$
\gcd(D_{3375}^{>},\Sigma_{3375})=1.
$$


The new, evaluated reference filtering gives


$$
\boxed{H_{3375}^{\rm ref}=V_{0,3375}=V_{3,3375}
       =V_{3375}=\mathcal W_{3375}^{\rm ref}=1.}
$$



The large exclusive divisor survives the collision-defect support filter but not the endpoint reference filter. This is an actual evaluated target certificate, not an inference from the previously known endpoint contents.

This turn proves an infinite-domain structural refinement of that filtering.

Define the **reference-alignment content**


$$
\boxed{
\mathcal I_n
=
\gcd\!\left(
|F|,\,
|Q\widehat h-P\widehat\ell|
\right)_{>N},
\qquad N=n+2,
}
\tag{E1}
$$


and the two canonical scalar/reference gcds


$$
\boxed{
\Delta_{j,n}
=
\gcd\!\left(D_n^{>},|\widehat R_j|\right),
\qquad j=0,3.
}
\tag{E2}
$$



For every original index,


$$
\boxed{
\delta_j^{>}\mid\Delta_{j,n}\mid\mathcal I_n\delta_j^{>}.
}
\tag{E3}
$$


Moreover,


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid\mathcal W_n^{\rm ref}
\mid\Delta_{0,n}\Delta_{3,n}
\mid\mathcal I_n^2\delta_0^{>}\delta_3^{>}.
}
\tag{E4}
$$



Thus the filtered certificate can overestimate the actual endpoint-content product **only at reference-alignment primes**, and its excess divides the square of the explicitly evaluated content (E1):


$$
\boxed{
\frac{\mathcal W_n^{\rm ref}}{\delta_0^{>}\delta_3^{>}}
\mid\mathcal I_n^2.
}
\tag{E5}
$$



Away from $\mathcal I_n$, this is an equality theorem, not merely a bound. In particular, the endpoint-specific filters are exact there:


$$
\boxed{
\operatorname{strip}_{\mathcal I_n}(V_{j,n})
=
\operatorname{strip}_{\mathcal I_n}(E_{j,n}).
}
\tag{E6}
$$



The theorem applies throughout the infinite original domain. It does **not** prove a subfactorial bound for the surviving content. The proved cost is


$$
\log\mathcal I_n\le \log(n!)+O(n),
\tag{E7}
$$


not $o(n\log n)$.

I also derive explicit integral Bézout identities between the actual canonical scalar, each actual reference projection, and the complete exponential-force projection. Their constant terms retain the logarithmic contribution $2L_{\rm ref}F(n!)^2$. They identify an exact affine congruence that any surviving prime must satisfy; they do not turn that congruence into a coprimality theorem.

Finally, I independently audit both omitted boundary cases of the Turn 10 residue law:

* At $a=p-1$, the explicit factor $m=n+1$ is genuine. A quotient congruence determines when its $p$-adic depth is exact.
* At $p=N=n+2$, Wilson’s theorem makes $(n!)^2$ a unit, and the factorial term cannot be deleted. I give its explicit corrected boundary formula.

No accepted producer, endpoint denominator, endpoint gcd table, or whole-error calculation is requested again.

---

# I. Assessment of the new sources

## 1. The canonical scalar receipt

The supplied scalar postprocessing uses the retained complete data to form


$$
b_n=u_n-E_nh_n-a_n,\qquad
b_{n+1}=u_{n+1}-E_nh_{n+1}-a_{n+1},
$$


and


$$
\mathscr K_n
=h_nb_{n+1}-h_{n+1}b_n-2(n!)^3.
$$


It then evaluates


$$
\Theta_n
=\frac{2^{(n+1)/2}}{n!}
\left[mZ(Qh-P\ell)-F\mathscr K_n\right]
$$


and checks its integral normalization exactly.

The small-prime extraction removes **every** prime through $3377$, including its complete valuation. Therefore the reported factorization of $U_{3375}$ is the complete canonical smooth part, not a selected-prime sample.

The receipt establishes neither an asymptotic failure nor an asymptotic success of


$$
\log U_n\ge 3\log(n!)-O(n).
$$


The same distinction applies to the exact omissions of $3,5,7$: deleting finitely many fixed-prime factorial contributions costs only $O(n)$.

The reported binary depth $14$ and the absence of $3,5,7$ agree with the proved Turn 10 laws.

## 2. The reference-filter receipt

The reference-filter code:

1. reconstructs the actual primitive contact rows from the retained moment entries;
2. forms both actual hatted references;
3. reuses $\mathcal B_{3375}=1$;
4. applies the collision-defect support stripping;
5. removes the full collision depth from each reference before taking the endpoint gcd;
6. computes $\mathcal W^{\rm ref}$ without recomputing either complete endpoint gcd.

Its exact outputs are therefore genuinely new arithmetic observations. In particular, the calculation did not manufacture $\mathcal W^{\rm ref}=1$ by substituting the previously known values $\delta_0^{>}=\delta_3^{>}=1$.

The result at $3375$ is:


$$
\begin{array}{c|c}
\text{Field}&\text{Value}\\ \hline
\operatorname{bits}(\widehat R_0),\operatorname{bits}(\widehat R_3)
&83979,\ 83969\\
H^{\rm ref}&1\\
\text{exclusive divisor before defect filtering}&110055\text{ bits}\\
\text{exclusive divisor after defect filtering}&110055\text{ bits}\\
V_0,\ V_3,\ V&1,\ 1,\ 1\\
\mathcal W^{\rm ref}&1
\end{array}
$$



This strongly motivates studying the reference-filtered route. It does not establish an infinite-family coprimality theorem.

## 3. The selected-prime note

The coordinator’s proof for odd $p\mid n$ is correct. Its coefficient argument pays the relevant integrality, and its division by $n!$ takes place in the exact expression before reduction, not by dividing a zero residue.

The resulting congruence


$$
\Theta_n\equiv4L_{\rm ref}\tau_n\pmod p
\qquad(p\text{ odd},\ p\mid n)
$$


is the $a=0$ case of the broader Turn 10 law.

The $26$ auxiliary primewise checks, $240$ Lucas checks, and retained $3375$ residues are finite corroborations of those symbolic statements. They do not audit the $a=1$, $a=p-1$, or $p=N$ cases by themselves.

The classical constant-term Lucas theorem is reused as background. The short support proof suffices for this particular sequence. No claim of exhaustive novelty is made.

---

# II. Definitions and unchanged construction

Throughout the main theorems,


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2,
$$


and


$$
m=n+1,\qquad N=n+2,\qquad L_{\rm ref}=2^{m/2}.
$$



Retain


$$
X=ma_n,\qquad Y=mna_{n-1},\qquad Z=2a_{n+1}-ma_n,
$$




$$
P=nX+Y,\qquad Q=nZ+2X-Y,
$$




$$
F=2m\bigl(Y-2X-(n-1)Z\bigr).
$$



The hatted reference pair is


$$
\widehat h=L_{\rm ref}\tau_n,\qquad
\widehat\ell=L_{\rm ref}\tau_{n+1}.
$$


For each actual primitive contact row $r_j$, write


$$
\alpha_j=r_jv',\qquad
\beta_j=r_jw',\qquad
\gamma_j=r_je_2,
$$


where


$$
v'=(2N,N,m)^T,\qquad
w'=(0,N,2n+3)^T.
$$


Then


$$
\widehat R_j=\alpha_j\widehat h+\beta_j\widehat\ell,
$$


and the shared-column relation is


$$
\boxed{P\alpha_j+Q\beta_j+F\gamma_j=0.}
\tag{2.1}
$$



All large-prime statements below are at $p>N$. At this scope,


$$
2,\ m,\ N,\ n!,\ L_{\rm ref}
$$


are units. The actual hatted and unhatted reference projections have the same valuations.

The original finite matrix, force cutoff $2n+2$, complete terminal return, both corrected reconstruction columns, and final primitive normalization are unchanged.

---

# III. A canonical support theorem for the reference-filter excess

## 4. Exact content of the transverse reference

Put


$$
M_n^{\rm ref}=Q\widehat h-P\widehat\ell.
$$



### Lemma 4.1 — Evaluated transverse-reference content

Fix $p>N$. In the quotient transverse to the primitive shared column $L=nJ_0+J_1$, the normalized reference column has content valuation


$$
\boxed{
a_p^{\rm ref}
=
\min\{v_p(F),v_p(M_n^{\rm ref})\}.
}
\tag{4.1}
$$



#### Proof

Use the coordinate basis $(v',w',e_2)$, whose determinant $2N^2$ is a unit. Up to unit scalars, the shared column and normalized reference are


$$
(P,Q,F)^T,\qquad
(\widehat h,\widehat\ell,0)^T.
$$


Their exterior product has coordinates


$$
-F\widehat\ell,\qquad F\widehat h,\qquad
P\widehat\ell-Q\widehat h.
$$



The reference pair generates the unit ideal at $p>N$. Hence the minimum valuation of these three coordinates is


$$
\min\{v_p(F),v_p(M_n^{\rm ref})\}.
$$



Because the shared column is primitive, completing it to a local basis identifies this exterior-product content with the content of the two transverse reference coordinates. ∎

Consequently,


$$
\mathcal I_n
=\gcd(|F|,|M_n^{\rm ref}|)_{>N}
$$


is an actual, canonically evaluated content. It is not an arbitrary saturation factor.

Also,


$$
\boxed{\mathcal B_n\mid\mathcal I_n.}
\tag{4.2}
$$


One can see this either from the source matrix—its content cannot exceed the content of its reference column—or directly from


$$
Q=nZ-(Y-2X),\qquad
F=2m\bigl((Y-2X)-(n-1)Z\bigr).
$$



The two integers $F,M_n^{\rm ref}$ cannot both be zero at an original index, since


$$
\Theta_n=mZM_n^{\rm ref}-F\widehat{\mathscr K}
$$


and $\Theta_n\ne0$. Thus $\mathcal I_n$ is a well-defined positive integer.

---

## 5. Each scalar/reference gcd differs from the actual content by at most $\mathcal I_n$

Recall


$$
\Delta_{j,n}=\gcd(D_n^{>},|\widehat R_j|).
$$



### Theorem 5.1

At every original index,


$$
\boxed{
\delta_j^{>}\mid\Delta_{j,n}\mid\mathcal I_n\delta_j^{>},
\qquad j=0,3.
}
\tag{5.1}
$$



#### Proof

Fix $p>N$, and abbreviate


$$
d=v_p(\Theta_n),\qquad
r=v_p(\widehat R_j),\qquad
e=v_p(\delta_j^{>}),\qquad
a=a_p^{\rm ref}.
$$



Complete the shared column to a local basis. By Lemma 4.1, a further unimodular change of the transverse coordinates puts the reference and complete residual columns in the form


$$
H_\perp=(p^a,0)^T,\qquad C_\perp=(x,y)^T,
$$


after absorbing a unit into the first coordinate.

The actual endpoint row becomes a primitive pair $(u,v)$. Therefore


$$
r=a+v_p(u),
$$


and


$$
e=\min\{a+v_p(u),\,v_p(ux+vy)\}.
$$


The source determinant identity gives


$$
d=a+v_p(y).
$$


Thus


$$
k:=\min(d,r)
=a+\min\{v_p(y),v_p(u)\}.
$$



The established source-content bound gives $e\le d$, and plainly $e\le r$, so $e\le k$.

For the other direction,


$$
v_p(ux+vy)\ge\min\{v_p(u),v_p(y)\},
$$


because $x,y,u,v\in\mathbb Z_p$. The reference projection has at least the same lower bound. Hence


$$
e\ge \min\{v_p(u),v_p(y)\}=k-a.
$$



We have proved


$$
\boxed{0\le k-e\le a.}
\tag{5.2}
$$


This is exactly (5.1), prime by prime. ∎

This theorem is about the actual complete residual. The transverse determinant used in its proof is the determinant whose valuation is $v_p(\Theta_n)$, including the seed subtraction and logarithmic term.

---

## 6. The filtered certificate lies between the actual product and the two scalar/reference gcds

The lower divisibility


$$
\delta_0^{>}\delta_3^{>}\mid\mathcal W_n^{\rm ref}
$$


was proved in Turn 10. The following additional upper divisibility is useful.

### Theorem 6.1



$$
\boxed{
\mathcal W_n^{\rm ref}\mid\Delta_{0,n}\Delta_{3,n}.
}
\tag{6.1}
$$



#### Proof

Fix $p>N$. Use the local notation


$$
b=v_p(\mathcal B_n),\qquad
d=v_p(\Theta_n),\qquad
s=v_p(\Sigma_n),\qquad
a=d-2b\ge0,
$$




$$
r_j=v_p(\widehat R_j),\qquad
t_j=r_j-b\ge0,
$$


and


$$
h=\min(s,t_0,t_3).
$$


The exponent in $\Delta_{0,n}\Delta_{3,n}$ is


$$
k_0+k_3,\qquad k_j=\min(d,r_j).
$$



The exclusive upper divisor has exponent $(a-s)_+$. If $h<s$, the collision-defect support filter removes this prime completely. Thus the exponent $w$ in $\mathcal W_n^{\rm ref}$ satisfies


$$
w\le \min\{d+\min(s,a),\,2b+2h\}.
$$


Here $\min(r_0,r_3)=b+h$, and $d+\min(s,a)\le2d$. Therefore


$$
w\le2\min\{d,\min(r_0,r_3)\}\le k_0+k_3.
$$



Now suppose $h=s$.

If $a\le s$, the exclusive upper divisor has exponent zero, and


$$
w\le d+a=2(d-b).
$$


Also $r_j\ge b+s\ge b+a=d-b$, so $k_j\ge d-b$. Again $w\le k_0+k_3$.

Finally suppose $a>s$, and put


$$
u=b+s,\qquad r_{\max}=\max(r_0,r_3).
$$


The exponent contributed by the endpoint-reference lcm is


$$
\min\{a-s,r_{\max}-u\}.
$$


Hence


$$
w\le
2u+\min\{a-s,r_{\max}-u\}
=u+\min\{d-b,r_{\max}\}.
$$


Since $r_{\min}\ge u$ and $d\ge u$,


$$
\min(d,r_{\min})\ge u,
$$


while


$$
\min(d,r_{\max})\ge\min(d-b,r_{\max}).
$$


This proves the desired inequality in the final case. ∎

Combining Theorems 5.1 and 6.1 with the established filtered product theorem yields


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid\mathcal W_n^{\rm ref}
\mid\Delta_{0,n}\Delta_{3,n}
\mid\mathcal I_n^2\delta_0^{>}\delta_3^{>}.
}
\tag{6.2}
$$



In particular,


$$
\boxed{
\operatorname{strip}_{\mathcal I_n}(\mathcal W_n^{\rm ref})
=
\operatorname{strip}_{\mathcal I_n}(\delta_0^{>}\delta_3^{>}).
}
\tag{6.3}
$$



This is the new canonical support theorem.

---

## 7. Exact collision and exclusive factors away from reference alignment

There is a more detailed consequence.

Fix $p>N$ with $p\nmid\mathcal I_n$. The transverse reference is primitive, and therefore the full source content has $b=0$. The observation matrix has determinant valuation $s$, so its two reference projections satisfy


$$
\min(r_0,r_3)\le s.
\tag{7.1}
$$


Otherwise the adjugate observation identity would make the transverse reference nonprimitive.

Theorem 5.1 now gives


$$
e_j=\min(d,r_j).
\tag{7.2}
$$



If $\min(r_0,r_3)<s$, the two primitive observation rows are unit-proportional modulo $p^s$, so


$$
r_0=r_3=\min(r_0,r_3).
$$


There is no endpoint-exclusive content, and the defect filter correctly removes the prime from the exclusive divisor.

If $\min(r_0,r_3)=s$, the larger endpoint has exclusive depth


$$
\min\{(d-s)_+,(r_{\max}-s)_+\},
$$


which is precisely the depth retained by the corresponding endpoint reference filter.

Thus, away from $\mathcal I_n$,


$$
\boxed{
V_{j,n}=E_{j,n}\quad\text{prime by prime}.
}
\tag{7.3}
$$


The common factor is also exact after clipping:


$$
\boxed{
\operatorname{strip}_{\mathcal I_n}(g_n)
=
\operatorname{strip}_{\mathcal I_n}
\bigl(\gcd(D_n^{>},H_n^{\rm ref})\bigr).
}
\tag{7.4}
$$



Notice the necessary clipping by $D_n^{>}$. An unqualified equality $g_n=H_n^{\rm ref}$ would be false as a general inference.

### What this does and does not accomplish

The reference filters are not merely heuristic exclusions. Except at the explicitly identified alignment support $\mathcal I_n$, they recover the actual common and exclusive factors exactly.

But exactness is not smallness. A surviving prime outside $\mathcal I_n$ represents actual complete-force endpoint cancellation. No uniform bound for the product of those primes is supplied by (7.3).

---

## 8. Size of the paid alignment cost

The moment estimates already established in Turn 9 give


$$
|F|\le n!\,e^{O(n)}.
$$


The same estimates, together with


$$
|\widehat h|+|\widehat\ell|=e^{O(n)},
$$


give


$$
|M_n^{\rm ref}|\le n!\,e^{O(n)}.
$$


Because $F,M_n^{\rm ref}$ are not both zero,


$$
\boxed{\log\mathcal I_n\le\log(n!)+O(n).}
\tag{8.1}
$$



Consequently,


$$
0\le
\log\mathcal W_n^{\rm ref}
-\log(\delta_0^{>}\delta_3^{>})
\le2\log\mathcal I_n
\le2\log(n!)+O(n).
\tag{8.2}
$$



This is a controlled denominator cost, but it is still factorial-scale. I do not relabel it subfactorial.

---

# IV. Explicit complete-force Bézout identities

## 9. The force projection used in the identities

Write


$$
v_n=u_n-a_n,\qquad v_{n+1}=u_{n+1}-a_{n+1}.
$$


These do not include the fixed $E_n$-seed subtraction.

For each endpoint define


$$
\boxed{
\mathcal E_{j,n}
=
\frac m2(\alpha_j-\beta_j)v_n
+\beta_jv_{n+1}
+mZ\gamma_j.
}
\tag{9.1}
$$



This is an integer. It is the corresponding exponential/exterior projection before the fixed homogeneous seed and logarithmic companion are restored.

The actual complete residual is still


$$
\boxed{
C_j
=
\mathcal E_{j,n}
-E_nR_j
+2n!m!\,(\alpha_j\rho_n+\beta_j\rho_{n+1}).
}
\tag{9.2}
$$


Equation (9.2) is retained, not replaced by $C_j=\mathcal E_{j,n}$.

Set


$$
\begin{aligned}
\mathcal T_n
&=mZQ-Fv_{n+1}+\frac{mF}{2}v_n,\\
\mathcal S_n
&=-mZP+\frac{mF}{2}v_n.
\end{aligned}
$$


The exact canonical decomposition is


$$
\boxed{
\Theta_n
=
\mathcal T_n\widehat h+\mathcal S_n\widehat\ell
+2L_{\rm ref}F(n!)^2.
}
\tag{9.3}
$$



## 10. Integral endpoint Bézout identities

### Theorem 10.1

For $j=0,3$,


$$
\boxed{
\beta_j\Theta_n-\mathcal S_n\widehat R_j
=
F\left(-\widehat h\,\mathcal E_{j,n}
       +2L_{\rm ref}(n!)^2\beta_j\right),
}
\tag{10.1}
$$


and


$$
\boxed{
\alpha_j\Theta_n-\mathcal T_n\widehat R_j
=
F\left(\widehat\ell\,\mathcal E_{j,n}
       +2L_{\rm ref}(n!)^2\alpha_j\right).
}
\tag{10.2}
$$



#### Proof

Using the shared-column relation (2.1),


$$
\begin{aligned}
\beta_j\mathcal T_n-\alpha_j\mathcal S_n
&=mZ(\beta_jQ+\alpha_jP)
-F\beta_jv_{n+1}
+\frac{mF}{2}(\beta_j-\alpha_j)v_n\\
&=-F\left[
mZ\gamma_j+\beta_jv_{n+1}
+\frac m2(\alpha_j-\beta_j)v_n
\right]\\
&=-F\mathcal E_{j,n}.
\end{aligned}
$$


Substitution into (9.3) proves (10.1). The reversed combination proves (10.2). ∎

These are evaluated, target-specific identities. They use the actual contact-row coefficients and actual force coefficients. No generic resultant-existence theorem is being used.

The terms


$$
2L_{\rm ref}F(n!)^2\alpha_j,\qquad
2L_{\rm ref}F(n!)^2\beta_j
$$


are indispensable: they retain the complete logarithmic determinant contribution.

---

## 11. What a surviving nonalignment prime must satisfy

Suppose


$$
p>N,\qquad p\nmid F,\qquad
p\mid\Theta_n,\qquad p\mid\widehat R_j.
$$


Then (10.1)–(10.2) give


$$
\boxed{
\widehat h\,\mathcal E_{j,n}
\equiv2L_{\rm ref}(n!)^2\beta_j\pmod p,
}
\tag{11.1}
$$




$$
\boxed{
\widehat\ell\,\mathcal E_{j,n}
\equiv-2L_{\rm ref}(n!)^2\alpha_j\pmod p.
}
\tag{11.2}
$$



At least one of $\alpha_j,\beta_j$ is a unit. Indeed, if both vanished modulo $p$, relation (2.1), $p\nmid F$, and primitivity of the actual row would give a contradiction.

Since $(\widehat h,\widehat\ell)$ is a unit pair, equations (11.1)–(11.2) force


$$
\boxed{p\nmid\mathcal E_{j,n}.}
\tag{11.3}
$$



More generally, putting


$$
G_j^{\alpha\beta}=\gcd(|\alpha_j|,|\beta_j|),
$$


the two identities imply


$$
\boxed{
\gcd(\Theta_n,\widehat R_j,\mathcal E_{j,n})_{>N}
\mid (F\,G_j^{\alpha\beta})_{>N}
\mid (F^2)_{>N}.
}
\tag{11.4}
$$


The second divisibility follows from (2.1) and row primitivity: at a prime dividing both $\alpha_j,\beta_j$, $\gamma_j$ is a unit and their common depth is at most $v_p(F)$.

### The remaining obstruction is now explicit

For $p>N$, $n!$ is a unit. Thus the right side of (11.1) is not killed by factorial divisibility.

A surviving prime must satisfy a particular **affine complete-force congruence**. Neither the reference unit-ideal theorem nor the real size of $\Theta_n$ excludes it. A useful next arithmetic lemma must control the common prime divisors generated by these affine congruences, including their higher depths and the collision filtering.

Merely observing that the homogeneous reference pair is primitive is insufficient.

---

# V. Independent audit of the all-prime residue boundaries

## 12. Interior digits and the $a=1$ extension

Let $p\le n$ be odd and


$$
n=pb+a,\qquad 0\le a<p.
$$


For $i\ge p$,


$$
c_i(n)=i![z^i]q(z)^n\equiv0\pmod p.
$$


For $i<p$, Frobenius gives the low-degree reduction


$$
c_i(n)\equiv c_i(a)\pmod p.
$$


The moment and force sums therefore reduce with the actual binomial low digit, while


$$
E_s\equiv E_{s\bmod p}\pmod p.
$$



For $a\le p-2$, both $n$ and $n+1$ are covered without a carry, and


$$
L_{\rm ref}^{-1}\Theta_n\equiv\tau_b\phi_a\pmod p.
$$


The term $2F(n!)^2$ is legitimately zero here.

The evaluation


$$
\phi_1=8
$$


therefore applies to $n=15^r\equiv1\pmod7$. This is a valid extension beyond the coordinator’s $p\mid n$ note.

It follows, as before, that


$$
\gcd(\Theta_n,105)=1
$$


throughout the original domain.

---

## 13. The $a=p-1$ case: exact factor and quotient law

The integral hatted expression immediately shows


$$
\boxed{m\mid\Theta_n.}
\tag{13.1}
$$


Indeed, both $mZ$ and $F$ contain $m$, and $\widehat{\mathscr K}$ is integral.

Define


$$
\Psi_n=\Theta_n/m\in\mathbb Z.
$$



### Proposition 13.1

Let $p$ be an odd prime dividing $m=n+1$. Write


$$
n=pb+p-1,
\qquad
\varepsilon_p=(-1)^{(p-1)/2}.
$$


Then


$$
\boxed{
\Psi_n
\equiv
4L_{\rm ref}\varepsilon_p\tau_b
\bigl(1-2E_{p-1}\bigr)\pmod p.
}
\tag{13.2}
$$



#### Proof

Every odd divisor of $m$ is at most $n$, so the factorial term vanishes modulo $p$.

Since $n+1\equiv0\pmod p$, the moment and force sums at that index have only their $i=0$ low-digit contribution:


$$
a_{n+1}\equiv1,\qquad
u_{n+1}\equiv E_{p-1}\pmod p.
$$


Thus


$$
Z\equiv2,\qquad
v_{n+1}\equiv E_{p-1}-1.
$$



After dividing the exact expression by $m$,


$$
\Psi_n
=
Z(Q\widehat h-P\widehat\ell)
-\frac Fm\widehat{\mathscr K}.
$$


Modulo $p$,


$$
P=0,\qquad Q=-Z,\qquad F/m=4Z,
\qquad
\widehat{\mathscr K}=\widehat h\,v_{n+1}.
$$


Hence


$$
\Psi_n
\equiv
-Z\widehat h\bigl(Z+4v_{n+1}\bigr)
=
4\widehat h(1-2E_{p-1}).
$$



Finally,


$$
\tau_n\equiv\tau_{p-1}\tau_b
=\varepsilon_p\tau_b\pmod p,
$$


by Lucas and the top coefficient of


$$
(1-2t-t^2)^{(p-1)/2}.
$$


This proves (13.2). ∎

In particular, if


$$
\tau_b\not\equiv0\pmod p,\qquad
2E_{p-1}\not\equiv1\pmod p,
$$


then


$$
\boxed{v_p(\Theta_n)=v_p(n+1).}
\tag{13.3}
$$



This is a positive-valuation statement, not another prime-unit list. It explains why the odd smooth part need not be trivial and gives an exact criterion for a controlled factor of $\Theta_n$.

It does not make that factor large enough for the required smooth-mass estimate.

---

## 14. The factorial boundary $p=N=n+2$

Suppose $p=n+2$ is prime. Then $n=p-2$, and Wilson gives


$$
n!=(p-2)!\equiv1\pmod p.
\tag{14.1}
$$


The factorial term in (9.3) is therefore a unit multiple of $F$, not zero.

The low-degree generating-function reduction gives


$$
\tau_{p-1}\equiv\varepsilon_p,\qquad
\tau_{p-2}\equiv-\varepsilon_p\pmod p.
\tag{14.2}
$$


The second identity is the next-to-leading coefficient of
$(1-2t-t^2)^{(p-1)/2}$.

Because $m=-1\pmod p$,


$$
Q+P=-2Z,\qquad
\tau_n+\tau_{n+1}=0.
$$


Substitution into the full canonical expression yields:

### Proposition 14.1 — Correct boundary formula



$$
\boxed{
L_{\rm ref}^{-1}\Theta_n
\equiv
2F+\varepsilon_p\left(
Fv_{n+1}-2Z^2
\right)\pmod p,
\qquad p=n+2.
}
\tag{14.3}
$$



Equivalently,


$$
L_{\rm ref}^{-1}\Theta_n
\equiv\phi_n+2F\pmod p.
\tag{14.4}
$$



The $2F$ term is the missing factorial-boundary correction. Applying the interior formula without it would be incorrect.

---

# VI. Consequences for actual denominators and weights

## 15. Complementary-prime endpoint denominators

Put


$$
A_j^{>}=(|\widehat R_j|)_{>N}=(|R_j|)_{>N}.
$$


The actual endpoint identity gives


$$
\boxed{
(d_j)_{>N}=\frac{A_j^{>}}{\delta_j^{>}}.
}
\tag{15.1}
$$


Consequently,


$$
\boxed{
(d_0d_3)_{>N}
=
\frac{A_0^{>}A_3^{>}}{\delta_0^{>}\delta_3^{>}}
\ge
\frac{A_0^{>}A_3^{>}}{\mathcal W_n^{\rm ref}}.
}
\tag{15.2}
$$



With the sharper projection comparison,


$$
\delta_j^{>}\mid\mathfrak D_j\mid B_j\delta_j^{>},
$$


one retains


$$
\boxed{
\mathfrak D_0\mathfrak D_3
\mid B_0B_3\mathcal W_n^{\rm ref},
}
\tag{15.3}
$$


where


$$
B_0B_3\le
(n^2+6n+4)(n^2+4n+1).
$$


Thus the projection route pays only


$$
\log(B_0B_3)=O(\log n)
$$


in addition to the filtered-content bound.

A proved estimate


$$
\log\mathcal W_n^{\rm ref}=o(n\log n)
$$


would imply that complementary-prime cancellation removes only a subfactorial amount from the product of the actual reference numerators. It would not by itself provide the final weighted denominator.

## 16. The all-prime weighted denominator

For the retained endpoint decomposition


$$
d_0=h_{\rm end}|A_{\rm wt}|,\qquad
d_3=h_{\rm end}|B_{\rm wt}|,
$$


the actual formula is


$$
q_\lambda
=
\frac{k_{\rm wt}d_0d_3}
{h_{\rm end}F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
\tag{16.1}
$$


Therefore


$$
\boxed{
(q_\lambda)_{>N}
=
\frac{(k_{\rm wt})_{>N}A_0^{>}A_3^{>}}
{\delta_0^{>}\delta_3^{>}
 (h_{\rm end}F_{\rm gcd}G_{\rm wt}H_{\rm gcd})_{>N}}.
}
\tag{16.2}
$$



Replacing $\delta_0^{>}\delta_3^{>}$ by the filtered certificate gives a valid lower bound. Using the projected-content route adds the displayed $B_0B_3$ cost.

But none of


$$
h_{\rm end},\quad F_{\rm gcd},\quad G_{\rm wt},\quad H_{\rm gcd}
$$


may be discarded. In particular, a small endpoint-content product does not prohibit weight-induced cancellation.

---

# VII. Complete reconstruction and whole-error normalization

The original reconstruction remains


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$




$$
S=
\begin{pmatrix}
1&-n&n(n+1)\\
0&1&-2n\\
0&0&1
\end{pmatrix},
\qquad sx=Sx,\quad sy=Sy,
$$


with all eight entries


$$
\boxed{
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
}
$$




$$
\boxed{
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
}
$$


The exterior $+1$ remains in $v_0$.

The least clearer is over all eight entries, followed by division of every reconstructed row by its actual two-entry content. At $3375$, those accepted contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$



The complete forcing remains


$$
F_k=(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3},
$$


through the original cutoff $2n+2$, with the complete terminal return. No extra recurrence step is introduced.

For $\lambda=a/k_{\rm wt}$, retain


$$
J_{\rm wt}=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A_{\rm wt}|,|a|)
 \gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


Every prime remains in these gcds.

The primitive numerator is


$$
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
$$


and the whole same-index error is still


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{17.1}
$$



The five accepted $3375$ whole forms remain nonzero and have absolute value greater than $1$. Neither the new support theorem nor $\Theta_n\ne0$ changes those evaluations.

---

# VIII. Universal coprimality, new bounded arithmetic, and the remaining lemma

## 18. Is the conjecture $\mathcal W_n^{\rm ref}=1$ false?

The supplied evidence and the theorems here do **not** determine whether


$$
\mathcal W_n^{\rm ref}=1
$$


holds at every original index.

I have not obtained a counterexample in the original domain, and I do not claim one.

The new theorem clarifies the conjecture’s content:

* Away from $\mathcal I_n$, it asserts the absence of **actual** endpoint cancellation.
* On $\mathcal I_n$, it additionally excludes possible certificate excess, whose depth is bounded by $2v_p(\mathcal I_n)$.

Thus universal $\mathcal W_n^{\rm ref}=1$ is stronger than merely having a useful subfactorial certificate.

An auxiliary counterexample outside the original domain would disprove an all-odd-index extension, not the stated all-original conjecture. That domain distinction is essential.

## 19. A new hand-evaluated boundary check

No finite computation is needed for the proofs above. There is, however, a short new boundary calculation at the auxiliary index


$$
n=9,\qquad p=N=11,
$$


which is not among the auxiliary scalar indices listed in the supplied receipts.

This is **not** an approximation index added to the original family.

Using the integral coefficient recurrence for $q(z)^9$, the residues $c_0,\ldots,c_{10}$ modulo $11$ are


$$
(1,2,4,6,5,1,6,10,1,10,1).
$$


The actual finite moment and force sums give


$$
a_8=9,\qquad a_9=7,\qquad a_{10}=0,\qquad u_{10}=9
\pmod{11}.
$$


Hence


$$
Z=7,\qquad F=4,\qquad v_{10}=9,\qquad
L_{\rm ref}=10,\qquad\varepsilon_{11}=10
\pmod{11}.
$$


The corrected boundary expression is


$$
L_{\rm ref}^{-1}\Theta_9
=
2F+\varepsilon_{11}(Fv_{10}-2Z^2)
=4\pmod{11},
$$


so


$$
\boxed{\Theta_9\equiv7\pmod{11}.}
\tag{19.1}
$$



Deleting the factorial correction would instead give the erroneous residue $4$ for $\Theta_9$.

At the same auxiliary index, $5\mid n+1$. Proposition 13.1 gives


$$
\boxed{\Theta_9/10\equiv3\pmod5,\qquad v_5(\Theta_9)=1.}
\tag{19.2}
$$



These are bounded modular calculations, not a full computation of $\Theta_9$, the contact contents, or $\mathcal W_9^{\rm ref}$.

If an independent exact arithmetic check of these new boundary fields is desired, its inputs are only:

* $n=9$;
* the displayed coefficient recurrence and finite moment/force sums;
* the canonical hatted formula for $\Theta_n$.

Its expected outputs are precisely (19.1)–(19.2). No archived producer or accepted $225/3375$ calculation is involved.

## 20. The concrete outstanding lemma

The new support theorem removes one ambiguity: large factors surviving the reference filter are not generally artifacts of the coarse canonical determinant. Outside $\mathcal I_n$, they are actual endpoint-content factors.

The remaining target is therefore a genuine arithmetic nonalignment estimate for the explicit complete-force congruences (11.1)–(11.2), with higher valuations and collision depth retained.

A sufficient next lemma is:

> **Filtered affine-force gcd lemma.**  
> On an infinite original subsequence, prove
> 

$$
> 2\log H_n^{\rm ref}+\log V_n=o(n\log n),
>
$$


> by controlling the prime powers satisfying the actual reference equations together with the integral Bézout identities (10.1)–(10.2), including the reference-alignment support
> 

$$
> \mathcal I_n=\gcd(F,Q\widehat h-P\widehat\ell)_{>N}.
>
$$


> Any removal of that support must pay its actual depth, not merely declare $F$ invertible.

The present bound


$$
\log\mathcal I_n\le\log(n!)+O(n)
$$


does not discharge that obligation. Nor does the exponentially bounded height of the reference pair control the gcds of its large contact projections with the complete-force affine remainder.

That is the precise obstruction to concluding a uniform small certificate from the new identities.

---

# Final status

| Statement | Status |
|---|---|
| Canonical $3375$ scalar decomposition | Accepted exact finite computation |
| $3375$ reference-filter certificate $\mathcal W^{\rm ref}=1$ | Accepted exact finite target computation |
| All-original $\Theta_n\ne0$, units at $3,5,7$, odd-$15$ binary scalar law | Reused proved results |
| Boundary $p=N$ correction | Explicitly proved |
| Quotient law at odd $p\mid n+1$ | New proof |
| Exact transverse-reference content $\mathcal I_n$ | New proof |
| $\delta_j^{>}\mid\Delta_j\mid\mathcal I_n\delta_j^{>}$ | New infinite-domain theorem |
| $\mathcal W^{\rm ref}/(\delta_0^{>}\delta_3^{>})\mid\mathcal I_n^2$ | New canonical support-and-cost theorem |
| Exact filtered common/exclusive factors away from $\mathcal I_n$ | New theorem |
| Complete-force endpoint Bézout identities | New explicit identities |
| Uniform subfactorial bound for the filtered certificate | Not proved |
| All-original $\mathcal W_n^{\rm ref}=1$ | Neither proved nor disproved |
| Infinite primitive whole forms tending to zero | Not proved |
| Irrationality or rationality of $e+\pi$ | Unresolved |

## Conclusion

The new infinite-family result is the exact support-and-cost statement


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid\mathcal W_n^{\rm ref}
\mid\Delta_{0,n}\Delta_{3,n}
\mid\mathcal I_n^2\delta_0^{>}\delta_3^{>},
\qquad
\mathcal I_n=\gcd(F,Q\widehat h-P\widehat\ell)_{>n+2}.
}
$$



Outside that explicit reference-alignment support, the reference filters recover the actual endpoint cancellation exactly. The accompanying integral Bézout identities retain the complete force and exhibit the affine congruence that surviving primes must satisfy.

What remains missing is a uniform arithmetic bound for those actual surviving prime powers on an infinite original family. The proven alignment cost is still factorial-scale. Even after that arithmetic bottleneck is resolved, an irrationality argument must use the actual all-prime weighted gcd, the actual primitive $q_\lambda$, and a whole nonzero same-index error tending to zero.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}}
$$


