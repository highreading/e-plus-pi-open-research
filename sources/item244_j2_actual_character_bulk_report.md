> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 244 — Abel reduction of the actual $j=2$ character bulk

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Continue in the normalized fixed $j=2$, $s\ge2$ cell.  Recall



$$
r=\frac{p-6s-3}{2},\qquad
 P_\nu(z)=(1-z)^r(1+z)^{1+3\nu}(1+z^2)^{2s-\nu},
 \quad\nu=0,1.                                       \tag{1.1}
$$



Write $P_\nu(z)=\sum_\ell c_{\nu,\ell}z^\ell$ and
$n_\ell=r+\ell+1$.  Item 241 isolated, at odd
$n=2u+1$, the variable character part



$$
\frac{90R_u}{2u+1},\qquad
 R_u=(-1)^u\mathcal O_u,\qquad
 \mathcal O_u=\sum_{j=0}^{u-1}\frac{(-1)^j}{2j+1}.   \tag{1.2}
$$



This item performs exact summation by parts against the actual
coefficients $c_{\nu,\ell}$.

> **PROVED — actual-family aggregate identity.**  Let $\mathsf S_\nu$
> be the old sine-endpoint period in (4.2), and let $\mathsf B_\nu$ be
> the single terminally normalized bulk scalar in (4.5).  Then
> 

$$
> \boxed{
> K_\nu=K_\nu^{\rm base}
> +90\mathcal O_L\mathsf S_\nu-90\mathsf B_\nu,}
> \qquad L=\left\lceil\frac r2\right\rceil.           \tag{1.3}
>
$$


> Here $K_\nu^{\rm base}$ is the aggregate of every term in the
> Item 241 kernel except $90R_u/(2u+1)$.  Thus (1.3) is an identity on
> the actual $P_\nu$ family, not a coefficientwise state statement.

> **PROVED — one canonical residual after Abel reduction.**  The two
> backward recurrences
> 

$$
> Q_{D+1}=0,\quad Q_k=\frac{d_k}{N_k}-Q_{k+1},
> \qquad
> B_D=0,\quad B_k=B_{k+1}+\frac{Q_{k+1}}{N_k}         \tag{1.4}
>
$$


> uniquely define $\mathsf B_\nu=B_0$.  One exact Abel step therefore
> leaves one scalar bulk moment beyond the known endpoint boundary term.
> This is a canonical one-residual normal form, not a claim that
> $B_0$ is algebraically independent of every larger harmonic state.

> **PROVED — exact zero-projection family.**  The odd-denominator
> projection of $P_\nu$ vanishes exactly when $\nu=0,r=1$.  On this
> line $p=6s+5$, $P_0=(1-z^2)(1+z^2)^{2s}$ is even, so the entire
> variable character aggregate, including $\mathsf B_0$, is absent.

> **PROVED SCOPED COUNTEREXAMPLES.**  The residual does not vanish
> identically: on the actual row $(p,s,\nu)=(17,2,1)$,
> $\mathsf B_\nu=9$ and the character aggregate is $7\pmod {17}$.
> Nor is $\mathsf B_\nu$ a common coordinate-independent multiple of
> $\mathsf S_\nu$: at $(p,s)=(19,2)$, the two ratios are $5$ and
> $12\pmod {19}$.  More general collapse into a larger collection of
> known harmonic states remains open.

> **GLOBAL INTERFACE.**  Equation (1.3) simplifies only the stronger
> $p^3$ carry from Item 239.  It does not strengthen the ordinary
> common-log gate $p^2\mid C_0,C_1$ and books no capacity.

> **EXACT FINITE ONLY.**  Through $p\le401$, the replay covers 1,115
> admissible rows and 2,230 coordinates.  It sees 38 zero projections,
> six additional zeros of $B_0$ on nonempty projections, and 17 zeros
> of the full variable character aggregate.  No asymptotic inference is
> made from these counts.

## 2. The exact actual-family parity projection

Put



$$
a_\nu=1+3\nu,\qquad q_\nu=2s-\nu,\qquad
 \delta\equiv r\pmod2,\quad\delta\in\{0,1\},
 \qquad L=\left\lceil\frac r2\right\rceil.           \tag{2.1}
$$



Define the polynomial of exactly those coefficients that give odd
denominators:



$$
D_\nu(t)=\sum_{k\ge0}d_{\nu,k}t^k,\qquad
 d_{\nu,k}=c_{\nu,2k+\delta}.                         \tag{2.2}
$$



Indeed, if $r=2\rho+\delta$, then



$$
n_{2k+\delta}=2(L+k)+1.                              \tag{2.3}
$$



The parity projection is



$$
z^\delta D_\nu(z^2)
 =\frac{P_\nu(z)+(-1)^\delta P_\nu(-z)}2.            \tag{2.4}
$$



Set



$$
b=\min(r,a_\nu),\qquad R=|r-a_\nu|,qquad
 E_{R,\delta}(t)=
 \sum_{j\ge0}\binom R{2j+\delta}t^j.                \tag{2.5}
$$



Factoring the common powers in (2.4) gives the exact integer identity



$$
\boxed{
D_\nu(t)=\sigma(1-t)^b(1+t)^{q_\nu}E_{R,\delta}(t),
\qquad
\sigma=\begin{cases}
(-1)^\delta,&r\ge a_\nu,\\
1,&r<a_\nu.
\end{cases}}                                         \tag{2.6}
$$



To see the sign, if $r\ge a_\nu$, the remaining bracket is



$$
\frac{(1-z)^R+(-1)^\delta(1+z)^R}{2},               \tag{2.7}
$$



whose surviving powers $z^{2j+\delta}$ have coefficient
$(-1)^\delta\binom R{2j+\delta}$.  If $r<a_\nu$, the two signs in
(2.7) are interchanged and the surviving coefficient is positive.

All exponents in (2.6) are less than $p$.  Hence reduction modulo
$p$ preserves nonzeroness of every nonempty factor.  The parity
polynomial can vanish only when $E_{R,\delta}$ is empty, namely
$R<\delta$.  This is equivalent to $R=0,\delta=1$, so $r=a_\nu$
is odd.  Since $a_0=1$ and $a_1=4$,



$$
\boxed{D_\nu=0\iff \nu=0\text{ and }r=1.}            \tag{2.8}
$$



On this line, $p=6s+5$, and the displayed even form of $P_0$ proves
the same conclusion directly.

## 3. The isolated actual character aggregate

Assume first that $D_\nu\ne0$, and let $D=\deg D_\nu$.  Suppress
$\nu$ temporarily and put



$$
N_k=2(L+k)+1,qquad w_k=\frac{d_k}{N_k},
 \qquad 0\le k\le D.                                 \tag{3.1}
$$



The degree/range audit inherited from Item 239 gives



$$
1\le N_k<p.                                         \tag{3.2}
$$



Thus every displayed inverse is legitimate.  The variable character
part of the actual aggregate is



$$
\mathcal M_\nu
 =90\sum_{k=0}^D w_kR_{L+k}.                          \tag{3.3}
$$



The Item 241 prefix recurrence is



$$
R_{u+1}+R_u=-\frac1{2u+1}.                           \tag{3.4}
$$



## 4. Exact Abel summation

Define the terminally normalized alternating tails



$$
Q_{D+1}=0,qquad Q_k=w_k-Q_{k+1}.                    \tag{4.1}
$$



Then



$$
Q_k=\sum_{v=k}^D(-1)^{v-k}w_v.                      \tag{4.2}
$$



The old sine-endpoint period is



$$
\mathsf S_\nu
 =\sum_{k=0}^D\frac{(-1)^{L+k}d_k}{N_k},
 \qquad Q_0=(-1)^L\mathsf S_\nu.                    \tag{4.3}
$$



For odd $n=2u+1$, the Item 219 endpoint weight satisfies



$$
J_\chi(n)=-2\chi(-1)^u,qquad
 \chi=(-1)^{(p-1)/2}.                                \tag{4.4}
$$



Therefore $\mathsf S_\nu$ is exactly $-1/(2\chi)$ times the old
$J_\chi$-endpoint period, not a new state.

Define the single residual bulk scalar by



$$
B_D=0,\qquad
 B_k=B_{k+1}+\frac{Q_{k+1}}{N_k}\quad(0\le k<D),
 \qquad \mathsf B_\nu=B_0.                           \tag{4.5}
$$



Since $w_k=Q_k+Q_{k+1}$, equations (3.3)--(3.4) give



$$
\begin{aligned}
\frac{\mathcal M_\nu}{90}
&=\sum_{k=0}^D(Q_k+Q_{k+1})R_{L+k}\\
&=Q_0R_L+
  \sum_{k=0}^{D-1}Q_{k+1}(R_{L+k}+R_{L+k+1})\\
&=Q_0R_L-\sum_{k=0}^{D-1}\frac{Q_{k+1}}{N_k}.        \tag{4.6}
\end{aligned}
$$



Finally $R_L=(-1)^L\mathcal O_L$, so (4.3), (4.5), and (4.6)
prove



$$
\boxed{
 \mathcal M_\nu
 =90\mathcal O_L\mathsf S_\nu-90\mathsf B_\nu.}    \tag{4.7}
$$



Both recurrences in (4.1), (4.5) have fixed terminal value and are
therefore unique.  This makes $\mathsf B_\nu$ a canonical single
residual of this Abel normal form.  It does not prove that another,
larger cohomology or harmonic system cannot absorb that scalar.

## 5. The complete actual carry

Let $K_p^{\rm base}(n)$ be the Item 241 formula with the variable term



$$
\mathbf1_{2\nmid n}\frac{90R_{(n-1)/2}}n           \tag{5.1}
$$



deleted, and define



$$
K_\nu^{\rm base}
 =\sum_\ell c_{\nu,\ell}K_p^{\rm base}(n_\ell).     \tag{5.2}
$$



Then (4.7) proves the promised actual-family identity



$$
\boxed{
 K_\nu=K_\nu^{\rm base}
 +90\mathcal O_L\mathsf S_\nu-90\mathsf B_\nu.}     \tag{5.3}
$$



If $D_\nu=0$, set $\mathsf S_\nu=\mathsf B_\nu=0$; (5.3) remains
valid and the variable character term is absent.

## 6. Exact scoped obstructions and finite census

The row $(p,s)=(17,2)$ has $r=1$.  For $\nu=0$, (2.8) gives the
automatic zero projection.  For $\nu=1$, direct exact evaluation of
(4.1), (4.5) gives



$$
\mathsf S_1=7,\qquad \mathsf B_1=9,\qquad
 \mathcal M_1=7\pmod {17}.                            \tag{6.1}
$$



Thus $\mathsf B_\nu$ does not vanish identically on the actual family.
At $(p,s)=(19,2)$, both old sine periods are nonzero, and



$$
\frac{\mathsf B_0}{\mathsf S_0}=5,qquad
 \frac{\mathsf B_1}{\mathsf S_1}=12\pmod {19}.       \tag{6.2}
$$



This rules out a common scalar multiple of the old sine period at fixed
$(p,s)$.  It does not rule out a coordinate-dependent formula or a
relation involving additional known harmonic aggregates.

The exact finite census through $p\le401$ contains



$$
\begin{array}{c|r}
\text{quantity}&\text{count}\\ \hline
\text{admissible rows}&1115\\
\text{coordinates}&2230\\
D_\nu=0&38\\
D_\nu\ne0,\ \mathsf B_\nu=0&6\\
D_\nu\ne0,\ \mathcal M_\nu=0&17.
\end{array}                                           \tag{6.3}
$$



The 38 zero projections are exactly the $r=1,\nu=0$ rows from (2.8).
The other counts are finite evidence only.

## 7. Replay, status, and booking

The standard-library checker `item244_j2_actual_character_bulk_certificate.py`:

1. reconstructs the actual parity projection (2.6);
2. checks exact agreement between direct aggregation and
   the uniquely normalized recurrences (4.1), (4.5);
3. identifies $\mathsf S_\nu$ with the old Item 219 endpoint;
4. checks the aggregate identity (5.3) against the complete Item 241
   kernel; and
5. replays the exact witnesses (6.1)--(6.2) and the bounded census.

The symbolic derivations in Sections 2 and 4 prove the identities for
all admissible rows; the bounded replay is not their proof.

From the archive root, run:

    python scripts/item244_j2_actual_character_bulk_certificate.py --output results/item244_j2_actual_character_bulk_certificate.json
    python scripts/item244_j2_actual_character_bulk_certificate.py --output results/item244_j2_actual_character_bulk_certificate_replay.json

Canonical and replay outputs are byte-identical and contain no host path,
timestamp, random seed, or elapsed time.

### Status ledger

**PROVED**

- the exact actual-family parity projection and its zero classification;
- the old endpoint normalization (4.3)--(4.4);
- the unique two-scalar propagation and one-residual Abel normal form;
- the complete aggregate identity (5.3); and
- the scoped exact witnesses (6.1)--(6.2) and range/unit audit.

**EXACT FINITE ONLY**

- the 1,115-row, 2,230-coordinate census through $p\le401$; and
- the six and 17 nonempty-projection zero counts in (6.3).

**OPEN**

- collapse $\mathsf B_\nu$ into a larger known aggregate state, or
  prove that no such actual-family collapse exists;
- classify zeros of $\mathsf B_\nu$ for all admissible rows;
- classify simultaneous $j=2$ common-log zeros; and
- obtain any Route-1 rate or capacity reduction.

The booking is



$$
\boxed{
\text{new unconditional log rate}=0,\qquad
\text{new divisibility exponent}=0,\qquad
\text{capacity reduction}=0.}                        \tag{7.1}
$$



Item 244 proves no statement about the arithmetic nature of $e+\pi$.
