> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — a bounded Newton reduction and an explicit scalar digit transfer

**The new normalized scalar digits are not yet numerically evaluated on the original exponent class, and I do not prove that their zeros align.** I obtain a new reduction that removes the growing-dimensional inverse from this obligation:

* both lifted columns can be reconstructed from signed Newton polynomials of degree at most $260$;
* all factorial blocks and the effect of the cubic inverse are retained;
* these bounded kernels give an explicit finite-state transfer for the **actual norm and mixed digits**, with all higher index digits included.

The transfer below is a proved evaluation procedure, not a claim that its output has already been computed. In particular, I do not assign values to $\delta$ or $\mu$.

Throughout, the original domain is


$$
p=29,\qquad b=3^a,\qquad n=2001b,\qquad
a\ge1,\qquad a\equiv432827\pmod{682892},\qquad m_w=1.
$$


I use the established whole-column divisibilities


$$
Z_w\in p^2\mathbb Z_p^{b+1},\qquad
Y:=V_w/b!\in p^3\mathbb Z_p^{b+1},
$$


and define


$$
\widehat P=Z_w/p^2,\qquad \widehat Q=Y/p^3.
$$


No previous zero $Q$-digit is treated as a parallel vector.

---

## 1. New finite-dimensional closure lemma

Let $U=T(n)$, so


$$
U_{kj}=\binom n{j-k},
$$


with the usual zero convention for a negative lower index. Let


$$
(D_sv)_{j+s}=\binom{j+s}{s}v_j.
$$


On nonnegative indices define


$$
C_s=UD_sU^{-1}.
$$



The exact kernel is


$$
\boxed{
C_s(k,l)=
\sum_{v=0}^{s}
\binom{k}{s-v}\binom nv
\binom{-v}{l-k+s-v}.
}
\tag{1}
$$


Here $\binom 0r=\mathbf1_{r=0}$.

Indeed, the row generating function is


$$
\sum_{l\ge0}C_s(k,l)z^l
=
\frac1{s!}\frac{d^s}{dz^s}
       \bigl(z^k(1+z)^n\bigr)(1+z)^{-n},
$$


and Leibniz’s rule gives (1).

Importantly, the actual finite matrix


$$
\left(
\sum_{s\ge1}d_s
 \binom{j+s}{s}\binom n{j+s-k}
\right)_{0\le k,j<b}T(-n)
$$


is exactly


$$
\left(\sum_{s\ge1}d_s C_s(k,l)\right)_{0\le k,l<b}.
\tag{2}
$$


There is no change of inverse dimension in (2): in the convolution defining its $(k,l)$-entry, the intermediate index is at most $l<b$.

### 1.1 Action on signed Newton polynomials

For a polynomial $h$, write


$$
(\mathcal S_bh)_k=(-1)^kh(k),\qquad 0\le k<b.
$$



Define an operator $\mathscr L_{s,b}$ by its action on the Newton basis:


$$
\begin{aligned}
\mathscr L_{s,b}\binom Xr
={}&
(-1)^s\binom Xs\binom{X-s}{r}\\
&+\sum_{v=1}^{s}(-1)^{s-v}
 \binom X{s-v}\binom nv
 \sum_{i=0}^{r}
 \binom{X-s+v}{r-i}
 \binom{v+i-1}{i}
 \binom{b-1-X+s}{v+i}.
\end{aligned}
\tag{3}
$$



Then


$$
\boxed{
(C_s)_{[0,b)}\,\mathcal S_bh
=
\mathcal S_b(\mathscr L_{s,b}h).
}
\tag{4}
$$


Moreover,


$$
\deg(\mathscr L_{s,b}h)\le \deg h+s,
\tag{5}
$$


and $\mathscr L_{s,b}$ preserves $p$-integral Newton coefficients.

#### Proof of (4)

It suffices to take $h(X)=\binom Xr$. The $v=0$ term of (1) gives the first line of (3).

For $v\ge1$, put $\tau=s-v$. When $k\ge\tau$, set


$$
l=k-\tau+t,\qquad
0\le t\le L:=b-1-k+\tau.
$$


The signs cancel as


$$
(-1)^l\binom{-v}{l-k+\tau}
=
(-1)^{k-\tau}\binom{t+v-1}{v-1}.
$$


Expand


$$
\binom{k-\tau+t}{r}
=
\sum_{i=0}^{r}\binom{k-\tau}{r-i}\binom ti.
$$


The required finite sum is


$$
\begin{aligned}
\sum_{t=0}^{L}
 \binom{t+v-1}{v-1}\binom ti
&=
\binom{v+i-1}{i}
 \sum_{t=0}^{L}\binom{t+v-1}{v+i-1}\\
&=
\binom{v+i-1}{i}\binom{L+v}{v+i}.
\end{aligned}
$$


This is precisely the second line of (3), after extracting $(-1)^k$.

When $k<\tau$, the prefactor $\binom k\tau$ is zero. Thus the same polynomial formula remains valid. The degree bound follows termwise. Every expression in (3) is integer-valued on integers; its Newton coefficients, obtained by finite differences, are therefore integral. ∎

**This closure is the new compression.** Repeated actual contact corrections do not require a length-$b$ vector: at any fixed precision, they act on a bounded Newton coefficient space.

---

## 2. Complete precision inputs and notation

Set


$$
d_s=s![z^s](1-z+z^2/2)^n,\qquad
F_d=\frac{(b+d)!}{b!}.
$$


The established coefficient bound


$$
v_p(d_s)\ge1+v_p((s-1)!)
$$


gives


$$
d_s=0\pmod{p^3}\quad(s\ge59),\qquad
d_s=0\pmod{p^4}\quad(s\ge88).
$$



Since the assigned low digits give


$$
b+2=p^2K,\qquad K\equiv6\pmod p,
$$


the complete factorial tail modulo $p^4$ is $0\le d\le59$. In particular, the block $31\le d\le59$ is retained below with its **actual factorial quotient**, not discarded or replaced by a lower-precision approximation.

The complete logarithmic forcing is zero at this precision for the stated, whole-coefficient reason:


$$
v_p(h_i^F/b!)
\ge
F_n-F_b-\lfloor\log_p(2n+b-1)\rfloor\ge4.
\tag{6}
$$


For example, on this domain,


$$
F_n\ge69b,\qquad F_b\le b/28,\qquad
\lfloor\log_{29}(4003b-1)\rfloor\le b.
$$


Thus (6) concerns the full forcing contribution, not selected summands.

For a cutoff $S$, define the polynomial operator


$$
\mathscr V_S=\sum_{s=1}^{S}d_s\mathscr L_{s,b}.
\tag{7}
$$


By (2)–(4), this is the actual finite contact correction on signed polynomial inputs.

---

## 3. The $P$-lift needs only degree $202$

The original forcing has the exact form


$$
f_i^0=
\frac{(n+i)!}{n!}
\sum_{t=0}^{i}\binom it J_t,
\qquad
J_t=[z^{\,n-t}](1+2z+2z^2)^n.
\tag{8}
$$


For $i\ge87$, the consecutive product in (8) is divisible by $p^3$. Hence define


$$
g_P(X)=
\sum_{i=0}^{86}(-1)^if_i^0\binom Xi
\pmod{p^3}.
\tag{9}
$$


The finite inverse Pascal transform of the complete $P$-forcing is


$$
P_{\rm Pascal}^{-1}f^0=\mathcal S_bg_P\pmod{p^3}.
$$



Now set


$$
\boxed{
h_P=(I-\mathscr V_{58}+\mathscr V_{58}^{\,2})g_P
\pmod{p^3}.
}
\tag{10}
$$


Then


$$
\deg h_P\le86+2\cdot58=202,
\tag{11}
$$


and the actual $P$-solution is


$$
\boxed{
\theta^P=T(-2n)\mathcal S_bh_P\pmod{p^3}.
}
\tag{12}
$$



This retains exactly the inverse precision needed to obtain $Z_w/p^2\bmod p$.

---

## 4. A complete bounded-boundary formula for the $Q$-lift

This is the main new use of the finite boundary.

Define the $60$ boundary coefficients


$$
\boxed{
c_h=\sum_{d=h}^{59}F_d\binom{2n}{d-h},
\qquad 0\le h\le59,
}
\tag{13}
$$


computed modulo $p^4$.

The $s=0$ base solution is


$$
\boxed{
\theta^{Q,\mathrm{base}}_j
=
-\sum_{h=0}^{59}
c_h\binom{-2n}{b+h-j}
\pmod{p^4},
\qquad 0\le j<b.
}
\tag{14}
$$



### 4.1 Derivation of the complete boundary force

Let $e_{\rm tail}=\sum_{d=0}^{59}F_de_{b+d}$, and let


$$
w=U^2e_{\rm tail}.
$$


Its part at indices $l\ge b$ is


$$
w_{\ge b}=\sum_{h=0}^{59}c_he_{b+h}.
$$


The Newton-transformed complete residual is the restriction of


$$
U\left(\sum_{s=0}^{87}d_sD_s\right)Ue_{\rm tail}
\pmod{p^4}.
$$



Eliminating the exterior part of the $s=0$ solution gives the exact combined correction force


$$
F_k^{\rm bdry}
=
\sum_{s=1}^{87}d_s
\sum_{h=0}^{59}c_h C_s(k,b+h)
\pmod{p^4}.
\tag{15}
$$


Thus all exterior indices have been eliminated into $60$ boundary coefficients. They are not additional unknown coordinates.

For $l=b+h>k$, (1) gives


$$
C_s(k,b+h)
=
(-1)^k(-1)^{b+h+s}
\sum_{v=1}^{s}(-1)^v
 \binom k{s-v}\binom nv
 \binom{b+h-k+s-1}{v-1}.
$$


Consequently define


$$
\boxed{
\begin{aligned}
a_Q(X)
={}&
\sum_{s=1}^{87}d_s
\sum_{h=0}^{59}c_h(-1)^{b+h+s}\\
&\quad{}\times
\sum_{v=1}^{s}(-1)^v
 \binom X{s-v}\binom nv
 \binom{b+h-X+s-1}{v-1}.
\end{aligned}}
\tag{16}
$$


Then


$$
F^{\rm bdry}=\mathcal S_ba_Q,\qquad
\deg a_Q\le86,\qquad a_Q\in p\,\operatorname{Int}(\mathbb Z_p)
\pmod{p^4}.
\tag{17}
$$



### 4.2 Where the cubic inverse goes

Set


$$
\boxed{
h_Q=(I-\mathscr V_{87}+\mathscr V_{87}^{\,2})a_Q
\pmod{p^4}.
}
\tag{18}
$$


Then


$$
\deg h_Q\le86+2\cdot87=260.
\tag{19}
$$



The complete solution is


$$
\boxed{
\theta^Q_j
=
-\sum_{h=0}^{59}c_h\binom{-2n}{b+h-j}
+
\bigl(T(-2n)\mathcal S_bh_Q\bigr)_j
\pmod{p^4}.
}
\tag{20}
$$



The absent term $-\mathscr V_{87}^{\,3}a_Q$ is divisible by $p^4$, because $a_Q\in p\operatorname{Int}(\mathbb Z_p)$ and $\mathscr V_{87}$ has a factor $p$.

This is **not** omission of the cubic inverse on the original residual. Rather, the complete cubic inverse has first been combined with the residual into the boundary equation (15). Its remaining cubic action has valuation at least four.

Equations (13), (16), and (18) retain:

* both unit tails;
* the complete $2\le d\le30$ block;
* the new $31\le d\le59$ block;
* every contact term required modulo $p^4$.

---

## 5. Explicit bounded kernels for every coordinate, including the endpoint

Write


$$
h_P(X)=\sum_{r=0}^{202}\alpha_r\binom Xr,\qquad
h_Q(X)=\sum_{r=0}^{260}\beta_r\binom Xr.
$$



For $0\le j<b$, put


$$
\boxed{
\mathcal K_r(j)=
(-1)^j\sum_{t=0}^{r}
 \binom j{r-t}
 \binom{2n+t-1}{t}
 \binom{2n+b-1-j}{b-1-j-t}.
}
\tag{21}
$$


An invalid lower index makes the last binomial zero. Finite summation gives


$$
\mathcal K_r(j)
=
\sum_{l=j}^{b-1}
 \binom{-2n}{l-j}(-1)^l\binom lr.
$$


Thus


$$
\theta^P_j=\sum_{r=0}^{202}\alpha_r\mathcal K_r(j)\pmod{p^3},
\tag{22}
$$




$$
\theta^Q_j=
-\sum_{h=0}^{59}c_h\binom{-2n}{b+h-j}
+\sum_{r=0}^{260}\beta_r\mathcal K_r(j)
\pmod{p^4}.
\tag{23}
$$



Set


$$
\theta^P_{-1}=\theta^P_b=\theta^Q_{-1}=\theta^Q_b=0,\qquad
W_j=\binom{n+2}{j}.
$$


The actual coordinate residues are


$$
z_j=
W_j(j\theta^P_{j-1}-\theta^P_j)\pmod{p^3},
\tag{24}
$$




$$
y_j=
W_j(j\theta^Q_{j-1}-\theta^Q_j)
+W_b\mathbf1_{j=b}\pmod{p^4}.
\tag{25}
$$



Therefore the actual first normalized digits are obtained by the exact divisions


$$
\boxed{
\widehat P_j\bmod p=\frac{z_j}{p^2}\bmod p,\qquad
\widehat Q_j\bmod p=\frac{y_j}{p^3}\bmod p.
}
\tag{26}
$$


These divisions are valid on the original assigned class by its established whole-column divisibility.

In particular, the endpoint is


$$
z_b=W_b\,b\theta^P_{b-1},\qquad
y_b=W_b(1+b\theta^Q_{b-1}),
\tag{27}
$$


not a deleted coordinate.

The only linear algebra remaining in (9)–(23) is on Newton polynomials of degree at most $260$, independent of $b$.

---

## 6. Explicit finite-state transfer for the actual scalar digits

The bounded kernel also permits a genuine digit transfer, rather than a sum over $b+1$ computed coordinates.

Let


$$
D_0=\widehat P^T\widehat P\bmod p,\qquad
M_0=\widehat P^T\widehat Q\bmod p.
\tag{28}
$$



### 6.1 A fully specified binomial transition

Work first modulo $p^4$, and let


$$
L=p^3.
$$


For a polynomial $Q(u,v)$ with constant term one, define the section operator


$$
\Lambda_{a,c}
  \left(\sum_{i,j}A_{ij}u^iv^j\right)
=
\sum_{i,j}A_{pi+a,pj+c}u^iv^j.
$$



A state is a polynomial $S$, representing $S/Q^L$. For input digits $a,c$, define


$$
\boxed{
S\longmapsto
\Lambda_{a,c}\!\left(SQ^{(p-1)L}\right)\pmod{p^4}.
}
\tag{29}
$$


The initial state is $Q^{L-1}$; the terminal output is $S(0,0)$.

The proof is the congruence


$$
Q(u,v)^{pL}\equiv Q(u^p,v^p)^L\pmod{p^4}.
$$


Hence


$$
\Lambda_{a,c}\left(\frac S{Q^L}\right)
=
\frac{\Lambda_{a,c}(SQ^{(p-1)L})}{Q^L}
\pmod{p^4}.
$$



For


$$
Q_{\rm bin}=1-u-uv,
$$


the output on the digit pairs of $A,B$ is


$$
[u^Av^B]Q_{\rm bin}^{-1}=\binom AB\pmod{p^4}.
$$


For


$$
Q_{\rm cen}=1-u(1+2v+2v^2),
$$


the output on the digit pairs of $n,n-t$ is the original coefficient $J_t$ in (8).

This is a finite-state construction: the degree bounds


$$
\deg_u S\le L\deg_uQ,\qquad
\deg_v S\le L\deg_vQ
$$


are preserved by (29), and all coefficients lie in a finite ring.

### 6.2 Affine-index carries

All large binomial indices in (21)–(25) are affine forms


$$
A=\lambda b+\varepsilon j+c,
\qquad
0\le\lambda\le4003,\quad
\varepsilon\in\{-1,0,1\},
$$


with bounded $c$.

If $d,z$ are the next digits of $b,j$, respectively, the exact carry transition is


$$
\boxed{
a\equiv \kappa+\lambda d+\varepsilon z\pmod p,\qquad
\kappa'=
\left\lfloor
\frac{\kappa+\lambda d+\varepsilon z}{p}
\right\rfloor,
}
\tag{30}
$$


starting at $\kappa=c$.

For these kernels one may uniformly use


$$
-5000\le\kappa\le5000.
$$


This interval is preserved by (30). Negative lower indices are detected by their terminal carry and assigned binomial value zero.

The largest required small lower index is $260<p^2$. Thus all small-lower binomials modulo $p^4$ depend only on their upper index modulo $p^5$. Indeed,


$$
\binom{x+p^5}{r}-\binom xr
=
\sum_{i=1}^{r}\binom{p^5}{i}\binom{x}{r-i}
\equiv0\pmod{p^4}
\quad(0\le r\le260),
\tag{31}
$$


because $v_p\binom{p^5}{i}=5-v_p(i)\ge4$.

Accordingly, the state also stores $b,j\bmod p^5$, their parities, and the finite comparison data for


$$
0\le j\le b,\qquad j=0,\qquad j=b.
$$


The $87$ central coefficients $J_t$ are obtained from (29); they are not replaced by their low-digit approximations.

### 6.3 Transition matrices and terminal contractions

Let $\Sigma$ be the finite product state consisting of:

1. the section states for the large binomials in (21)–(25);
2. the section states for $J_0,\ldots,J_{86}$;
3. the affine carries (30);
4. the bounded residue, parity, and comparison registers.

There are at most $643$ large-binomial instances needed: two arguments $j,j-1$ for each of the $261$ boundary binomials in (21), two for each of the $60$ terms in (23), and the weight. This is independent of $b$.

Let $\mathcal T_{d,z}$ be the explicitly defined combined transition. Define matrices over $\mathbb F_p$ by


$$
\boxed{
\mathsf M_d(\sigma,\sigma')
=
\#\{z\in\{0,\ldots,p-1\}:
 \mathcal T_{d,z}(\sigma)=\sigma'\}\pmod p.
}
\tag{32}
$$



At a terminal state:

* reject unless $0\le j\le b$;
* build $\alpha_r,\beta_r,c_h$ from its stored parameter residues and central coefficients using (9)–(18);
* evaluate (21)–(25);
* take the digits in (26).

Define terminal output functions


$$
w_D(\sigma)=
(\widehat P_j\bmod p)^2,\qquad
w_M(\sigma)=
(\widehat P_j\bmod p)(\widehat Q_j\bmod p).
\tag{33}
$$


Rejected states have output zero.

If $b=(d_0,\ldots,d_{\ell-1})_p$, append four zero digits. With $v_0$ the initial-state row vector, the exact scalar transfer is


$$
\boxed{
\begin{aligned}
D_0&=
v_0\mathsf M_{d_0}\cdots
 \mathsf M_{d_{\ell-1}}\mathsf M_0^4\,w_D,\\
M_0&=
v_0\mathsf M_{d_0}\cdots
 \mathsf M_{d_{\ell-1}}\mathsf M_0^4\,w_M.
\end{aligned}}
\tag{34}
$$


Four padding digits suffice for all nonnegative affine indices here. Every accepted path corresponds to exactly one $j\in[0,b]$.

Equation (34) follows by summing the terminal coordinate outputs over all digit paths. Thus it computes the actual weighted contractions—not a Boolean support condition—and processes every higher digit.

### What (34) does and does not establish

This is a **proved bounded-state scalar recurrence**, with specified transitions and outputs. It is not a practically minimized automaton: the generic section-state bound is very large.

I have **not evaluated** the product (34), nor proved an invariant of its reachable states that forces


$$
M_0=(6C_n)^{-1}D_0
\quad\text{or}\quad
(D_0=0\iff M_0=0).
$$


Consequently it would be incorrect to label either scalar “computed” merely because (34) now gives a bounded recurrence.

---

## 7. The precise alignment obstruction after this reduction

Put


$$
\widehat D=\widehat P^T\widehat P,\qquad
\widehat M=\widehat P^T\widehat Q,\qquad
c=(6C_n)^{-1}.
$$


The scalar whose evaluation is still needed at the present layer is


$$
\boxed{
\widehat M-c\widehat D
=
\sum_{j=0}^{b}
\widehat P_j(\widehat Q_j-c\widehat P_j).
}
\tag{35}
$$


Its residue is obtained from (34) by the terminal output $w_M-cw_D$.

The bounded-boundary reduction identifies exactly where a defect may enter:

* the $60$ coefficients $c_h$, including the new factorial block;
* the boundary polynomial $a_Q$;
* its two subsequent contact actions in (18);
* the complete $P$-correction polynomial (10);
* the endpoint (27).

None is shown to vanish in (35). In particular, the whole-column transfer already established at the previous layer does not imply a Gram-divisibility statement here.

If $D_0\ne0$, then $\delta=0$; if $M_0\ne0$, then $\mu=0$. If either first digit vanishes, its valuation remains a further-depth question. I obtain no unconditional relative bound for $\mu-\delta$ from the present reduction.

---

## 8. Actual least denominator, final gcd, and whole error

Retain the actual least two-column lift denominator $d_B$, not a row-clearer or determinant substitute:


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


With the actual factorial metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
$$



Define


$$
\delta=v_{29}(\widehat D),\qquad
\mu=v_{29}(\widehat M).
$$


The norm is positive. Finiteness of the mixed valuation retains the supplied original-family $3$-adic nonvanishing dependency.

The exact identities remain


$$
\boxed{
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
}
\tag{36}
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
}
\tag{37}
$$



At the supplied dependency status of the complete signed-rate theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)>0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n+o(n).
$$


Thus the whole primitive evaluated error is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n<0
\quad\text{eventually}.
}
\tag{38}
$$


All other prime contributions remain in $q_n$. The new local compression supplies no global denominator-rate conclusion and no irrationality conclusion.

---

# Concluding ledger

## (1) New result and proof status

**Proved here:**

* The explicit signed-Newton closure operator (3) for the actual finite contact correction.
* A degree-$202$ reduction for the actual $P$-lift modulo $29^3$.
* A degree-$260$, $60$-boundary-coefficient reduction for the complete $Q$-lift modulo $29^4$.
* The reduction retains the new factorial block, the effect of the cubic inverse, and the endpoint.
* The explicit bounded-state scalar recurrence (29)–(34) for
  

$$
\widehat P^T\widehat P\bmod29,\qquad
  \widehat P^T\widehat Q\bmod29,
$$


  with unrestricted higher digits.

**Not proved or computed:** the values of these two digits on the original exponent class, their zero alignment, a relative valuation bound, or irrationality/rationality of $e+\pi$.

## (2) Exact remaining bottleneck

The immediate missing step is evaluation or a reachable-state invariant for (34), after the fixed low digits


$$
(27,28,5,28)_{29}.
$$


In particular, one must determine the terminal scalar defect


$$
M_0-(6C_n)^{-1}D_0
$$


on norm-zero states—not merely on unit-norm auxiliary examples.

Even a first-digit alignment theorem would leave further valuation depth and the global primitive denominator unresolved.

## (3) Bounded computation request

A useful audit of the **new compression**, rather than another original precision-four run, is:

**Inputs:** the already computed auxiliary pair


$$
(n,b,p)=(1678839,839,29),
$$


with the original forcing coefficients, using (9)–(25) instead of the length-$839$ inverse.

**Expected verifiable output:** equality with all $840$ entries of the existing certificate:


$$
Z_w/29\bmod841,\qquad Y/29^2\bmod841.
$$


Useful coordinate checks extracted from that certificate are


$$
\begin{array}{c|rrrrrr}
j&0&1&2&27&28&839\\ \hline
Z_{w,j}/29\bmod841&201&207&85&754&377&377\\
Y_j/29^2\bmod841&514&129&596&533&464&578.
\end{array}
$$


This tests the new bounded polynomial operators and complete boundary elimination. It does **not** test alignment at a vanishing normalized norm and would prove no infinite assertion.
