> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 18 — Exact first-kernel reductions and the obstruction to an unrestricted integral moment module

## Executive conclusion

The two finite binomial transforms can be reduced explicitly on the first-force coordinate kernels, the $s=t=0$ mixed kernel, and the symbolic boundary polynomials. The actual reconstruction weights can also be retained in exact, boundary-aware rational coefficient representations.

These calculations establish a useful first algebraic gate, but **not the requested original norm/mixed certificate at $M\ge20$**. In particular:

1. The unweighted $s=t=0$ mixed kernel has a particularly simple finite Pascal transform:
   

$$
\sum_{i=0}^{j}(-1)^{j-i}\binom ji\binom{2n+i}{b}
   =\binom{2n}{b-j}.
$$


2. After multiplication by the actual $W_j^2$, this reduction becomes a multivariate coefficient extraction. Its exact representation is given below, including the finite upper boundary of the other binomial transform.
3. An unrestricted, characteristic-zero integral module closed under multiplication by $W_j^2$ and containing the transformed zeroth first-force coordinate kernel necessarily has rank at least $b$. Thus the proposed **exact integral finite-basis closure**, if interpreted without reduction modulo $2^M$, cannot have precision-sized rank.
4. This rank obstruction does **not** disprove a precision-dependent quotient over $\mathbb Z/2^M\mathbb Z$. Such a quotient remains the necessary next step; the rational representations below do not themselves prove that it is small or computationally feasible at an original index.

The report therefore gives exact reductions and a specific closure obstruction, but it does not claim completion of the fixed-precision closure problem. The unresolved issue is now narrower: construct and bound a **specialized modular coefficient-extraction state space for the actual weighted channels**, rather than an unrestricted exact integral moment module.

No tools were used. No new numerical residues are claimed.

---

## 1. Domain and accepted scope

The original family remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The contact coordinates are $0\le i,j<b$, and the reconstructed coordinates are $0\le j\le b$.

Writing


$$
b=128D+81,
$$


the contact blocks remain:

- $0\le t<D,\ 0\le\rho<128$;
- $t=D,\ 0\le\rho\le80$;
- the separate reconstructed endpoint $j=b$.

Set


$$
N_0=n+2,\qquad W_j=\binom{N_0}{j}.
$$


The subscript on $N_0$ distinguishes the binomial upper parameter from the norm $N$.

The accepted normalization is


$$
\mathsf a=2X=\mathcal RA^{-1}f,\qquad
\mathsf b=4Y=\mathcal RA^{-1}r+W_be_b,
$$


where


$$
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
$$


The actual scalar outputs are


$$
D_{\rm raw}:=\mathsf a^T\mathsf a=4N,\qquad
E_{\rm raw}:=\mathsf a^T\mathsf b=8H.
$$



A4turn19 accepts the finite band-plus-boundary adjoint identities. The supplied coordinator receipt certifies the stated two auxiliary systems modulo $8192$, including their 315 high-moment comparisons apiece. It does not certify an original-family output.

The divided-power inverse in Turn 17 follows algebraically from the stated symbol filtration: the convolution recurrence there is integral, and its valuation induction is valid. That result compresses the interior contact operator, not the complete scalar calculation.

---

## 2. Notation for the two kernel transforms

For a contact kernel $\kappa$, define


$$
(\mathcal T_U\kappa)(i)
=
\sum_{j=i}^{b-1}\kappa(j)\binom{-n}{j-i},
\tag{2.1}
$$


and


$$
(\mathcal T_L\kappa)(j)
=
\sum_{i=0}^{j}(-1)^{j-i}\binom ji\kappa(i).
\tag{2.2}
$$



These are precisely the functional transfers induced by $U^{-T}$ and $L^{-T}$. Their different finite endpoints matter:

- $\mathcal T_L$ has an upper endpoint equal to its output index;
- $\mathcal T_U$ retains the original upper contact endpoint $b-1$.

All coefficient identities below are identities over the integers. They therefore remain valid after reduction modulo $2^M$, with no factorial division.

---

## 3. Actual first-force coordinate kernels

The norm contraction is


$$
D_{\rm raw}=w^Tf,
\qquad w=A^{-T}\mathcal R^T\mathsf a.
$$


The accepted factorial budget allows


$$
D_{\rm raw}\equiv
\sum_{\ell<\min(b,I_M)}f_\ell w_\ell\pmod{2^M}.
$$



Thus the relevant small first-force kernels are the coordinate kernels


$$
\delta_\ell(j)=\mathbf1_{j=\ell},
$$


with their **actual coefficients $f_\ell$**. This is a decomposition of the actual truncated force, not a replacement by a test force.

### Proposition 1 — Both transforms on a coordinate kernel

For $0\le\ell<b$,


$$
\boxed{
(\mathcal T_U\delta_\ell)(i)
=
\mathbf1_{i\le\ell}\binom{-n}{\ell-i},
}
\tag{3.1}
$$


and


$$
\boxed{
(\mathcal T_L\delta_\ell)(j)
=
\mathbf1_{j\ge\ell}(-1)^{j-\ell}\binom j\ell.
}
\tag{3.2}
$$



These follow immediately by selecting the single nonzero summand.

In particular, the actual zeroth coordinate channel gives


$$
\mathcal T_U(f_0\delta_0)=f_0\delta_0,
\qquad
\mathcal T_L(f_0\delta_0)(j)=f_0(-1)^j.
\tag{3.3}
$$



The actual first coordinate channel gives


$$
(\mathcal T_U(f_1\delta_1))(i)
=
f_1
\begin{cases}
-n,&i=0,\\
1,&i=1,\\
0,&i\ge2,
\end{cases}
\tag{3.4}
$$


and


$$
(\mathcal T_L(f_1\delta_1))(j)
=f_1(-1)^{j-1}j.
\tag{3.5}
$$



There is no long finite sum in these reductions. They also show exactly where a small first-force support becomes a dense polynomial-sign kernel.

### Cutoff at $M=20$

The budget alone gives


$$
I_{20}=48:
$$


indeed,


$$
v_2(23!)=19,\qquad v_2(24!)=22.
$$


Hence the actual norm force may be retained through index $47$ at absolute precision $2^{20}$. This does not imply that the corresponding adjoint entries are already evaluable.

---

## 4. Complete $s=t=0$ mixed-kernel reduction

For the lowest mixed channel, retain the genuine kernel


$$
K(j)=\binom{2n+j}{b},
\qquad 0\le j<b.
\tag{4.1}
$$


“Complete” here means that the finite range and the lower index $b$ are retained. This channel is not the entire mixed force.

### Proposition 2 — Finite Pascal reduction



$$
\boxed{
(\mathcal T_LK)(j)=\binom{2n}{b-j}.
}
\tag{4.2}
$$



**Proof.** Since


$$
K(i)=[z^b](1+z)^{2n}(1+z)^i,
$$


the finite binomial theorem gives


$$
\begin{aligned}
(\mathcal T_LK)(j)
&=[z^b](1+z)^{2n}
  \sum_{i=0}^{j}\binom ji(-1)^{j-i}(1+z)^i\\
&=[z^b](1+z)^{2n}z^j\\
&=\binom{2n}{b-j}.
\end{aligned}
$$


This preserves the original lower index before evaluation. ∎

### Proposition 3 — Boundary-aware rational reduction of the other transform

Put $B_i=b-1-i$. Then


$$
\boxed{
(\mathcal T_UK)(i)
=
[z^b y^{B_i}]
\frac{(1+z)^{2n+i}}
{(1-y)\bigl(1+(1+z)y\bigr)^n}.
}
\tag{4.3}
$$



**Proof.** For any indeterminate $X$,


$$
\sum_{k=0}^{B}\binom{-n}{k}X^k
=
[y^B]\frac{(1+Xy)^{-n}}{1-y}.
\tag{4.4}
$$


Apply this with $X=1+z$, after writing $j=i+k$ in (2.1). ∎

The factor $(1-y)^{-1}$ is essential. It records the finite partial sum ending at $b-1$. Replacing (4.3) by evaluation of the infinite binomial series at $y=1$ would change the finite matrix problem.

Equation (4.3) is a rational coefficient representation, not yet a small-state evaluation algorithm.

---

## 5. The actual squared and adjacent weights

The weights cannot be treated as bounded-degree polynomials in $j$. A convenient exact representation uses constant terms.

For fixed shifts $a,c$, define


$$
\Phi_{a,c}(u,v)
=(1+u)^{N_0}(1+v)^{N_0}u^{-a}v^{-c}.
$$


Then


$$
\boxed{
W_{j+a}W_{j+c}
=
\operatorname{CT}_{u,v}
\Phi_{a,c}(u,v)(uv)^{-j}.
}
\tag{5.1}
$$


This uses the ordinary convention that binomial coefficients outside their valid nonnegative range vanish.

In particular:

- $a=c=0$ gives $W_j^2$;
- $a=0,c=1$ gives $W_jW_{j+1}$;
- $a=c=1$ gives $W_{j+1}^2$.

All three are available without dividing by $j+1$, $N_0-j$, or another potentially nonunit quantity.

### 5.1 Weighted mixed channel: both transforms

Define


$$
K_{a,c}(j)=W_{j+a}W_{j+c}\binom{2n+j}{b},
$$


and set


$$
X=\frac{1+z}{uv}.
$$


Then


$$
K_{a,c}(j)
=
[z^b]\operatorname{CT}_{u,v}
\Phi_{a,c}(u,v)(1+z)^{2n}X^j.
\tag{5.2}
$$



The two exact reductions are


$$
\boxed{
(\mathcal T_LK_{a,c})(j)
=
[z^b]\operatorname{CT}_{u,v}
\Phi_{a,c}(u,v)(1+z)^{2n}(X-1)^j,
}
\tag{5.3}
$$


and


$$
\boxed{
(\mathcal T_UK_{a,c})(i)
=
[z^b y^{b-1-i}]\operatorname{CT}_{u,v}
\frac{\Phi_{a,c}(u,v)(1+z)^{2n}X^i}
{(1-y)(1+Xy)^n}.
}
\tag{5.4}
$$



**Proof.** Apply the finite binomial theorem to $X^j$ for (5.3), and (4.4) for (5.4), before taking the indicated coefficients. Every sum being interchanged is finite at the required coefficient. ∎

Thus the first weighted mixed gate has an exact rational representation with four coefficient variables $u,v,z,y$. The finite endpoint is explicit.

This is more information than introducing a new named unevaluated binomial sum. Nevertheless, it is not a claim that the associated modular coefficient-extraction state space has feasible dimension.

### 5.2 Polynomial factors and the actual reconstruction matrix

If a channel includes a polynomial factor $P(j)$, introduce an independent variable $X$ and use


$$
P(\Theta_X)X^j=P(j)X^j,
\qquad \Theta_X=X\frac{d}{dX},
$$


before substituting the required expression for $X$.

This handles the actual factors $j$, $j+1$, and their squares integrally.

In contact coordinates,


$$
Q:=\mathcal R^T\mathcal R=C^T\operatorname{diag}(W_j^2)C
$$


has entries


$$
\boxed{
Q_{ii}=W_i^2+(i+1)^2W_{i+1}^2,
}
\tag{5.5}
$$


and


$$
\boxed{
Q_{i,i+1}=Q_{i+1,i}=-(i+1)W_{i+1}^2
\quad(0\le i<b-1).
}
\tag{5.6}
$$


All other entries vanish.

At $i=b-1$, the diagonal term is


$$
W_{b-1}^2+b^2W_b^2.
$$


That final contribution must not be dropped.

Equations (5.5)–(5.6) identify the actual norm weights. Adjacent products $W_jW_{j+1}$, when used in another intermediate representation, are covered by (5.1); they must not be substituted for the squared weights in $Q$.

---

## 6. Exact boundary-polynomial pairings

The divided-power endpoint corrections are linear combinations of


$$
P_h(x)=(x-1)^h,
\qquad b-m\le h\le b-1,
$$


with the valid range shortened when necessary. Their coefficient vectors are


$$
p_h(j)=
\begin{cases}
(-1)^{h-j}\binom hj,&0\le j\le h,\\
0,&j>h.
\end{cases}
$$



For any contact kernel $\kappa$,


$$
\boxed{
\sum_{j=0}^{b-1}\kappa(j)p_h(j)
=(\mathcal T_L\kappa)(h).
}
\tag{6.1}
$$


Consequently, the weighted mixed boundary pairing is evaluated symbolically by


$$
\boxed{
\sum_{j=0}^{h}
(-1)^{h-j}\binom hj
W_{j+a}W_{j+c}\binom{2n+j}{b}
=
[z^b]\operatorname{CT}_{u,v}
\Phi_{a,c}(u,v)(1+z)^{2n}(X-1)^h.
}
\tag{6.2}
$$



For the actual squared-weight boundary pairing without the mixed factor,


$$
\boxed{
\sum_{j=0}^{h}
(-1)^{h-j}\binom hj W_j^2
=
\operatorname{CT}_{u,v}
(1+u)^{N_0}(1+v)^{N_0}
\left(\frac1{uv}-1\right)^h.
}
\tag{6.3}
$$



### Pairing two boundary polynomials

A potentially necessary boundary Gram entry is


$$
\mathcal B_{h,k}
=
\sum_{j=0}^{\min(h,k)}
W_j^2\,p_h(j)p_k(j).
$$


Its exact reduction is


$$
\boxed{
\mathcal B_{h,k}
=
(-1)^{h+k}
[t^k]\operatorname{CT}_{u,v}
(1+u)^{N_0}(1+v)^{N_0}
(1+t)^k
\left(1+\frac{t}{uv}\right)^h.
}
\tag{6.4}
$$



Indeed,


$$
[t^k](1+t)^k(1+Xt)^h
=
\sum_j\binom hj\binom kj X^j.
$$


Inserting $X=(uv)^{-1}$ and applying (5.1) proves (6.4).

Adjacent-weight and polynomially weighted versions follow by replacing $\Phi_{0,0}$ with $\Phi_{a,c}$ and applying the indicated Euler operators. This retains the actual large degrees $h,k$; they have not been replaced by small proxy indices.

---

## 7. A specific closure obstruction: exact integral rank grows with $b$

The preceding formulas do not justify an unrestricted small integral kernel module. In fact, that interpretation is impossible.

### Theorem 4 — Squared-weight multiplication forces full characteristic-zero rank

Fix an original pair $(b,n)$. Let $V\subseteq\mathbb Q^b$ be a vector space that:

1. contains the kernel $v(j)=(-1)^j$;
2. is closed under multiplication by $W_j^2$.

Then


$$
\boxed{\dim_{\mathbb Q}V=b.}
\tag{7.1}
$$



The same conclusion applies to a torsion-free integral kernel module after tensoring with $\mathbb Q$. It also applies if $v$ is replaced by any nonzero scalar multiple, including an actual nonzero $f_0v$.

**Proof.** Let


$$
d_j=W_j^2.
$$


Because $N_0=n+2=4002b+2$, the binomial coefficients


$$
\binom{N_0}{j},\qquad0\le j<b,
$$


are strictly increasing: their successive ratio is


$$
\frac{N_0-j}{j+1}>1.
$$


Thus the $d_j$ are pairwise distinct.

Closure under weight multiplication puts


$$
v,\quad dv,\quad d^2v,\quad\ldots,\quad d^{b-1}v
$$


in $V$. Their coordinate matrix has determinant


$$
\left(\prod_{j=0}^{b-1}(-1)^j\right)
\prod_{0\le i<j<b}(d_j-d_i),
$$


which is nonzero. Therefore these $b$ vectors are linearly independent. ∎

### Scope of the obstruction

This is a different obstruction from the already-settled ordinary-jet failure.

It rules out a rank-$\operatorname{poly}(M)$ **exact characteristic-zero module**, uniformly in $b$, if that module is required to contain these channels and be closed under unrestricted repeated multiplication by the actual squared weights.

It does **not** rule out:

- a module defined only modulo $2^M$;
- a representation permitting only the bounded number of weight multiplications required by the actual computation;
- a straight-line rational-expression representation;
- a small quotient tailored to the two final outputs.

The Vandermonde determinant above can have large binary valuation. It is therefore invalid to reduce this proof modulo $2^M$ and assert the same rank lower bound.

This distinction is decisive. The exact integral closure proposal is too broad; the fixed-precision output closure is still open.

---

## 8. A narrower alternative, and what is still missing

A concrete replacement is to retain a **bounded-operation coefficient representation**, rather than close under arbitrary products.

For the first gate, the required records are:

1. a rational Laurent expression such as (5.3), (5.4), or (6.4);
2. its coefficient target;
3. its expansion convention;
4. bounded shift labels $a,c,s,t$;
5. the finite-boundary target $b-1-i$;
6. its binary coefficient modulus.

The formulas above give these records explicitly. They avoid a length-$b$ expanded row at this stage.

However, an expression with a bounded number of variables is not automatically a feasible original-index algorithm. For example,


$$
(1+Xy)^{-n}
$$


has a parameter-dependent denominator exponent. A generic finite-ring rational-series theorem cannot be invoked as if its state dimension were independent of that exponent and of the remaining coefficient targets.

### Concrete follow-on lemma

The next sufficient lemma is:

> **Specialized modular weighted-extraction lemma.**  
> For the rational expressions (5.3), (5.4), and (6.4), and their bounded-shift divided-power descendants arising from the accepted $m=4(M-1)$ contact factor and boundary Schur correction, construct an explicit coefficient-extraction state system over $\mathbb Z/2^M\mathbb Z$. Prove a numerical bound for its reachable state dimension at $M=20$, including the actual binary digits of $n,b,h,k$, and prove that all integral transfer operations preserve the stated expansion conventions and finite endpoints.

A general assertion that such a rational series has some finite representation is insufficient. The required result must give the reachable dimension and actual integral transition operators for these expressions.

The present report does not prove that lemma. Therefore it would be incorrect to label the complete kernel-closure gate or the original scalar computation as passed.

---

## 9. Complete force, logarithmic budget, and the exterior endpoint

The normalized exponential force remains


$$
r_i^e\equiv
\sum_{\substack{a,t\ge0\\a+v_2(t!)<M}}
\sum_{s=0}^{4a}
\lambda_s^{(a)}
\binom{n+i}{s}
t!\binom{b+t}{t}
\binom{2n+i-s}{b+t}
\pmod{2^M},
\tag{9.1}
$$


with all original valid-term guards retained.

The $s=t=0$ calculation above evaluates the transform structure of one actual channel. It does not authorize deleting the other channels in (9.1).

The complete logarithmic term may be omitted only if


$$
M\le K_{\rm norm}
=
1+v_2((n/2)!)-v_2(b!)
-\lfloor\log_2(2n+b-1)\rfloor.
\tag{9.2}
$$


Otherwise the exact contribution


$$
\sum_{i=0}^{b-1}w_i\,\frac{h_i^F}{b!}
$$


must be added.

The original exterior $+1$ is retained through the exact normalization identity


$$
\mathcal R(j!)_{0\le j<b}=-e_0+b!W_be_b.
$$


Accordingly,


$$
\boxed{
D_{\rm raw}=w^Tf,\qquad
E_{\rm raw}=w^Tr+W_b\mathsf a_b.
}
\tag{9.3}
$$


Neither a boundary-polynomial reduction nor a mixed-kernel identity removes $W_b\mathsf a_b$.

---

## 10. Norm-sensitive precision

Let


$$
a=\min_jv_2(\mathsf a_j),\qquad
c=\min_jv_2(\mathsf b_j),
$$


and


$$
d=v_2(D_{\rm raw}),\qquad e=v_2(E_{\rm raw}).
$$



Since


$$
\frac HN=\frac{E_{\rm raw}}{2D_{\rm raw}},
$$


relative precision $2^s$ requires, sufficiently,


$$
M_E\ge s+d+1,\qquad
M_D\ge s+2d+1-e,
$$


with $M_E>e$, $M_D>d$.

The assignment additionally requires


$$
M\ge2\mu+6,
$$


so the smallest original target begins at $M=20$, before extra norm cancellation is paid.

If a first-column replacement has coordinate error depth $T$, the correct budgets are:

- squared approximate norm:
  

$$
\min(T+a+1,2T);
$$


- one-sided adjoint norm using the exact force:
  

$$
T+a;
$$


- mixed contraction against the exact second column:
  

$$
T+c.
$$



No exact valuation may be assigned to a raw output that is merely zero at the working modulus.

---

## 11. Bounded exact arithmetic proposed for inspection

The previous auxiliary adjoint audit is already supplied as passed. The following is a different, narrowly scoped audit of the new weighted reductions.

### Inputs

Use


$$
(b,n)=(81,324162),\qquad(209,836418),
$$


and modulus $2^{20}$.

These remain auxiliary systems. No complete force regeneration is needed for this kernel-only test.

Use:

- first-force coordinate labels $\ell=0,1$;
- weight shifts
  

$$
(a,c)=(0,0),(0,1),(1,1);
$$


- every contact output index;
- boundary degrees
  

$$
h,k\in\{b-2,b-1\}.
$$



### Comparisons

1. Compare direct matrix transforms of $\delta_0,\delta_1$ with (3.1)–(3.5).
2. Compare direct transforms of $\binom{2n+j}{b}$ with (4.2)–(4.3).
3. Compare direct transforms of
   

$$
W_{j+a}W_{j+c}\binom{2n+j}{b}
$$


   with (5.3)–(5.4).
4. Compare the direct weighted boundary pairings with (6.2)–(6.4).
5. Check (5.5)–(5.6) directly from the $(b+1)\times b$ reconstruction matrix, especially
   

$$
Q_{b-1,b-1}=W_{b-1}^2+b^2W_b^2.
$$



The coefficient expressions should be evaluated independently using only the finite coefficient ranges requested by each identity. Their degrees need not be expanded through $n$.

### Expected verifiable output

Every difference is zero modulo $2^{20}$. The receipt should report the number of comparisons and explicitly identify the endpoint diagonal comparison.

These checks verify the new reductions at their finite scope. They neither predict new auxiliary norm residues at $2^{20}$ nor provide an original-family certificate.

For an original-index calculation, the indispensable additional output is still an explicit bounded state list and transition system for the lemma in Section 8. No such list is supplied here.

---

## 12. Final gcd, primitive denominator, and whole error

The final arithmetic remains unchanged:


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B},
$$


where $d_B$ is the least actual two-column clearer and


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}\ne0
$$


at the accepted scope.

The primitive multiplier is


$$
\frac{d_B^2}{g_B}.
$$


Every prime in the gcd is included.

The binary denominator interface remains


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\},
$$


where $\alpha=v_2(N)$ and $\gamma=v_2(H)$. The kernel identities do not establish an original-family value of $\gamma-\alpha$.

Under the accepted complete signed-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
$$


eventually, and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The relevant evaluated form is the whole quantity


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
$$


eventually.

Irrationality by this route still requires a same-index bound forcing this entire nonzero quantity to tend to zero. A binary kernel calculation alone does not supply the required all-prime primitive-denominator estimate.

---

## Conclusion and proof-status ledger

| Item | Status |
|---|---|
| Both transforms on the actual first-force coordinate channels | Proved |
| Finite Pascal reduction of the $s=t=0$ mixed kernel | Proved |
| Boundary-aware rational representation of its other transform | Proved |
| Both transforms with actual $W_j^2$ and adjacent weights | Exact coefficient representations proved |
| Weighted boundary-polynomial and boundary-pair pairings | Proved |
| Unrestricted characteristic-zero integral closure of precision-sized rank | Ruled out by the squared-weight rank theorem |
| Precision-sized closure modulo $2^M$ | Open |
| Feasible complete original calculation at $M\ge20$ | Not established |
| Original relative-output law after full norm cancellation | Not established |
| All-prime primitive-denominator and whole-error bound | Open |

The new result is an exact first-layer reduction of the requested weighted kernels and boundary pairings, together with a rank obstruction showing why an unrestricted exact integral kernel module is the wrong closure target.

The exact remaining mathematical bottleneck is a **feasibly bounded modular state representation for these specific rational coefficient extractions under the actual finite adjoint and boundary operations**. It must evaluate both raw outputs, certify their first nonzero digits, and pay the full norm loss. Beyond that remains the full gcd and primitive-denominator comparison.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


