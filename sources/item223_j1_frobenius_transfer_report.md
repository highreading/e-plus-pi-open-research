> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 223 — the $j=1$ boundary recurrence and its first Frobenius transfer

## 1. Outcome

This item starts from the exact endpoint formulas of Item 220 and attacks the
$j=1$ pair through boundary-vanishing moments. It obtains a genuine all-row
transfer theorem and an exact exclusion of the symmetric diagonal. The
remaining off-diagonal transfer survivors are not classified all-prime.

The main exact conclusions are:

1. After reciprocal conversion, both Item 220 endpoint conditions use the
   same boundary functional. With
   

$$
W(z)=(1-z)^r(1+z^2)^{2s-1},\qquad n_*=p+r,
$$


   put $u_t=\mathcal L_\epsilon(z^{n_*+t}W)$. The two common-log
   conditions reduce exactly to
   

$$
(u_0,u_1,u_2)=\lambda(1,1,-1).             \tag{1.1}
$$


2. Away from its two Frobenius poles, the shifted moments satisfy modulo
   $p$ the order-three Pearson recurrence
   

$$
\boxed{\begin{aligned}
   (2r+4s+t+2)u_{t+3}={}&(r+t+1)u_t-(2r+t+2)u_{t+1}\\
                         &+(r+4s+t+1)u_{t+2}.
   \end{aligned}}                                               \tag{1.2}
$$


3. Transfer of the line (1.1) reaches two first Frobenius resonances. The
   exact lifted recurrence has multipliers $p$ and $2p$ at the lower and
   upper poles, so their nonzero sources are respectively
   $-2\epsilon$ and $-4\epsilon$. If $\Delta_-$ and $\Delta_+$ are
   the corresponding normalized line transfers, every actual collision must
   satisfy
   

$$
\boxed{\Delta_+=2\Delta_-\ne0\pmod p.}       \tag{1.3}
$$


   Thus $\Theta:=\Delta_+-2\Delta_-\ne0$, or either transfer being zero,
   is an exact all-row noncollision certificate.
4. Both transfers have explicit binomial-coefficient formulas. No hidden
   numerical linear algebra is involved.
5. On the actual diagonal
   

$$
r=2s,\qquad p=10s+3,                 \tag{1.4}
$$


   the recurrence has the involution $v_t=-v_{3-t}$, which forces
   $\Delta_+=\Delta_-$ identically. Combined with (1.3), this proves an
   exact all-prime noncollision theorem on the whole diagonal family (1.4).

No all-prime exclusion of the remaining off-diagonal transfer survivors is
proved.
Consequently Item 223 books no positive Route-1 logarithmic rate and no new
divisibility exponent.

## 2. Actual phase and the common boundary functional

For $j=1$, write



$$
p=4h+6s+3=2r+6s+3,\qquad r=2h,\qquad h,s\geq1,                 \tag{2.1}
$$


and


$$
\epsilon=(-1)^{(p-1)/2}=(-1)^{s+1}.                           \tag{2.2}
$$


Item 220 uses


$$
\begin{aligned}
P_0&=(1-z)^r(1+z)(1+z^2)^{2s},\\
P_1&=(1-z)^r(1+z)^4(1+z^2)^{2s-1},                             \tag{2.3}
\end{aligned}
$$


and Euler resolvents $V_\nu$ with


$$
N_\nu=2p-2s+\nu-1,\qquad
 d_\nu=\deg P_\nu=r+1+\nu+4s.                                  \tag{2.4}
$$


Both $P_\nu$ are self-reciprocal because $r$ is even, and


$$
N_\nu-d_\nu-1=p+r=:n_*                  \tag{2.5}
$$


is independent of $\nu$. Therefore, for $\zeta=\pm i$,


$$
V_\nu(\zeta)=\zeta^{N_\nu}
       \int_0^{\zeta^{-1}} z^{n_*}P_\nu(z)\,dz.                 \tag{2.6}
$$



Define the polynomial boundary functional


$$
\mathcal L_\epsilon(f)=
 (2\epsilon-i)\int_0^{-i}f(z)\,dz
 +(2\epsilon+i)\int_0^i f(z)\,dz.                              \tag{2.7}
$$


The phases in (2.6) are


$$
i^{N_0}=-i\epsilon,\quad(-i)^{N_0}=i\epsilon,\qquad
 i^{N_1}=(-i)^{N_1}=\epsilon.                                  \tag{2.8}
$$


Consequently Item 220's two primitive endpoint forms satisfy


$$
\begin{aligned}
C_0-2\epsilon S_0
  &=\frac{\epsilon}{2}\mathcal L_\epsilon(z^{n_*}P_0),\\
2C_1+\epsilon S_1
  &=\frac12\mathcal L_\epsilon(z^{n_*}P_1).                    \tag{2.9}
\end{aligned}
$$


Only the displayed nonzero scalars were removed. Thus the two apparently
different endpoint lines really are one common boundary functional.

## 3. The minimal common weight and Pearson recurrence

Factor the gcd weight


$$
W=(1-z)^r(1+z^2)^{2s-1}.                                      \tag{3.1}
$$


Then


$$
P_0=(1+z)(1+z^2)W,\qquad P_1=(1+z)^4W.                         \tag{3.2}
$$


For every integer $t$ in the nonresonant transfer range, set


$$
u_t=\mathcal L_\epsilon(z^{n_*+t}W).  \tag{3.3}
$$



Put $\sigma=(1-z)(1+z^2)$. Direct differentiation gives the exact
Pearson identity


$$
(\sigma W)'=\bigl(-(r+1)+4sz-(r+4s+1)z^2\bigr)W.              \tag{3.4}
$$


The endpoint values of
$z^{n_*+t+1}\sigma W$ vanish at $0,i,-i$. Integrating its derivative
under (2.7) gives the exact rational identity


$$
\begin{aligned}
(p+2r+4s+t+2)u_{t+3}={}&(p+r+t+1)u_t\\
 &-(p+2r+t+2)u_{t+1}+(p+r+4s+t+1)u_{t+2}.       \tag{3.5}
\end{aligned}
$$


For $p$-integral moments, reducing (3.5) modulo $p$ gives (1.2).
Keeping the added $p$'s in (3.5) is essential at the two poles.

The recurrence has three states rather than the four states of the direct
$P_0$ recurrence because (3.1) removes the two multipliers in (3.2) while
retaining all three boundary roots $1,i,-i$.

## 4. Reduction of the collision pair to one initial line

Equations (2.9) and (3.2) give


$$
\begin{aligned}
u_0+u_1+u_2+u_3&=0,\\
u_0+4u_1+6u_2+4u_3+u_4&=0.                                    \tag{4.1}
\end{aligned}
$$


At $t=0,1$, the leading recurrence coefficients are respectively


$$
2r+4s+2=p-(2s+1),\qquad 2r+4s+3=p-2s,                         \tag{4.2}
$$


so they are $p$-units. Eliminating $u_3,u_4$ from (4.1) with (1.2)
gives the equivalent two rows


$$
\begin{pmatrix}
3r+4s+3&4s&3r+8s+3\\
7r+16s+11&4s&-r-4s-1
\end{pmatrix}
\begin{pmatrix}u_0\\u_1\\u_2\end{pmatrix}=0.                   \tag{4.3}
$$


Subtracting the rows first gives


$$
(r+3s+2)u_0-(r+3s+1)u_2=0.                                   \tag{4.4}
$$


Since $2(r+3s+1)=p-1$, (4.4) yields $u_2=-u_0$; the first row then
gives $u_1=u_0$. The rank is exactly two because the first two-column
minor is


$$
-16s(r+3s+2)\equiv-8s\not\equiv0\pmod p.                     \tag{4.5}
$$


This proves (1.1), including the zero value $\lambda=0$ at this stage.

## 5. The two first Frobenius sources

For a monomial, write


$$
\mathcal L_\epsilon(z^q)=\frac{\ell_q}{q+1},\qquad
 \ell_q=(2\epsilon-i)(-i)^{q+1}+(2\epsilon+i)i^{q+1}.          \tag{5.1}
$$


The numerator is an ordinary integer. At the two relevant extremes,


$$
\ell_{p-1}=-2\epsilon,\qquad
                       \ell_{2p-1}=-4\epsilon.                 \tag{5.2}
$$



All state moments used between the resonances have denominators strictly
between $p$ and $2p$, hence are $p$-integral. More explicitly, the
transfer uses $-r\leq t\leq2s+3$. At the lower adjacent index
$t=-r-1$, only the constant coefficient $W(0)=1$ has denominator
$p$. At the upper adjacent index $t=2s+4$, only the leading coefficient
of $W$, also $1$, has denominator $2p$. Therefore


$$
\begin{aligned}
p\,\mathcal L_\epsilon(z^{p-1}W)&\equiv-2\epsilon,\\
p\,\mathcal L_\epsilon(z^{n_*+2s+4}W)&\equiv-2\epsilon
                                                               \tag{5.3}
\end{aligned}
$$


modulo $p$. These are moment residues, not yet the terminal recurrence
sources. At $t=-r-1$, the coefficient of the lower pole in the exact
identity (3.5) is $p$. At $t=T=2s+1$, the coefficient of the upper pole
is


$$
p+2r+4s+T+2=2p.                                               \tag{5.4}
$$


Consequently the two terminal recurrence sources are


$$
-2\epsilon\quad\hbox{and}\quad-4\epsilon, \tag{5.5}
$$


respectively. Dropping the extra $p$ in (3.5) would incorrectly identify
these sources; both the pole residue and its exact multiplier are essential.

## 6. Transfer scalars and the determinant theorem

Let $v_t$ be the formal recurrence solution normalized by


$$
(v_0,v_1,v_2)=(1,1,-1).                \tag{6.1}
$$


Propagate (1.2) forward for $0\leq t<T$, where


$$
T=2s+1.                          \tag{6.2}
$$


All leading coefficients are


$$
2r+4s+t+2=p-(T-t)\in\{p-T,\ldots,p-1\},       \tag{6.3}
$$


so the transfer is invertible. Its state-matrix determinant is


$$
\prod_{t=0}^{T-1}\frac{r+t+1}{2r+4s+t+2},                    \tag{6.4}
$$


a $p$-unit. Define the upper terminal covector


$$
\Delta_+=(r+T+1)v_T-(2r+T+2)v_{T+1}
                +(r+4s+T+1)v_{T+2}.                            \tag{6.5}
$$



Likewise propagate backward for $-r\leq t<0$. The solved coefficients
are $r,r-1,\ldots,1$, all units. Define


$$
\Delta_-=(r+1)v_{-r}-4sv_{-r+1}+(r+4s+1)v_{-r+2}.              \tag{6.6}
$$



If an actual collision exists, its state is $\lambda v_t$ throughout
both nonresonant intervals. Applying (5.3)--(5.5) at the two ends gives


$$
\lambda\Delta_+=-4\epsilon,\qquad
                 \lambda\Delta_-=-2\epsilon.                   \tag{6.7}
$$


Since both sources are nonzero, (6.7) proves


$$
\lambda\ne0,\qquad
                 \Delta_+=2\Delta_-\ne0\pmod p.                \tag{6.8}
$$


Equivalently, the two-source transfer determinant


$$
\det\begin{pmatrix}\Delta_+&-4\epsilon\\
                     \Delta_-&-2\epsilon\end{pmatrix}
       =-2\epsilon(\Delta_+-2\Delta_-)                         \tag{6.9}
$$


must vanish. This is the strongest all-row theorem of Item 223.

## 7. Closed coefficient formulas

Set


$$
D_n(r,s)=[x^n]\frac1{(1-x)^{r+1}(1+x^2)^{2s}}.                \tag{7.1}
$$


It has the explicit integer sum


$$
D_n(r,s)=\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^j
   \binom{2s+j-1}{j}\binom{r+n-2j}{n-2j}.                      \tag{7.2}
$$


The two transfer scalars are


$$
\boxed{\begin{aligned}
\Delta_+\equiv{}&(2r+4s-1)D_{2s+4}+(r+1)D_{2s+3}
                    -(r+8s)D_{2s+2}\pmod p,\\
\Delta_-={}&-(r+3)D_{r+3}+(3r+5)D_{r+2}
                    -(2r+4s+2)D_{r+1}.
\end{aligned}}                                                 \tag{7.3}
$$


The second identity is an equality over the integers for the normalization
(6.1); the first is the exact Frobenius residue modulo $p$.

For completeness, if $F(x)=\sum_{t\geq0}v_tx^t$, its recurrence gives


$$
x(1-x)(1+x^2)F'+QF=R,                                        \tag{7.4}
$$


where


$$
\begin{aligned}
Q={}&2r+4s-1-(r+4s-1)x+(2r+1)x^2-(r+1)x^3,\\
R={}&2r+4s-1+(r+1)x-(r+8s)x^2.
\end{aligned}                                                  \tag{7.5}
$$


The integrating factor


$$
\frac{x^{2r+4s-1}}{(1-x)^r(1+x^2)^{2s-1}}                    \tag{7.6}
$$


shows that the first denominator divisible by $p$ occurs at coefficient
$2s+4$, yielding the first line of (7.3). Applying the same calculation
to the reversed sequence $b_j=v_{2-j}$ gives the second line. Thus (7.3)
is a closed coefficient theorem, not a guessed finite recurrence.

## 8. Exact all-prime diagonal exclusion

Take $r=2s$, set $T=2s+1$, and note


$$
p=10s+3=5T-2.                          \tag{8.1}
$$


Direct substitution into (1.2) modulo $p$ shows that the involution


$$
v_t\longmapsto-v_{3-t}            \tag{8.2}
$$


preserves the recurrence. The initial line supplies
$v_0=-v_3$ and $v_1=-v_2$; uniqueness across the nonresonant intervals
therefore gives


$$
v_t=-v_{3-t}                      \tag{8.3}
$$


through both transfers.

The upper state $(v_T,v_{T+1},v_{T+2})$ is consequently the reversed
negative of $(v_{-r},v_{-r+1},v_{-r+2})$. Using $p=5T-2$ in the two
terminal covectors proves


$$
\Delta_+=\Delta_-\pmod p.         \tag{8.4}
$$


But a collision would require (6.8). Combining (6.8) with (8.4) gives
$\Delta_-=0$, contradicting the nonzero clause in (6.8). Therefore


$$
\boxed{\text{the original common-log pair cannot vanish on any actual
 diagonal row }r=2s.}                                         \tag{8.5}
$$


These are genuine admissible $j=1$ rows, with $h=s$, $m=7s+2$, and
$p=10s+3$. This is an all-prime theorem, not a finite scan.

## 9. Finite replay, kept separate

The deterministic replay enumerates all $22,934$ admissible rows with
$p\leq2000$. It finds


$$
\begin{array}{c|r}
\Delta_+=0&29\\
\Delta_-=0&22\\
\Theta=\Delta_+-2\Delta_-=0&22\\
\text{diagonal rows among the 22}&0\\
\text{direct paired zeros among the 22}&0.
\end{array}                                                     \tag{9.1}
$$


The first two $\Delta_+=0$ rows are


$$
(p,r,s;\Delta_-,Q_0,Q_1)=(19,2,2;3,14,5),
 (47,4,6;34,17,23).                                            \tag{9.2}
$$


They illustrate why a claim based only on $\Delta_+\ne0$ would be false;
the two-source determinant excludes them because (6.8) fails.

There are 22 off-diagonal determinant survivors through this bound.
The first two are


$$
(p,r,s;\Delta_+,Q_0,Q_1)=(223,38,24;123,67,128),
$$




$$
(239,40,26;11,230,178).                                        \tag{9.3}
$$


The full 22-row survivor stream has SHA-256
05ebc18f04d538fb4e968b0a8c54c774df3d1d43522455c4d49ab97a76e2d608.

All counts in (9.1)--(9.3) are labeled **EXACT_FINITE_ONLY**. They prove
neither a density estimate nor an all-prime theorem.

## 10. Rate and scope

The full $j=1$ cell has conditional removable mass $1/6$ per $m$, as
recorded in Items 217--220. Item 223 proves noncollision on every row that
fails (6.8), but it does not give a uniform prime-log bound for the rows that
satisfy (6.8). It excludes the full diagonal (8.1), but that thin phase by
itself supplies no positive linear log-mass estimate, and no theorem bounds
all off-diagonal survivors.

Therefore the currently bookable quantities remain


$$
\boxed{\text{new unconditional linear log rate}=0,\qquad
        \text{new divisibility exponent}=0.}                   \tag{10.1}
$$



The rigorous next target is a second resonance covector independent of
(6.9) on the remaining off-diagonal rows.

## 11. Reproducibility and labels

The companion standard-library checker verifies the reciprocal phases,
both resonance sources, the Pearson identity, the initial rank-two line,
all transfer denominator ranges, both closed formulas, the diagonal
involution/exclusion, and the finite survivor replay. Canonical and replay JSON are
deterministic and byte-identical.

Classification:

* **PROVED:** (2.1)--(8.5), including the all-row implication
  $\Delta_+=2\Delta_-\ne0$ and the exact diagonal exclusion.
* **EXACT_FINITE_ONLY:** the counts and direct survivor checks through
  $p\leq2000$.
* **OPEN:** noncollision on every remaining off-diagonal transfer survivor; a higher
  independent resonance; any positive Route-1 rate or radical saving.
