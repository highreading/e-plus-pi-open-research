> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 20: Independent audit of the higher corrected cofactors and the all-order contact-jet filter

## 1. Verdicts and scope

### Audit I — A2turn12 cofactor recursion

**PASS, at the stated original indices and with the complete corrected pencil retained.**

The following claims are valid:

- the exact weighted contact-jet identity (4.3), including its shifts, factorials and odd factor;
- the exact binary valuations of all normalized atom jets;
- the low-order contact-jet evaluation, **only under $r+j<16$**;
- the uniform source-minor lower divisor and its attainment for the three selected source sets;
- the complete corrected common-column content valuations
  

$$
19,\qquad 39,\qquad 72;
$$


- the successive residual pivot depths
  

$$
13,\qquad 19,\qquad 32;
$$


- every Cramer division and subsequent row division, including both affine coefficient borders;
- the column-permutation signs and exact all-prime coefficient transfers;
- the identities
  

$$
\nu_k=64+\nu_k^{[5]},
  \qquad
  v_2(G_k)=\chi_k+64+\nu_k^{[5]},
$$


  with the actual primitive denominator and whole evaluated error unchanged.

The general corrected-cofactor criterion also passes, but **only with its source-unit hypothesis and its strict precision hypothesis $t_q<L_d$**. Neither hypothesis may be omitted.

### Audit II — parent all-order $\mathbb F_4$ formula and two-carry algorithm

**PASS, as a formula and algorithm for the normalized contact-jet parity.**

The derivation is valid without $r+j<16$. In particular:

- the extension of the finite sum by zero is legitimate;
- the trace descriptions of $\theta$ and the contact sequence are correct;
- the characteristic-two derivative term has the stated factor;
- both coefficient extractions are correct;
- the weighted two-carry rule has the correct exponent signs;
- zero digits have unique zero choices;
- one additional all-zero digit suffices to kill a remaining carry;
- the final trace returns the required element of $\mathbb F_2$;
- the complexity is logarithmic in the input sizes, and therefore $O(\log d)$ for jets used inside the original finite source matrix.

This is **not** a compact determinant or inverse algorithm. It does not prove a growing source-unit flag, justify discarding visible bottom corrections, or bound the joint terminal coefficient depth.

### Status corrections, not mathematical repairs

The “different audit pending” labels concerning turn11 and turn10 in the attached historical reports are superseded by the coordinator’s gate. Both constructions are established reuse here. I do not repeat their full proofs.

No mathematical repair is needed to the two new principal results audited here. Several tempting extensions fail; their exact obstructions and the corresponding usable statements are recorded below.

The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 2. Original objects and the exact reused interface

### 2.1 Domain and index conventions

Throughout,


$$
\mathcal K=\{9^{18+32u}:u\ge0\},
\qquad k\in\mathcal K,
\qquad d=k-1.
$$


The original-domain facts are


$$
v_2(d)=4,\qquad d\equiv2\pmod3,\qquad d\ge64.
$$


No auxiliary value of $d$ replaces this domain.

We distinguish:

- $n$: a top-source row index, $0\le n<d$;
- $i$: a residual row index, $0\le i<d+2$, representing the original physical row
  

$$
m=d+i;
$$


- $r$: a retained Newton return-column index, $0\le r<d$;
- $j$: a source-jet order.

A jet used as a jet of the actual finite top matrix satisfies


$$
n+j<d.
$$


The sequence identities can be derived for arbitrary nonnegative $n,j,r$, but this algebraic extension does not enlarge the finite matrix or create additional original columns.

Put


$$
\alpha=\alpha_d=v_2((2d)!),
\qquad
\beta=\beta_d=v_2((2d-2)!).
$$


Then


$$
\alpha=d+v_2(d!),
\qquad
\alpha-\beta=5.
\tag{2.1}
$$



### 2.2 Complete sequences, returns and terminal

Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,
\qquad w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$



The complete returns are


$$
\sigma_n=u_{n+1}+u_n=c_{n+1}+c_n
$$


and


$$
\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.
$$


Thus, with


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
$$


the integer forcing is exactly


$$
T_n
=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
\tag{2.2}
$$



The original determinant remains


$$
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
$$


where


$$
0\le m<2k,\qquad 0\le j<k.
$$



Its physical terminal is


$$
\boxed{
\text{moment }3k-2,\qquad
\text{factorial }(6k-4)!,\qquad
\text{last odd denominator }6k-5.
}
\tag{2.3}
$$



### 2.3 Actual clearers, contents and primitive normalization

The established least original right-column entry clearers are


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k,
$$


and their least common entry clearer is $\Lambda_k$.

The final gcd is always the all-prime gcd


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
$$


For the rational pair $H_k/\Lambda_k^k$, define


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer and subsequent content are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{2.4}
$$



The actual original rectangles are


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k-1\\j<k}}
\right].
$$


Writing


$$
\mathscr R_k=\delta_{2k-1}(Z_k),
\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


the reused interface is


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k
\mid \Lambda_k\mathscr L_k\mathscr R_k.
\tag{2.5}
$$



The established sign and nonvanishing results give, at every original index,


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,
\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$


and


$$
\boxed{
0<\ell_k=q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{2.6}
$$


These are the actual primitive denominator and the nonzero whole error.

### 2.4 The complete paid pencil

Define


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),
$$




$$
(\mathcal A_d y)_n
=\sum_{h=0}^d(-1)^h\binom dh P_d(n+h)y_{n+h}.
$$


Because $d$ is even,


$$
\mathcal A_d y=\Delta^d(P_dy).
$$



The annihilator acts only on the first $d$ physical rows. Its retained determinant is


$$
\Omega_k=\prod_{n=0}^{d-1}P_d(n),
$$


an odd positive integer.

Put


$$
b(t)=4t^2+6t+3.
$$


The complete top forcing block is


$$
F_k(n,j)
=-\Lambda_k\sum_{h=0}^d(-1)^h\binom dh
P_d(n+h)b(n+h+j)(2(n+h+j))!,
\quad n,j<d.
\tag{2.7}
$$


The identity


$$
b(t)(2t)!=(2t+2)!+(2t)!
$$


shows explicitly that both factorial terms remain.

Let


$$
D_f=\operatorname{diag}((2n)!)_{n<d},
\qquad
F_k=-\Lambda_kD_fK_dD_f.
$$


To avoid confusion with the contact sequence below, write


$$
\eta_d^F=\det K_d.
$$


The established congruence is


$$
K_d(n,j)\equiv\binom{n+j}{j}\pmod2.
\tag{2.8}
$$


Every leading principal determinant of $K_d$ is odd.

Retain


$$
h_d=(2d-2)!,
\qquad
\widehat D_f=h_dD_f^{-1},
$$




$$
N_d=\widehat D_f\,\operatorname{adj}(K_d)\,\widehat D_f,
\qquad
\delta_k=\Lambda_k\eta_d^Fh_d^2,
$$




$$
F_k^{-1}=-N_d/\delta_k,
$$


and


$$
f_k=\det F_k
=(-\Lambda_k)^d\eta_d^F
\left(\prod_{n<d}(2n)!\right)^2.
\tag{2.9}
$$



The complete bottom forcing matrix is


$$
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}b(d+i+j)(2(d+i+j))!,
\quad i<d+2,\ j<d.
\tag{2.10}
$$



The full weighted divisors are


$$
D_r=2^rr!,
\qquad
\mathfrak D_d=\prod_{r=0}^{d-1}D_r,
\qquad
o_d=\operatorname{odd}(d!).
$$


In particular,


$$
D_0=1,\quad D_1=2,\quad
D_4=384=2^7\cdot3,\quad
D_5=3840=2^8\cdot15.
$$


Their odd factors are retained.

Define the integral top sources


$$
\mathsf a_n=\frac{(\mathcal A_dc)_n}{2^d},
\qquad
t_n^{(r)}
=\frac{(\mathcal A_d\Delta^r\sigma)_n}
       {2^{\alpha+1}D_r}.
$$


The corrected columns are exactly


$$
x=RN_d\mathsf a+\frac{\delta_k}{2^{d+2}}c_{\rm bot},
\tag{2.11}
$$




$$
z^{(r)}
=RN_dt^{(r)}
+\frac{\delta_k}{2^{\alpha+3}D_r}
(\Delta^r\sigma)_{\rm bot}.
\tag{2.12}
$$


For $\psi_0=r,\ \psi_1=w$, the complete coefficient borders are


$$
\mathfrak b_h
=\frac{\delta_k\Lambda_k}{4}(\psi_h)_{\rm bot}
+RN_d\Lambda_k(\mathcal A_d\psi_h)_{\rm top},
\qquad h=0,1.
\tag{2.13}
$$


Hence


$$
\mathcal Q_k(s)=
[x,z^{(0)},z^{(1)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1].
\tag{2.14}
$$



The established pair is $x,y=z^{(1)}$. Its depth is $5$, with


$$
\det\Pi_{2,k}=2^5\mu_{2,k},
\qquad \mu_{2,k}=\mu_k\ \text{odd}.
$$


The resulting turn11 pencil is exactly $\mathcal P_k^{[2]}=\mathcal P_k$.

The reused pre-pair transfer is


$$
\delta_k^{d+2}\Omega_kH_{h,k}
=f_k\,2^{\lambda_d}\mathfrak D_d I_{h,k},
\qquad h=0,1,
\tag{2.15}
$$


where


$$
\det\mathcal Q_k(s)=I_{0,k}+I_{1,k}s,
\qquad
\lambda_d=d\alpha+4d+4.
$$



---

## 3. Audit of the exact weighted jets

### 3.1 Product rule, shifts and polynomial differences

The finite-difference product rule needed here is


$$
\Delta^N(fg)(n)
=\sum_{h=0}^N\binom Nh
\Delta^hf(n)\,\Delta^{N-h}g(n+h).
\tag{3.1}
$$


The shift $n+h$ belongs on the second factor.

Set


$$
Q_h(n)=\prod_{a=h}^{d-1}(2n+2a+1).
$$


Since


$$
\Delta Q_h(n)=2(d-h)Q_{h+1}(n),
$$


induction gives


$$
\Delta^hP_d(n)
=2^h\frac{d!}{(d-h)!}Q_h(n),
\qquad 0\le h\le d.
\tag{3.2}
$$


Higher differences vanish.

The established contact divisibility permits the integers


$$
\eta_t^{(m)}
=\frac{\Delta^t\sigma_m}{2^{t+1}t!}.
\tag{3.3}
$$



Now


$$
\Delta^j(\mathcal A_d\Delta^r\sigma)
=\Delta^{d+j}(P_d\Delta^r\sigma).
$$


This is not a commutation of $\mathcal A_d$ with $\Delta$. Applying (3.1) gives


$$
\begin{aligned}
\Delta^j(\mathcal A_d\Delta^r\sigma)_n
={}&
2^{d+j+r+1}d!
\sum_{h=0}^d
\binom{d+j}{h}Q_h(n)\\
&\quad\cdot
\frac{(d-h+r+j)!}{(d-h)!}
\eta_{d-h+r+j}^{(n+h)}.
\end{aligned}
\tag{3.4}
$$



Divide by the actual top-source normalizer


$$
2^{\alpha+1}D_r=2^{\alpha+r+1}r!.
$$


Using $\alpha=d+v_2(d!)$ and


$$
(r+1)_j=\frac{(r+j)!}{r!},
$$


we obtain exactly


$$
\boxed{
\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j}
=
o_d
\sum_{h=0}^d
\binom{d+j}{h}Q_h(n)
\binom{d-h+r+j}{r+j}
\eta_{d-h+r+j}^{(n+h)}.
}
\tag{3.5}
$$



This verifies turn12 (4.3) with:

- every difference of $P_d$;
- the correct binomial coefficient $\binom{d+j}{h}$;
- the shift $n+h$;
- the full factorial ratio;
- the full $D_r$;
- the remaining odd factor $o_d$.

The right side is integral. Therefore


$$
2^j(r+1)_j\mid\Delta^jt_n^{(r)}.
$$


Since


$$
(r+1)_j=j!\binom{r+j}{j},
$$


also


$$
2^jj!\mid\Delta^jt_n^{(r)}.
\tag{3.6}
$$



**Verdict: PASS.**

### 3.2 The actual atom jets

The reused atom identity is


$$
(\mathcal A_dw)_n=2^d(-1)^nU_d(n),
$$


where


$$
U_d(n)=
\sum_{h=0}^d
\binom dh\frac{d!}{(d-h)!}Q_h(n).
$$



A useful direct strengthening of the source’s argument is


$$
\frac{\Delta^tU_d(n)}{2^t}
=
\sum_{h=0}^{d-t}
\binom dh\frac{d!}{(d-h-t)!}Q_{h+t}(n),
\qquad 1\le t\le d.
\tag{3.7}
$$


Every summand contains the even factor $d$. For $t>d$, the difference is zero. Also $U_d(n)$ is odd, because its $h=0$ term is odd and every $h\ge1$ coefficient contains $d$.

The exact identity


$$
\Delta^j((-1)^nU_d(n))
=(-1)^{n+j}
\sum_{t=0}^j\binom jt2^{j-t}\Delta^tU_d(n)
$$


therefore implies


$$
\frac{\Delta^j((-1)^nU_d(n))}{2^j}\equiv1\pmod2.
\tag{3.8}
$$



For the $u$-part, the established divisibility


$$
2^tt!\mid\Delta^tu_m
$$


and the same shifted product rule give


$$
2^{d+j}d!j!\mid\Delta^j(\mathcal A_du)_n.
\tag{3.9}
$$


Indeed, after removing this factor, the factorial ratio in each term is


$$
\frac{(d+j-h)!}{(d-h)!j!}
=\binom{d+j-h}{j}\in\mathbb Z.
$$


Thus the $u$-contribution divided by $2^{d+j}$ is even.

Since $c=u-w$,


$$
\boxed{
\frac{\Delta^j\mathsf a_n}{2^j}\equiv1\pmod2,
\qquad
v_2(\Delta^j\mathsf a_n)=j.
}
\tag{3.10}
$$



The literal atom is indispensable. Replacing $c$ by $u$ would remove the odd normalized entry.

**Verdict: PASS, uniformly for the jets used inside the original top-row range.**

---

## 4. Low-order parity and the selected source minors

### 4.1 Reduction of the exact jet identity

The established contact premises are


$$
\theta_t=\frac{\Delta^tu_0}{2^tt!},
\qquad
\eta_t=\theta_t+(t+1)\theta_{t+1},
$$


and, modulo $2$,


$$
\theta_{t+2}=\theta_{t+1}+\theta_t,
\qquad
(\theta_0,\theta_1,\theta_2)=(1,0,1).
\tag{4.1}
$$


Thus $\theta$ has period $3$.

The finite Newton shift gives


$$
\eta_t^{(m)}
=\sum_{h=0}^m\binom mh2^h(t+1)_h\eta_{t+h},
$$


so


$$
\eta_t^{(m)}\equiv\eta_t\pmod2.
\tag{4.2}
$$



Every $Q_h(n)$ and $o_d$ is odd. Setting $t=d-h$ in (3.5), the normalized jet parity is therefore


$$
J(d,r,j)
=
\sum_{t=0}^d
\binom{d+j}{t+j}
\binom{t+j+r}{j+r}\eta_{t+j+r}
\quad\text{in }\mathbb F_2.
\tag{4.3}
$$


The physical top row $n$ has disappeared **at this normalized parity precision only**.

### 4.2 The polynomial-binomial identity and its cutoff

Vandermonde expansion gives


$$
\binom{t+j+r}{j+r}
=\sum_{a=0}^r\binom ra\binom{t+j}{t-a}.
$$


Multiplying by $\binom{d+j}{t+j}$, factorial cancellation yields


$$
\boxed{
\binom{d+j}{t+j}\binom{t+j+r}{j+r}
=
\sum_{a=0}^r
\binom ra
\binom{d+j}{j+a}
\binom{d-a}{t-a}.
}
\tag{4.4}
$$


This is valid in the original source domain $r<d$, with the usual zero convention for an out-of-range lower index.

Assume now


$$
r+j<16.
\tag{4.5}
$$


Because $16\mid d$, the low four bits of $d+j$ equal those of $j$. For $a\ge1$,


$$
j<j+a<16,
$$


so $j+a$ cannot be a submask of $j$. Lucas’s criterion gives


$$
\binom{d+j}{j+a}\equiv0\pmod2\quad(a\ge1),
$$


whereas


$$
\binom{d+j}{j}\equiv1\pmod2.
$$


Thus


$$
J(d,r,j)=
\sum_{t=0}^d\binom dt\eta_{t+r+j}
=:\varepsilon_{r+j}.
\tag{4.6}
$$



Write $d=2D$. From (4.1),


$$
\eta_{2h}=\theta_h,\qquad
\eta_{2h+1}=\theta_{h+1}
\quad\text{in }\mathbb F_2.
$$


Lucas reduction and $1+E=E^2$ on $\theta$ give


$$
\varepsilon_{2a}=\theta_{a+d},
\qquad
\varepsilon_{2a+1}=\theta_{a+d+1}.
$$


Using $d\equiv2\pmod3$,


$$
\boxed{
(\varepsilon_0,\ldots,\varepsilon_5)
=(1,1,1,0,0,1),
\qquad
\varepsilon_{h+6}=\varepsilon_h.
}
\tag{4.7}
$$



Consequently,


$$
\boxed{
\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j}
\equiv\varepsilon_{r+j}\pmod2,
\qquad r+j<16.
}
\tag{4.8}
$$



**Verdict: PASS with the stated cutoff. Extension of (4.8) beyond that cutoff without further work would fail.**

### 4.3 Uniform source-minor lower divisor

Consider


$$
A=[\mathsf a,t^{(r_1)},\ldots,t^{(r_{q-1})}],
\qquad 1\le q\le d.
$$


Finite Newton expansion in the row index expresses this matrix as


$$
A=B_d\,\mathcal J,
\qquad
B_d(n,j)=\binom nj,
$$


where $\mathcal J$ consists of the source jets at $0$.

For chosen jet orders


$$
j_0<\cdots<j_{q-1},
$$


extract $2^{j_0+\cdots+j_{q-1}}$ using (3.6) and (3.10). Expanding in the atom column, every term contains the contact factorial payments from all but one row. The smallest possible factorial valuation is obtained by omitting a row with largest factorial valuation. Hence it is at least


$$
\sum_{a=0}^{q-2}v_2(j_a!).
$$


Because $j_a\ge a$,


$$
j_0+\cdots+j_{q-1}\ge\binom q2,
\qquad
\sum_{a=0}^{q-2}v_2(j_a!)
\ge\sum_{a=0}^{q-2}v_2(a!).
$$



Cauchy–Binet with the integer matrix $B_d$ now proves that every $q$-minor of $A$ is divisible by $2^{b_q}$, where


$$
\boxed{
b_q=\binom q2+\sum_{j=0}^{q-2}v_2(j!).
}
\tag{4.9}
$$


This is a lower divisor, not an attainment statement.

### 4.4 Source-specific valuation table

For the sources in question, all table entries use $r+j\le9<16$. From (3.10) and (4.8), the table is


$$
\begin{array}{c|ccccc}
j&
\Delta^j\mathsf a&
\Delta^jt^{(1)}&
\Delta^jt^{(0)}&
\Delta^jt^{(5)}&
\Delta^jt^{(4)}
\\ \hline
0&0&0&0&0&\ge1\\
1&1&2&1&2&1\\
2&2&\ge4&3&3&3\\
3&3&\ge7&\ge5&7&4\\
4&4&7&\ge8&\ge9&8
\end{array}
\tag{4.10}
$$


Unadorned entries are exact valuations.

For example,


$$
v_2\!\left(2^2(5+1)_2\right)
=v_2(4\cdot6\cdot7)=3,
$$


and $\varepsilon_7=1$, so the corresponding valuation is exactly $3$. In contrast,


$$
v_2(4\cdot2\cdot3)=3,
$$


but $\varepsilon_3=0$, giving the lower bound $4$ for $\Delta^2t^{(1)}$.

Let


$$
T_q=\{d-q,\ldots,d-1\}.
$$


Changing these consecutive source rows into jets of orders $0,\ldots,q-1$ based at $d-q$ is lower triangular with diagonal $1$. It preserves the determinant exactly.

#### Three columns

For


$$
A^{[3]}=[\mathsf a,t^{(1)},t^{(0)}],
$$


the unique minimum uses


$$
t^{(1)}\text{ in row }0,\quad
t^{(0)}\text{ in row }1,\quad
\mathsf a\text{ in row }2.
$$


Its valuation is $0+1+2=3$.

If the atom is in row $1$, the best remaining contact contribution has valuation at least $3$, giving total at least $4$. If the atom is in row $0$, the total is at least $5$. With the atom in row $2$, the other contact assignment has valuation at least $4$.

Thus the minimum is genuinely unique.

#### Four columns

For


$$
A^{[4]}=[\mathsf a,t^{(1)},t^{(0)},t^{(5)}],
$$


the unique minimum is


$$
t^{(1)},t^{(0)},t^{(5)},\mathsf a
$$


in rows $0,1,2,3$, with valuation


$$
0+1+3+3=7.
$$


If the atom is not in row $3$, the last contact row costs at least $5$, and the total is at least $8$. With the atom in row $3$, inspection of the first three rows shows that every other assignment costs at least $5$, rather than $4$, for those contact rows.

#### Five columns

For


$$
A^{[5]}=[\mathsf a,t^{(1)},t^{(0)},t^{(5)},t^{(4)}],
$$


the unique minimum is


$$
t^{(1)},t^{(0)},t^{(5)},t^{(4)},\mathsf a
$$


in rows $0,1,2,3,4$, with valuation


$$
0+1+3+4+4=12.
$$


If the atom is not in row $4$, that row costs at least $7$, and the total is at least $13$. With the atom in row $4$, attaining $12$ requires $t^{(4)}$ in row $3$, then $t^{(0)}$ in row $1$, then $t^{(5)}$ in row $2$, leaving $t^{(1)}$ in row $0$.

Every factor in each distinguished product is odd after its exact binary payment. Since the minimum is unique, cancellation cannot raise the determinant valuation. Therefore


$$
\boxed{
v_2\det A^{[q]}[T_q,:]=b_q,
\qquad
(b_3,b_4,b_5)=(3,7,12).
}
\tag{4.11}
$$



**Verdict: PASS, including uniqueness and attainment in the actual source rows.**

---

## 5. Complete forcing, adjugate gaps and corrected cofactors

### 5.1 Complete bottom forcing minors

For increasing $q$-tuples $M,I$, let


$$
V(M)=\prod_{a<b}(i_b-i_a),
\qquad
\Phi_q=\prod_{j=0}^{q-1}j!,
$$


and


$$
\mathcal N_q(M)=\frac{V(M)}{\Phi_q}.
$$


The identity


$$
\mathcal N_q(M)
=\det\left[\binom{i_a}{j}\right]_{0\le a,j<q}
\tag{5.1}
$$


proves integrality.

The Cauchy part $R_0$ of (2.10) has exact minor


$$
\det R_0[M,I]
=
\frac{\Lambda_k^q2^{q(q-1)}V(M)V(I)}
{\prod_{i\in M,\ j\in I}(2(d+i+j)+1)}.
\tag{5.2}
$$


There is no missing sign. Both row and column Vandermonde factors have the displayed increasing order.

Every denominator divides $\Lambda_k$, because


$$
d+i+j\le3d,
$$


so its largest possible value is $6d+1=6k-5$.

Define


$$
c_q=q(q-1)+2v_2(\Phi_q).
$$


Then


$$
(c_3,c_4,c_5)=(8,16,30).
\tag{5.3}
$$



The factorial correction in each entry of $R$ has valuation at least $\alpha-2$. Since $16\mid d$,


$$
\alpha=d+v_2(d!)
\ge d+\frac d2+\frac d4=\frac74d.
$$


Thus


$$
\alpha-2\ge110
$$


at every original index.

Multilinearity of a determinant therefore gives


$$
\det R[M,I]\equiv\det R_0[M,I]\pmod{2^{\alpha-2}}.
$$


For $q=3,4,5$, this is more than sufficient to conclude


$$
2^{c_q}\mid\det R[M,I]
$$


and, in fact,


$$
\frac{\det R[M,I]}{2^{c_q}}
\equiv\mathcal N_q(M)\mathcal N_q(I)\pmod2.
\tag{5.4}
$$


For the consecutive set $I=T_q$, $\mathcal N_q(T_q)=1$, so


$$
\boxed{
\frac{\det R[M,T_q]}{2^{c_q}}
\equiv\mathcal N_q(M)\pmod2.
}
\tag{5.5}
$$



This conclusion concerns the complete $R$, not a replacement matrix with its factorial terms deleted.

### 5.2 Factorial diagonal gaps

Set


$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right).
$$


For $r\ge0$ within range,


$$
e_{d-1-r}
=\sum_{s=1}^r(1+v_2(d-s)).
\tag{5.6}
$$


Using $16\mid d$, the final values are


$$
0,\ 1,\ 3,\ 4,\ 7,\ 8
\tag{5.7}
$$


in reverse row order, through $e_{d-6}$.

Thus


$$
E_q^F:=\sum_{n\in T_q}e_n
$$


satisfies


$$
(E_3^F,E_4^F,E_5^F)=(4,8,15).
\tag{5.8}
$$



The weights $e_n$ strictly decrease as $n$ increases. Therefore $T_q$ is the unique $q$-set with minimum weight sum. For $q=3,4,5$, replacing it by any other set increases that sum by at least


$$
1,\quad3,\quad1,
\tag{5.9}
$$


respectively.

Because the two diagonal factors in $N_d$ are retained,


$$
v_2\det N_d[I,J]
\ge\sum_{i\in I}e_i+\sum_{j\in J}e_j.
\tag{5.10}
$$



### 5.3 The complementary leading Pascal determinant

For the principal terminal set, Jacobi’s identity gives


$$
\det\operatorname{adj}(K_d)[T_q,T_q]
=(\eta_d^F)^{q-1}\det K_d[T_q^c,T_q^c].
\tag{5.11}
$$


The complement is a leading principal block.

The needed leading-block assertion follows from the established Pascal congruence: for a leading block of size $L$,


$$
\binom{n+j}{j}
=\sum_{h=0}^{L-1}\binom nh\binom jh,
\qquad n,j<L.
$$


It is the product of a unit lower-triangular Pascal matrix and its transpose. Its determinant is $1$. Hence the complementary determinant in (5.11) is odd.

Consequently,


$$
\boxed{
v_2\det N_d[T_q,T_q]=2E_q^F.
}
\tag{5.12}
$$


Every other pair $(I,J)$ has strictly larger valuation. More precisely, the lower gaps supplied by (5.9) are $1,3,1$ for $q=3,4,5$.

Oddness of $\det K_d$ alone would not prove this step; the complementary leading block is essential.

### 5.4 Both retained bottom corrections

Since $c_m$ is even, the correction in $x$ has valuation at least


$$
2\beta-(d+2)+1
=2\beta-d-1
=2\alpha-d-11.
\tag{5.13}
$$



For every $r<d$, the full sequence divisibility gives


$$
2D_r\mid\Delta^r\sigma_m.
$$


Therefore the correction in $z^{(r)}$, after its actual full $D_r$-division, has valuation at least


$$
2\beta-\alpha-2=\alpha-12.
\tag{5.14}
$$



Set


$$
L_d=\alpha-12.
$$


Then $L_d\ge100$, and the atom correction has at least this valuation as well. Hence


$$
\mathcal C^{[q]}
\equiv RN_dA^{[q]}\pmod{2^{L_d}},
\qquad q=3,4,5.
\tag{5.15}
$$


All other entries are integers, so a fixed minor changes by a multiple of $2^{L_d}$.

Both kinds of bottom correction remain in the exact matrices. They are invisible only at the justified precision.

### 5.5 Cauchy–Binet evaluation

For a residual row set $M$ of size $q$,


$$
\det(RN_dA^{[q]})[M,:]
=
\sum_{\substack{|I|=q\\|J|=q}}
\det R[M,I]\,
\det N_d[I,J]\,
\det A^{[q]}[J,:].
\tag{5.16}
$$



The universal lower valuations are


$$
c_q,\qquad 2E_q^F,\qquad b_q.
$$


The pair $I=J=T_q$ is the unique pair whose factorial-adjugate factor can attain $2E_q^F$. Its normalized source factor is odd by (4.11), its normalized adjugate factor is odd by (5.12), and its normalized forcing residue is $\mathcal N_q(M)$ by (5.5).

Every other term has at least one additional factor $2$. Therefore


$$
t_q=c_q+2E_q^F+b_q
$$


gives


$$
\boxed{
(t_3,t_4,t_5)
=(8+8+3,\ 16+16+7,\ 30+30+12)
=(19,39,72).
}
\tag{5.17}
$$


Because $t_q<L_d$, the corrected columns have the same normalized residue:


$$
\boxed{
2^{t_q}\mid\det\mathcal C^{[q]}[M,:],
\qquad
\frac{\det\mathcal C^{[q]}[M,:]}{2^{t_q}}
\equiv\mathcal N_q(M)\pmod2.
}
\tag{5.18}
$$



For $M=(0,\ldots,q-1)$, the residue is $1$. Thus the first $q$ residual physical rows attain the content valuation.

If


$$
\mathscr C_k^{[q]}
=\gcd_{|M|=q}\left|\det\mathcal C^{[q]}[M,:]\right|,
$$


then


$$
\boxed{
v_2(\mathscr C_k^{[3]})=19,\quad
v_2(\mathscr C_k^{[4]})=39,\quad
v_2(\mathscr C_k^{[5]})=72.
}
\tag{5.19}
$$



These are valuations of actual all-prime contents. Their odd parts are not evaluated.

The physical rows are $m=d+i$. Since translation does not change Vandermonde differences, (5.18) is genuinely a residue statement in those original physical rows.

**Verdict: PASS for the complete higher cofactors and their normalized row residues.**

---

## 6. Cramer interpolation, all remaining columns and both borders

### 6.1 Integer Cramer payments

For $q=3,4,5$, put the selected common columns first and partition the complete permuted pencil:


$$
\begin{pmatrix}
\Pi_{q,k}&U_{q,k}(s)\\
V_{q,k}&C_{q,k}(s)
\end{pmatrix},
$$


where


$$
\det\Pi_{q,k}=2^{t_q}\mu_{q,k}.
$$


By (5.18), $\mu_{q,k}$ is odd and nonzero.

Define


$$
M_{q,k}
=\frac{V_{q,k}\operatorname{adj}(\Pi_{q,k})}{2^{t_q}}.
\tag{6.1}
$$


Each numerator entry is a determinant obtained by replacing one pivot row by a residual row. After sorting its row order, it is a signed $q$-minor of the complete selected columns. Equation (5.18) therefore proves every division in (6.1) integral.

Exactly,


$$
V_{q,k}\Pi_{q,k}^{-1}=M_{q,k}/\mu_{q,k}.
\tag{6.2}
$$



Here $\mu_{q,k}$ is the actual odd pivot quotient. It is not replaced by $1$. Nor is it asserted to be the least possible denominator after all individual cancellations.

### 6.2 Explicit interpolation residues

Let


$$
B_{h,t}=\binom ht,\qquad 0\le h,t<q.
$$


Its inverse is


$$
(B^{-1})_{t,h}=(-1)^{t-h}\binom th
\quad(t\ge h).
$$


Hence the integer-valued interpolation coefficient for node $h$ is


$$
\lambda_h^{[q]}(i)
=\sum_{t=h}^{q-1}(-1)^{t-h}\binom th\binom it.
\tag{6.3}
$$


It satisfies


$$
\lambda_h^{[q]}(a)=\delta_{h,a}
\quad(0\le a<q),
\qquad
\sum_{h=0}^{q-1}\lambda_h^{[q]}(i)=1.
\tag{6.4}
$$



The Cramer residue formula (5.18) gives


$$
(V_{q,k}\Pi_{q,k}^{-1})_{i,h}
\equiv\lambda_h^{[q]}(i)\pmod2.
\tag{6.5}
$$


The signs involved in placing the replacement row in increasing order disappear only after reduction modulo $2$; the integer Cramer divisions themselves retain their signs.

Writing $B_t=\binom it\bmod2$, the three residue vectors are:



$$
q=3:\quad
(1+B_1+B_2,\ B_1,\ B_2);
\tag{6.6}
$$





$$
q=4:\quad
(1+B_1+B_2+B_3,\ B_1+B_3,\ B_2+B_3,\ B_3);
\tag{6.7}
$$





$$
q=5:\quad
(1+B_1+B_2+B_3+B_4,\ B_1+B_3,\ B_2+B_3,\ B_3,\ B_4).
\tag{6.8}
$$



Each vector has coefficient sum $1$ in $\mathbb F_2$.

### 6.3 Parity of every complete column

The established factorial-adjugate residue is


$$
N_d\equiv e_{\rm last}e_{\rm last}^{\,T}\pmod2.
\tag{6.9}
$$


Also $R$ is entrywise odd.

Thus $RN_dv$ is row-constant modulo $2$ for every integral top vector $v$. The bottom corrections in (2.11)–(2.12) are even, uniformly for all $r<d$. Consequently:

- $x$ has row residue $1$;
- every $z^{(r)}$ has a row-constant residue, not necessarily $1$.

Both coefficient borders must be checked separately.

For the linear border, the top vector


$$
\Lambda_k\mathcal A_dw
$$


is divisible by $2^d$, and its bottom correction is even. Its complete row residue is therefore $0$.

For the constant border, $\Lambda_kr_n$ is even whenever $n\ge1$: the factorial term is even and $4\Lambda_k\rho_n$ is divisible by $4$. The last top component of $\Lambda_k\mathcal A_dr$ uses only such indices. Equation (6.9) therefore gives residue $0$ for the $RN_d$-part. Its bottom correction is also even, since $\Lambda_kr$ is integral and $\delta_k/4$ is even.

Hence both complete coefficient borders have row residue $0$. Neither the factorial part of $r$, its rational part, nor the literal $w$ has been omitted.

### 6.4 The additional row divisions

Set


$$
\mathcal V_k^{[q]}(s)
=\mu_{q,k}C_{q,k}(s)-M_{q,k}U_{q,k}(s).
$$


The original column parities are row-constant, and the interpolation coefficients sum to $1$ modulo $2$. Since $\mu_{q,k}$ is odd,


$$
\mathcal V_k^{[q]}(s)\equiv0\pmod2
$$


coefficientwise, including both affine coefficients.

Therefore


$$
\boxed{
\mathcal P_k^{[q]}(s)
=\frac{\mathcal V_k^{[q]}(s)}2
}
\tag{6.10}
$$


is an integer pencil of size


$$
n_q=d+2-q.
$$


The division contributes $2^{n_q}$ to its block determinant identity.

The retained columns are exactly


$$
\begin{array}{c|l|c}
q&\text{remaining return indices}&n_q\\ \hline
2&0,2,3,4,5,\ldots,d-1&d\\
3&2,3,4,5,\ldots,d-1&d-1\\
4&2,3,4,6,\ldots,d-1&d-2\\
5&2,3,6,\ldots,d-1&d-3.
\end{array}
\tag{6.11}
$$


Each pencil also retains its complete affine border.

These are direct paid Schur pencils from $\mathcal Q_k$. Their row payments must not be added as though every direct definition had been applied cumulatively to the same determinant.

### 6.5 The actual next pivots

For a new common column $z$, the bordered determinant identity gives


$$
\det
\begin{pmatrix}
\Pi_q&u\\v&c
\end{pmatrix}
=2^{t_q}\bigl(\mu_qc-M_qu\bigr)
=2^{t_q+1}(\mathcal P_k^{[q]})_{i-q,z}.
\tag{6.12}
$$



For the next selected column, the normalized Vandermonde is


$$
\mathcal N_{q+1}(0,1,\ldots,q-1,i)=\binom iq.
$$


Thus


$$
\frac{(\mathcal P_k^{[q]})_{i-q,z_{\rm next}}}
     {2^{t_{q+1}-t_q-1}}
\equiv\binom iq\pmod2.
\tag{6.13}
$$


At $i=q$, the numerator determinant is exactly $\det\Pi_{q+1}$. Therefore the first entries of the selected next columns are


$$
(\mathcal P_k^{[2]})_{0,z^{(0)}}=2^{13}\mu_{3,k},
$$




$$
(\mathcal P_k^{[3]})_{0,z^{(5)}}=2^{19}\mu_{4,k},
$$




$$
(\mathcal P_k^{[4]})_{0,z^{(4)}}=2^{32}\mu_{5,k}.
\tag{6.14}
$$


The depths are


$$
19-5-1=13,\qquad
39-19-1=19,\qquad
72-39-1=32.
$$



These are actual corrected-pencil entries, and each corresponding column content has exactly the displayed binary valuation.

**Verdict: PASS for all Cramer divisions, interpolation residues, whole-pencil row divisions and pivots.**

---

## 7. Signs, coefficient transfers and return to the original normalization

### 7.1 Column permutations

Relative to


$$
[x,z^{(0)},z^{(1)},z^{(2)},\ldots,\text{border}],
$$


the signs are


$$
\epsilon_2=-1,\qquad
\epsilon_3=-1,\qquad
\epsilon_4=+1,\qquad
\epsilon_5=+1.
\tag{7.1}
$$



Indeed:

- putting $z^{(1)}$ before $z^{(0)}$ is one transposition;
- the $q=3$ total order is unchanged;
- moving $z^{(5)}$ past $z^{(2)},z^{(3)},z^{(4)}$ uses three transpositions;
- then moving $z^{(4)}$ past $z^{(2)},z^{(3)}$ uses two.

### 7.2 Exact determinant and coefficient identities

Write


$$
\det\mathcal P_k^{[q]}(s)
=P_{0,k}^{[q]}+P_{1,k}^{[q]}s.
$$


Since the Schur complement is $2\mathcal P_k^{[q]}/\mu_{q,k}$,


$$
\epsilon_q\det\mathcal Q_k(s)
=2^{t_q+n_q}\mu_{q,k}^{1-n_q}
\det\mathcal P_k^{[q]}(s).
$$


Thus, coefficientwise,


$$
\boxed{
\mu_{q,k}^{n_q-1}I_{h,k}
=\epsilon_q2^{t_q+n_q}P_{h,k}^{[q]},
\qquad h=0,1.
}
\tag{7.2}
$$



In particular,


$$
\mu_{3,k}^{d-2}I_{h,k}
=-2^{d+18}P_{h,k}^{[3]},
$$




$$
\mu_{4,k}^{d-3}I_{h,k}
=2^{d+37}P_{h,k}^{[4]},
$$




$$
\mu_{5,k}^{d-4}I_{h,k}
=2^{d+69}P_{h,k}^{[5]}.
\tag{7.3}
$$



Comparing consecutive stages gives


$$
\mu_{3,k}^{d-2}P_{h,k}^{[2]}
=2^{13}\mu_k^{d-1}P_{h,k}^{[3]},
$$




$$
\mu_{4,k}^{d-3}P_{h,k}^{[3]}
=-2^{19}\mu_{3,k}^{d-2}P_{h,k}^{[4]},
$$




$$
\mu_{5,k}^{d-4}P_{h,k}^{[4]}
=2^{32}\mu_{4,k}^{d-3}P_{h,k}^{[5]}.
\tag{7.4}
$$


The combined signed relation is


$$
\mu_{5,k}^{d-4}P_{h,k}^{[2]}
=-2^{64}\mu_k^{d-1}P_{h,k}^{[5]}.
\tag{7.5}
$$



### 7.3 Actual all-prime gcds

Let


$$
g_k^{[q]}
=\gcd(|P_{0,k}^{[q]}|,|P_{1,k}^{[q]}|),
\qquad
\nu_k^{[q]}=v_2(g_k^{[q]}).
$$


Taking actual all-prime gcds in (7.4) yields


$$
|\mu_{3,k}|^{d-2}g_k^{[2]}
=2^{13}|\mu_k|^{d-1}g_k^{[3]},
$$




$$
|\mu_{4,k}|^{d-3}g_k^{[3]}
=2^{19}|\mu_{3,k}|^{d-2}g_k^{[4]},
$$




$$
|\mu_{5,k}|^{d-4}g_k^{[4]}
=2^{32}|\mu_{4,k}|^{d-3}g_k^{[5]}.
\tag{7.6}
$$


Thus


$$
\boxed{
|\mu_{5,k}|^{d-4}g_k^{[2]}
=2^{64}|\mu_k|^{d-1}g_k^{[5]},
}
\tag{7.7}
$$


and


$$
\boxed{
\nu_k=\nu_k^{[2]}
=13+\nu_k^{[3]}
=32+\nu_k^{[4]}
=64+\nu_k^{[5]}.
}
\tag{7.8}
$$



The intermediate odd factors cancel by exact identities; they have not been declared equal to $1$.

Combining (2.15) with the $q=5$ identity gives


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d+d+69}\mathfrak D_d\,g_k^{[5]}.
}
\tag{7.9}
$$



This retains the full annihilator determinant, forcing determinant, Schur clearer, Newton product, all binary payments, odd pivot factor and residual all-prime gcd.

Using the established turn11 offset


$$
\chi_k=
d^2+4d+29+(d+4)s_2(d)
-3\sum_{n=0}^{d-1}s_2(n),
$$


we obtain


$$
\boxed{
v_2(G_k)=\chi_k+64+\nu_k^{[5]}.
}
\tag{7.10}
$$


The old digit-sum calculation is reused, not repeated.

### 7.4 Primitive denominator and whole error

The coefficient pairs at every stage are common nonzero rational scalar multiples of the original pair, and the all-prime identities account for the absolute scalar in their gcds. Hence


$$
\boxed{
\frac{|P_{1,k}^{[5]}|}{g_k^{[5]}}
=\frac{|H_{1,k}|}{G_k}=q_k,
}
\tag{7.11}
$$


and


$$
\boxed{
\frac{|P_{0,k}^{[5]}+P_{1,k}^{[5]}(e+\pi)|}{g_k^{[5]}}
=
\frac{|H_k(e+\pi)|}{G_k}
=\ell_k>0.
}
\tag{7.12}
$$



No lower divisor has replaced $G_k$. No simultaneous least-clearer assertion has been made for $\delta_k$ or $\mu_{q,k}$; the actual original least coefficient clearer remains (2.4).

**Verdict: PASS, including signs, all-prime scalars and primitive normalization.**

---

## 8. Independent derivation of the all-order $\mathbb F_4$ law

### 8.1 Extension of the unreduced sum by zero

Start from the exact parity sum (4.3), not from the low-order reduction. Put


$$
n_0=d+j,\qquad K=j+r,\qquad \ell=t+j.
$$


Then


$$
J(d,r,j)
=\sum_{\ell=j}^{n_0}
\binom{n_0}{\ell}\binom{\ell+r}{K}\eta_{\ell+r}.
$$


For $0\le\ell<j$,


$$
\ell+r<K,
$$


so $\binom{\ell+r}{K}=0$. Therefore


$$
\boxed{
J(d,r,j)
=\sum_{\ell=0}^{n_0}
\binom{n_0}{\ell}\binom{\ell+r}{K}\eta_{\ell+r}.
}
\tag{8.1}
$$


No negative-index contact value is introduced. The upper endpoint is unchanged.

### 8.2 Trace formulas

Work in


$$
\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1).
$$


Then


$$
\omega^3=1,\qquad 1+\omega=\omega^2,
$$


and


$$
\operatorname{Tr}(x)=x+x^2.
$$


The trace values are


$$
\operatorname{Tr}(1)=0,\qquad
\operatorname{Tr}(\omega)=\operatorname{Tr}(\omega^2)=1.
$$



The sequence


$$
\operatorname{Tr}(\omega^{m+2})
$$


starts $1,0,1$ and satisfies the recurrence in (4.1). Hence


$$
\boxed{
\theta_m=\operatorname{Tr}(\omega^{m+2}),
}
$$


and


$$
\boxed{
\eta_m
=\operatorname{Tr}\!\left(
\omega^{m+2}[1+(m+1)\omega]
\right).
}
\tag{8.2}
$$


All integer multipliers inside $\mathbb F_4$ are reduced modulo $2$.

### 8.3 Both coefficients and the derivative term

Define


$$
C(a,b,K)
=[z^K](1+z)^a[1+\omega(1+z)]^b.
\tag{8.3}
$$


Let


$$
X=\omega(1+z).
$$


Using


$$
\binom{\ell+r}{K}=[z^K](1+z)^{\ell+r},
$$


substitution of (8.2) into (8.1) gives


$$
\begin{aligned}
J(d,r,j)
=\operatorname{Tr}\Bigl(
\omega^{r+2}[z^K](1+z)^r
\sum_{\ell=0}^{n_0}\binom{n_0}{\ell}X^\ell
[1+(r+1)\omega+\ell\omega]
\Bigr).
\end{aligned}
\tag{8.4}
$$



The two sums are


$$
\sum_{\ell=0}^{n_0}\binom{n_0}{\ell}X^\ell=(1+X)^{n_0}
$$


and, by formal differentiation in characteristic $2$,


$$
\sum_{\ell=0}^{n_0}\ell\binom{n_0}{\ell}X^\ell
=(n_0\bmod2)X(1+X)^{n_0-1}.
\tag{8.5}
$$


The additional $\omega$ already multiplying $\ell$ in (8.4) changes $\omega X$ into


$$
\omega^2(1+z).
$$


Therefore


$$
\boxed{
\begin{aligned}
J(d,r,j)
=\operatorname{Tr}\Bigl(\omega^{r+2}\bigl(
&[1+(r+1)\omega]C(r,n_0,K)\\
&+(n_0\bmod2)\omega^2C(r+1,n_0-1,K)
\bigr)\Bigr).
\end{aligned}
}
\tag{8.6}
$$



Both coefficient arguments are correct:

- first: $(a,b,K)=(r,d+j,r+j)$;
- second: $(a,b,K)=(r+1,d+j-1,r+j)$.

Since $d>0$, the second exponent $n_0-1$ is nonnegative. There is no need for $r+j<16$.

The derivative term is not optional. As a symbolic check on the original domain, take $r=0,j=1$. Then $n_0=d+1$ is odd, and


$$
C(0,d+1,1)=\omega^{2d+1}=\omega^2,
\qquad
C(1,d,1)=\omega^{2d}=\omega.
$$


Formula (8.6) returns $1$, as required by the independently audited low-order value $\varepsilon_1=1$. Omitting the derivative term returns


$$
\operatorname{Tr}(1)=0.
$$


This is an original-domain symbolic check, not a rerun of the finite receipt.

**Verdict: PASS for the full all-order formula, including the derivative term and both coefficients.**

---

## 9. Audit of the two-carry coefficient algorithm

### 9.1 Lucas expansion and exponent signs

Since


$$
1+\omega(1+z)
=\omega^2+\omega z
=\omega^2(1+\omega^{-1}z),
$$


we have


$$
C(a,b,K)
=\omega^{2b}[z^K](1+z)^a(1+\omega^{-1}z)^b.
$$


Lucas expansion in characteristic $2$ gives


$$
\boxed{
C(a,b,K)
=\omega^{2b}
\sum_{\substack{u+v=K\\u\subseteq_{\rm bit}a\\v\subseteq_{\rm bit}b}}
\omega^{-v}.
}
\tag{9.1}
$$



The negative exponent is necessary. At digit $i$, a selected $v_i=1$ contributes


$$
\omega^{-2^i}.
$$


Because $2^i\equiv(-1)^i\pmod3$, this weight alternates between

- $\omega^2$ at even $i$;
- $\omega$ at odd $i$.

The final prefactor is $\omega^{2b\bmod3}$.

### 9.2 Carry-state invariant

At digit $i$, choose


$$
u_i\in
\begin{cases}
\{0\},&a_i=0,\\
\{0,1\},&a_i=1,
\end{cases}
\qquad
v_i\in
\begin{cases}
\{0\},&b_i=0,\\
\{0,1\},&b_i=1.
\end{cases}
$$


Thus a zero input bit has exactly one zero choice. Counting it twice would incorrectly cancel a contribution in characteristic $2$.

Let $w_i(c)$ be the total weight of valid low-digit choices with carry $c\in\{0,1\}$. Initialize


$$
w_0(0)=1,\qquad w_0(1)=0.
$$


The transition is


$$
\boxed{
w_{i+1}(c')
=
\sum_{\substack{c,u_i,v_i\\
u_i+v_i+c=K_i+2c'}}
w_i(c)\,\omega^{-v_i2^i}.
}
\tag{9.2}
$$



The invariant is


$$
u_{<i}+v_{<i}=K_{<i}+2^ic,
$$


with accumulated weight $\omega^{-v_{<i}}$. The transition equation is exactly the condition that this invariant persist at the next digit.

Since $u_i+v_i+c\le3$, no carry beyond $1$ is possible. Two carry states suffice.

### 9.3 Leading-zero termination

Choose


$$
L\ge\max\bigl(1,\operatorname{bitlen}(a),
\operatorname{bitlen}(b),\operatorname{bitlen}(K)\bigr).
$$


At every position $i\ge L$, all three input digits vanish.

At the first such all-zero digit:

- carry $0$ has the unique transition to carry $0$;
- carry $1$ would require $1=2c'$, so it has no transition.

Thus one leading all-zero digit kills any remaining carry. Equivalently, after processing the $L$ input digits, retain only carry $0$.

The coefficient is


$$
C(a,b,K)=\omega^{2b\bmod3}w_L(0).
\tag{9.3}
$$



This rejects an unresolved overflow rather than silently accepting it.

### 9.4 Trace output and complexity

Each coefficient uses a two-component carry-state vector over the fixed field $\mathbb F_4$, with only a constant number of transitions per digit. The two coefficients in (8.6) can be evaluated sequentially, or with two such state vectors in parallel.

The digit complexity is


$$
O(\log(a+b+K+1)).
$$


For actual finite-matrix jets,


$$
r<d,\qquad j<d,
$$


so all coefficient inputs are $O(d)$, and the number of digit steps is $O(\log d)$.

The correct complexity interpretation is:

- $O(\log d)$ digit steps for original finite-source entries;
- constant-size finite-field carry state;
- ordinary input storage of $O(\log d)$ bits;
- not an $O(\log d)$ determinant or inverse computation.

For algebraically extended, unbounded $r,j$, the complexity must instead be stated in terms of $\log(d+r+j+1)$.

Finally, the trace in (8.6) lies in $\mathbb F_2$, since


$$
\operatorname{Tr}(x)^2=x^2+x^4=x^2+x.
$$


It is the required parity, not an unevaluated $\mathbb F_4$ coefficient.

**Verdict: PASS for the carry algorithm and its stated entry-computation complexity.**

---

## 10. Algebraic cross-check at $j=0$

This section compares the new formula with the evaluated bitmask law from turn19. That older theorem is reused; it is not being presented as a second independent audit of itself.

Let


$$
h=d\mathbin{\&}r,
\qquad
\gamma(d,r)=d-h.
$$


Thus $\gamma(d,r)$ consists of the bits of $d$ absent from $r$.

At $j=0$,


$$
n_0=d,\qquad K=r,
$$


and the derivative term vanishes because $d$ is even.

In (9.1), the conditions $u+v=r$ and $u\subseteq_{\rm bit}r$ imply that $v=r-u$ is the complementary submask of $r$. Therefore the permitted $v$'s are exactly the submasks of $h=d\mathbin{\&}r$. Hence


$$
\begin{aligned}
C(r,d,r)
&=\omega^{2d}\sum_{v\subseteq_{\rm bit}h}\omega^{-v}\\
&=\omega^{2d}
\prod_{i:h_i=1}(1+\omega^{-2^i}).
\end{aligned}
$$


For either nontrivial cube root $z$, $1+z=z^2$. Thus


$$
C(r,d,r)
=\omega^{2d-2h}
=\omega^{2\gamma(d,r)}.
\tag{10.1}
$$



Substituting into (8.6):

- if $r$ is odd, $1+(r+1)\omega=1$;
- if $r$ is even, $1+(r+1)\omega=1+\omega=\omega^2$.

Therefore


$$
\boxed{
J(d,r,0)
=\theta_{\,2\gamma(d,r)+c_r},
\qquad
c_r=r+2\mathbf1_{\{r\text{ even}\}}.
}
\tag{10.2}
$$


This agrees exactly with turn19 Section 6.2.

It also supplies an explicit warning against extending the old cutoff formula. At every original $d$, bit $4$ is present. For $r=16,j=0$,


$$
\gamma(d,16)=d-16,
$$


so


$$
J(d,16,0)
=\theta_{2d-14}=1,
$$


because $d\equiv2\pmod3$. But the illicit extension of the six-periodic low-order answer would give


$$
\varepsilon_{16}=\varepsilon_4=0.
$$


Thus the $r+j<16$ restriction is mathematically essential, not merely a conservative presentation choice.

---

## 11. The general cofactor criterion and a new exact source-unit test

### 11.1 Audit of the criterion at its stated hypotheses

Choose $q-1$ distinct original return indices $r_a<d$, together with the atom source, and assume


$$
1\le q\le d.
$$


Define


$$
b_q=\binom q2+\sum_{j=0}^{q-2}v_2(j!),
$$




$$
c_q=q(q-1)+2\sum_{j=0}^{q-1}v_2(j!),
$$




$$
E_q^F
=\sum_{r=0}^{q-1}\sum_{s=1}^r(1+v_2(d-s)).
$$



Suppose


$$
v_2\det A^{[q]}[T_q,:]=b_q
\tag{11.1}
$$


and


$$
t_q:=c_q+2E_q^F+b_q<L_d.
\tag{11.2}
$$



These hypotheses suffice:

1. The uniform source-minor divisor is valid for every $q\le d$.
2. The strict inequality implies $c_q<\alpha-2$, so the complete forcing-minor calculation is valid at the required precision.
3. The factorial weight minimum is uniquely attained at $T_q$.
4. The complementary leading determinant is odd.
5. The complete bottom corrections vanish modulo $2^{t_q+1}$.

Consequently the same Cauchy–Binet proof gives


$$
v_2(\operatorname{content}_q(\mathcal C^{[q]}))=t_q
$$


and normalized row residues $\mathcal N_q(M)$.

**Verdict: PASS as a conditional criterion.** It does not supply (11.1), and its strict inequality cannot be weakened to an unverified deletion of corrections at or beyond $L_d$.

### 11.2 New proved audit lemma: the precise binary source-unit matrix

The all-order entry law can be connected to the source-unit hypothesis without hiding any jet factorial payment.

Let


$$
\nu_j=v_2(j!),\qquad \nu_*=\nu_{q-1},
$$


and take the terminal source rows $T_q$, equivalently jets at $n=d-q$ of orders $0,\ldots,q-1$.

Define a $q\times q$ binary matrix $\mathcal U$ by


$$
\mathcal U_{j,0}
=\mathbf1_{\{\nu_j=\nu_*\}},
$$


and


$$
\boxed{
\mathcal U_{j,a}
=
\left(\binom{r_a+j}{j}\bmod2\right)
J(d,r_a,j),
\qquad 1\le a<q.
}
\tag{11.3}
$$


Equivalently, the binomial factor is $1$ precisely when


$$
r_a\mathbin{\&}j=0.
$$



Then


$$
\boxed{
\frac{\det A^{[q]}[T_q,:]}{2^{b_q}}
\equiv\det\mathcal U\pmod2.
}
\tag{11.4}
$$


In particular,


$$
v_2\det A^{[q]}[T_q,:]=b_q
\quad\Longleftrightarrow\quad
\det\mathcal U=1.
\tag{11.5}
$$



#### Proof

Let $\mathcal J$ be the consecutive jet matrix. Form the integer matrix $W$ with entries


$$
W_{j,0}
=2^{\nu_*-\nu_j}\frac{\Delta^j\mathsf a_n}{2^j},
$$




$$
W_{j,a}
=\frac{\Delta^jt_n^{(r_a)}}{2^{j+\nu_j}}.
$$


Its integrality follows from the atom and contact jet divisibilities.

Its determinant satisfies


$$
\det\mathcal J
=
2^{\sum_{j=0}^{q-1}(j+\nu_j)-\nu_*}\det W
=2^{b_q}\det W.
\tag{11.6}
$$


The atom entries reduce to $\mathbf1_{\{\nu_j=\nu_*\}}$ by (3.10).

For a contact entry,


$$
\frac{\Delta^jt_n^{(r)}}{2^{j+\nu_j}}
=
\frac{(r+1)_j}{2^{\nu_j}}
\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j}.
$$


Since


$$
\frac{(r+1)_j}{2^{\nu_j}}
=\operatorname{odd}(j!)\binom{r+j}{j},
$$


its parity is exactly the contact entry in (11.3). Thus $W\bmod2=\mathcal U$, proving (11.4). ∎

This is an all-order, explicitly evaluated **entry test** for the nominal source depth. It uses the actual weighted sources and their factorial payments. The atom column is supported only on the final factorial-valuation plateau—one row when $q$ is odd, and the final two rows when $q$ is even.

It does **not** prove that a desired growing determinant $\det\mathcal U$ equals $1$. That determinant remains a growing object. No compact inverse theorem follows from the logarithmic entry rule.

### 11.3 A quantitative limit on the correction-free criterion

For $q\le d$,


$$
E_q^F\ge\binom q2,
$$


because every summand $1+v_2(d-s)$ is at least $1$. Hence


$$
t_q=c_q+2E_q^F+b_q
\ge\frac52q(q-1).
\tag{11.7}
$$


Also


$$
L_d=2d-s_2(d)-12\le2d-13.
$$


Therefore the strict criterion $t_q<L_d$ forces


$$
\boxed{
\frac52q(q-1)<2d-13.
}
\tag{11.8}
$$


In particular, this correction-free method can reach only $q=O(\sqrt d)$, even if every requested source-unit hypothesis were proved.

This is a bound on the **applicability of the present comparison argument**, not an upper bound on any actual residual gcd.

There is additionally the exact rank obstruction


$$
\operatorname{rank}\!\left(
RN_d[\mathsf a,t^{(0)},\ldots,t^{(d-1)}]
\right)\le d,
$$


whereas the complete common-column matrix has $d+1$ columns. Every $(d+1)$-minor of the pure product vanishes. The retained corrections must eventually supply essential rank.

---

## 12. Finite boundaries and excluded extrapolations

### 12.1 Boundary check

All audited operations remain inside the original arrays.

- The annihilator acts on only the first $d$ rows.
- A top jet used in the matrix has $n+j<d$.
- Combining the annihilator, such a jet and an original return index $r<d$ uses return indices at most $3d-2$.
- The largest bottom return index remains
  

$$
(2d+1)+(d-1)=3d.
$$


- Its successor moment remains $3d+1=3k-2$.
- The terminal factorial remains $6d+2=6k-4$.
- The selected residual pivots use physical rows
  

$$
m=d,d+1,\ldots,d+4.
$$


- After $q=5$, the remaining rows are
  

$$
m=d+5,\ldots,2d+1,
$$


  including the original last row.
- All unselected original common columns and both complete affine coefficients remain.

The disappearance of $n$ from $J(d,r,j)$ is only a parity fact for a properly normalized top jet. It is not a disappearance of physical rows from the integer pencil.

### 12.2 Rejected extensions and their repaired statements

| Proposed extension | Verdict | Correct usable statement |
|---|---|---|
| Extend $\varepsilon_{r+j}$ to all orders | **FAIL** | Use the all-order formula (8.6); $r=16,j=0$ already distinguishes it from the low-order period. |
| Infer a growing source unit from $O(\log d)$ entry evaluation | **FAIL** | The source-unit condition is the growing determinant test (11.5), still requiring proof. |
| Delete bottom corrections throughout a full common-column elimination | **FAIL** | Deletion is justified only below $L_d$; (11.8) bounds this method’s range. |
| Use the pure $RN_dA$ for all $d+1$ common columns | **FAIL** | Its rank is at most $d$; the complete corrected layer is indispensable. |
| Infer a residual coefficient upper bound from contents $19,39,72$ | **FAIL** | These give the exact payment $\nu_k=64+\nu_k^{[5]}$, not an upper bound on $\nu_k^{[5]}$. |
| Infer terminal border units from common-column saturation | **FAIL** | The two complete terminal coefficients need joint depth control. |
| Replace odd pivot quotients or the final gcd by units or lower divisors | **FAIL** | Retain the exact $\mu_{q,k}$, all-prime transfers, $G_k$, $q_k$ and $\ell_k$. |

### 12.3 Separate work remains separate

No conclusion is transferred to the other binary producer. Its data remain


$$
b=9^{18+32u},\qquad n=4002b,
$$


with reconstruction indices $0,\ldots,b$, terminal $z_b=0$, complete corrected columns


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
$$


and complete return


$$
\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


Its contents, norm, least simultaneous clearer, primitive denominator and all-prime final gcd are not identified with those of the present pencil.

Likewise, this audit gives no new pass to Uniform56, the higher ternary block theorem, physical source34, the separately labelled eta, first4, or physical7 obligations. Their separate statuses remain unchanged. Oddness of $\eta_d^F$ here is not a substitute for any separately labelled eta obligation.

---

## 13. Proof-status ledger, remaining bottleneck and computation scope

### 13.1 Compact ledger

| Statement | Status |
|---|---|
| Turn10 dyadic construction and turn11 full pair theorem | **Established reuse; audits complete under the gate** |
| Full $D_r=2^rr!$ payments | **Established reuse**, retained in every new identity |
| Exact weighted contact-jet identity | **PASS; rigorously derived** |
| Exact normalized atom-jet valuations | **PASS; rigorously derived** |
| Low-order contact parity | **PASS only for $r+j<16$** |
| Uniform source-minor lower divisor | **PASS; lower divisor only** |
| Selected source-unit minors $3,7,12$ | **PASS; unique attaining terms proved** |
| Complete corrected contents $19,39,72$ | **PASS on every original index** |
| Cramer divisions, odd pivot quotients, both borders and row payments | **PASS** |
| Residual pivots $13,19,32$ and $\nu_k=64+\nu_k^{[5]}$ | **PASS; exact payment, not an upper bound** |
| Signs and all-prime return to $G_k$ | **PASS** |
| Actual $q_k$ and nonzero whole error | **Preserved exactly** |
| All-order $\mathbb F_4$ formula and two-carry evaluation | **PASS; normalized parity only** |
| Source-unit test (11.4)–(11.5) | **New proved audit lemma** |
| Quantitative precision-window limit (11.8) | **New proved limitation of the criterion** |
| General corrected-cofactor conclusion | **Conditional on source-unit and $t_q<L_d$** |
| Growing corrected elimination and terminal joint coefficient depth | **Open** |
| Other odd-prime descents and large-prime exclusion | **Separate open obligations** |
| All-prime whole-error conclusion | **Not established by this audit** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

### 13.2 Exact remaining binary obligation

After all evaluated payments, the remaining quantity is the actual coefficient depth


$$
\boxed{
\nu_k^{[5]}
=
\min\bigl(v_2(P_{0,k}^{[5]}),v_2(P_{1,k}^{[5]})\bigr).
}
$$


The stated sufficient target remains


$$
\boxed{
\nu_k^{[5]}
\le \frac{15}{4}k^2-64+O(k\log k),
\qquad k=9^{18+32u}.
}
\tag{13.1}
$$



The exact obstruction is not entry evaluation. It is control of a growing corrected common-column lattice after bottom corrections become visible, followed by control of the **joint** terminal constant and linear coefficient depth.

The new source-unit lemma gives a precise, fully normalized binary certificate that an attempted flag must satisfy. It does not certify a flag merely by naming its determinant. Beyond the strict correction window, the complete corrected entries—not the pure rank-$d$ product—must enter the proof.

The odd-prime obligations remain independent. In particular, neither the oddness of the forcing determinant nor that of the $\mu_{q,k}$ proves the required descents at primes $p\ge5$ or excludes primes above $6k-5$.

Even the contemplated binary upper bound, together with the separate odd-prime bounds and the closed analytic estimate, would yield the previously stated conditional whole-error divergence for this producer. That would retire it as a source of primitive whole-error decay; it would not prove $e+\pi$ rational or irrational.

### 13.3 Bounded arithmetic and literature scope

No tools or remote code have been used.

No new bounded calculation is indispensable to the proofs in this report, and **no new calculation is proposed**. The local valuation table and its unique minima have been checked explicitly above. The parent’s completed finite comparison receipt is not rerun.

That receipt authenticates only its stated finite binomial and carry calculations. It does not verify an original-index growing minor, corrected flag, terminal coefficient pair or gcd bound.

Only the stated overlap scope of the supplied literature information is used. No theorem from an unread full paper, and no special single-sequence Hankel result, is imported into this corrected mixed pencil.

---

## Final conclusion

Both new mathematical tools pass the independent audit at their proper scope.

The complete cofactor recursion proves


$$
\boxed{
v_2(\mathscr C_k^{[3]})=19,\qquad
v_2(\mathscr C_k^{[4]})=39,\qquad
v_2(\mathscr C_k^{[5]})=72,
}
$$


with explicit attaining original-row minors and normalized Vandermonde residues. It gives actual residual pivots $13,19,32$ and the exact all-prime transfer


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d+d+69}\mathfrak D_d\,g_k^{[5]}.
}
$$


Consequently,


$$
\boxed{
v_2(G_k)=
d^2+4d+29+(d+4)s_2(d)
-3\sum_{n<d}s_2(n)
+64+\nu_k^{[5]}.
}
$$



The parent’s all-order $\mathbb F_4$ formula and two-carry algorithm also pass. They correctly evaluate the normalized contact-jet parity beyond the old cutoff, including the indispensable derivative contribution. The new audit lemma (11.4) identifies exactly how those evaluated entries enter the nominal source-unit test.

What remains unproved is the growing **corrected** elimination and the joint terminal coefficient bound. The correction-free criterion has only an $O(\sqrt d)$ range, and the pure product has insufficient rank for all $d+1$ common columns. Neither obstruction is removed by logarithmic-time entry evaluation or by a fixed finite arithmetic check.

The original domain, complete forcing and returns, finite boundaries, terminal, full divisors, actual contents and least clearer, all-prime final gcd, actual primitive denominator and nonzero whole error have been preserved throughout. No unconditional rationality or irrationality conclusion for $e+\pi$ has been obtained.
