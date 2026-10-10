> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Direct two-degree transfer on the even subsequence

Date: 2026-09-13. Original bounded derivation by audit_computations.

The accepted leading-minor theorem proves that $Q_n$ is cubic for every even $n\ge2$. This note constructs the direct transfer from $n$ to $n+2$, with denominator only $Q_n$, and proves its exact second-order differential and Volterra form. The estimates required to bound its coefficients uniformly remain open.

The polynomial convention throughout is the **reflected** factorial polynomial



$$
P_n(t)=\sum_{j=0}^n B_{n,j}\frac{t^{n-j}}{(n-j)!}.
$$



The earlier high-row integrals use $U_n(x)=P_n(1-x)$. Reflection preserves every norm and Legendre spectral projection used below; this note does not silently replace $F_k(x)$ in those high-row identities.

## 1. A direct rational transfer without an intermediate degree

Use the canonical normalization $B_n(1)=1,C_n(1)=4$, the three-column jet matrix $\Psi_n$ with columns $(R_n,B_ne^z,C_n)$, and the rational gauge matrix $K_n$ from `raw_hp_rational_degree_transfer.md`. Its exact factorization is



$$
\det K_n=z^{3n-1}Q_n,\qquad \Psi_n=K_nSG,
$$



where $SG$ is independent of the degree. Define directly



$$
\boxed{T_n^{[2]}=\Psi_{n+2}\Psi_n^{-1}
=K_{n+2}K_n^{-1}=\frac{N_n^{[2]}}{Q_n}.}
\tag{1}
$$



No degree-$n+1$ matrix is used in this definition.

For each numerator entry, Cramer's rule gives a determinant of two old jet rows and one new jet row. After undoing the universal gauge, every first-column remainder entry vanishes to order at least $3n-1$. Hence the polynomial mixed determinant has a factor $z^{3n-1}$, which cancels the same factor in $\det K_n$. This proves (1) without any assumption about the zeros of $Q_n$.

The precise degree bounds are



$$
\boxed{(\deg N_{rj}^{[2]})\le
\begin{pmatrix}6&7&7\\5&6&6\\4&5&5\end{pmatrix},
\qquad z\mid N_{r2}^{[2]}.}
\tag{2}
$$



Indeed the mixed rows now have total base degree $3n+2$. The first column adds four degrees; the first and third columns incur the derivative orders of the two chosen rows. Subtracting the two smallest possible derivative orders and then $3n-1$ gives the displayed bounds except the bottom-right entry, initially bounded by six. For that entry the maximizing first/third-column pair consists of the two old derivative rows zero and one. Their leading $A,C$ minor cancels, reducing the degree to five. Replacing old row two leaves old remainder derivatives only of orders zero and one, so the origin factor gains one further power of $z$, proving the last-column divisibility.

The determinant and differential compatibility identities are



$$
\boxed{\det T_n^{[2]}=z^6\frac{Q_{n+2}}{Q_n},\qquad
\det N_n^{[2]}=z^6Q_n^2Q_{n+2},}
\tag{3}
$$





$$
(T_n^{[2]})'=\mathcal C_{n+2}T_n^{[2]}-T_n^{[2]}\mathcal C_n,
\tag{4}
$$



where $\mathcal C_n$ is the old scalar-ODE companion matrix. These follow respectively by taking determinants and differentiating (1). The first transfer row defines an operator of order at most two,



$$
\mathcal S_n^{[2]}=
\frac{N_0+N_1\partial_z+N_2\partial_z^2}{Q_n},
\quad\deg(N_0,N_1,N_2)\le(6,7,7),
\tag{5}
$$



mapping each actual old fundamental column to its degree-$n+2$ counterpart.

Equations (1)–(5) actually hold at every degree, with $\deg Q_n\le3$. The integral and norm formulas below use that the **current** $Q_n$ is cubic. On the even subsequence this is now unconditional; no odd cubic-degree assertion is needed.

## 2. The three infinity cancellations

Put



$$
\mathsf A=N_0+N_1+N_2,\qquad
\mathsf B=N_1+2N_2,\qquad
\mathsf C=N_2,
$$



and write their coefficients as $a_d,b_d,c_d$, respectively. All indices outside $0,\ldots,7$ mean zero. Then



$$
Q_nB_{n+2}=\mathsf A B_n+\mathsf B B_n'+\mathsf C B_n''.
\tag{6}
$$



Because $Q_n$ is cubic, its infinity degree ledger supplies an exponential branch with polynomial degree $n$, and the algebraic Laurent plane has powers $n,n-1$. The latter is the span of $C_n$ and $A_n+C_n(\arctan z-F_\infty)$. The direct transfer carries this entire plane to the corresponding degree-$n+2$ plane, with both powers at most $n+2$.

The excessive algebraic numerator coefficient at degree $n+6$ and the two excessive exponential numerator coefficients at degrees $n+7,n+6$ therefore give



$$
N_{0,6}+nN_{1,7}=0,\qquad N_{1,7}+N_{2,7}=0,
$$




$$
N_{0,6}+N_{1,6}+N_{2,6}
 +nN_{1,7}+2nN_{2,7}=0.
\tag{7}
$$



In the last equation the possible first subleading coefficient of $B_n$ multiplies the already vanishing coefficient in the second equation. Thus no unproved coefficient ratio is used.

Write $\gamma=c_7$, $\delta=c_6$. Equivalently,



$$
\boxed{a_7=0,\quad b_7=\gamma,\quad a_6=-n\gamma,
\quad b_6=\delta-2n\gamma.}
\tag{8}
$$



These are the one-degree cancellations with their coefficient indices shifted by one, while the input degree remains $n$. Repeated roots, a root at zero, and a root at one cause no exception to (7)–(8).

## 3. The exact factorial transform and its two zero boundary data

Let $Jf(t)=\int_0^t f(s)\,ds$ and $\theta=t\partial_t$. Apply the coefficientwise reversed factorial transform at the common reference degree $n+7$ to (6). One obtains



$$
\sum_{d=0}^3 Q_dJ^{5-d}P_{n+2}
=\mathcal W_n^{[2]}P_n,
$$




$$
\mathcal W_n^{[2]}=
\sum_{j=0}^2\sum_{d=0}^7
\widetilde N_{j,d}J^{7+j-d}(n-\theta)_{\underline j},
\quad(\widetilde N_0,\widetilde N_1,\widetilde N_2)
=(\mathsf A,\mathsf B,\mathsf C).
\tag{9}
$$



For clarity, on a monomial coefficient $B_k z^k$, the right factorial denominator is exactly
$(n+7-d-k+j)!$; $(n-\theta)_{\underline j}$ contributes $(k)_{\underline j}$. On the left, the reference difference is
$(n+7)-(n+2+d)=5-d$. These identities explain why a two-degree jump does **not** increase the derivative order after transformation.

All integral powers in (9) are nonnegative, and $a_7=0$ removes the only potential $J^0$ term. Hence $\mathcal W_n^{[2]}P(0)=0$. Its first derivative at zero can receive contributions only from



$$
a_6JP+b_7J(n-\theta)P,
$$



and these sum to $(-n\gamma+n\gamma)P(0)=0$. Thus applying **two** derivatives to (9) loses no boundary data for any polynomial input: integrating twice recovers exactly (9).

## 4. A second-order Legendre operator and six Volterra terms

Define the explicit quadratics, for $0\le k\le7$,



$$
\boxed{V_k(t)=a_{5-k}+(n+k)b_{6-k}
 +(n+k)(n+k-1)c_{7-k}
 -t[b_{5-k}+2(n+k)c_{6-k}]+t^2c_{5-k}.}
\tag{10}
$$



The integrations by parts



$$
J^r(n-\theta)P=(n+r)J^rP-tJ^{r-1}P
$$



and



$$
J^r(n-\theta)_{\underline2}P
=(n+r)(n+r-1)J^rP
-2(n+r-1)tJ^{r-1}P+t^2J^{r-2}P
$$



hold for $r\ge1$ and $r\ge2$, respectively. At $r=1$, the second identity is instead read as
$n(n+1)JP-2ntP+t^2P'$. Their endpoint terms contain factors $t$ or $t^2$ and vanish at zero.

Using (8), the differentiated equation becomes



$$
\boxed{(Q_3I+Q_2J+Q_1J^2+Q_0J^3)P_{n+2}
=\mathcal D_n^{[2]}P_n,}
\tag{11}
$$





$$
\boxed{\mathcal D_n^{[2]}=
\gamma\mathscr L+\delta t(t-1)\partial_t
+V_0(t)+\sum_{k=1}^{6}V_k(t)J^k,}
\quad
\mathscr L=-[t(1-t)\partial_t]'.
\tag{12}
$$



In detail, before using the last relation in (8), the first-derivative coefficient is
$\delta t^2-[(2n-2)\gamma+b_6]t-\gamma$. Substituting $b_6=\delta-2n\gamma$ gives exactly the coefficient in (12); there is no uncontrolled unweighted $tP'$ term.

The absence of a seventh integral term is exact: (2) gives $c_0=N_2(0)=0$, so $V_7=(n+7)(n+6)c_0=0$. Thus the direct two-degree transfer introduces one more Volterra term than the one-degree formula, but no higher differential order.

The centered identity is also exact:



$$
\mathcal D_n^{[2]}=
\gamma(\mathscr L-n(n+1)I)
+\delta[t(t-1)\partial_t+n(1-2t)]
+W_0(t)+\sum_{k=1}^{6}V_k(t)J^k,
$$




$$
W_0(t)=a_5-b_5t+c_5t^2.
\tag{13}
$$



## 5. An explicit sufficient two-degree norm criterion

Normalize coefficients in (11)–(13) by $Q_3$, using bars. The same cubic Volterra operator as in the one-degree note occurs:



$$
H_n=I+(Q_2/Q_3)J+(Q_1/Q_3)J^2+(Q_0/Q_3)J^3
=\prod_{Q_n(\alpha)=0}(I-\alpha J).
$$



Every factor is invertible on $L^2(0,1)$, with the exact inverse and root bounds in `raw_hp_integral_transfer_operator.md`, Section 5. In particular, write $\Lambda_n$ for the proved upper bound there on $\|H_n^{-1}\|$. Root coalescence or a root at one is harmless. Uniform boundedness of $\Lambda_n$ is a sufficient hypothesis, not a conclusion of cubic degree alone.

For a polynomial $P$ of degree at most $n$, let $N=n(n+1)$. The spectral Legendre bound and its energy identity give



$$
\|\mathscr LP\|_2\le N\|P\|_2,
\qquad \|t(t-1)P'\|_2\le\frac{\sqrt N}{2}\|P\|_2,
\qquad \|J^k\|\le\frac1{k!}.
$$



Consequently the completely explicit sufficient condition



$$
\boxed{\Lambda_n\left[
|\bar\gamma|n(n+1)+\frac{|\bar\delta|\sqrt{n(n+1)}}2
+\|\bar V_0\|_\infty+
\sum_{k=1}^{6}\frac{\|\bar V_k\|_\infty}{k!}
\right]\le C(n+1)(n+2)}
\tag{14}
$$



implies



$$
\boxed{\|P_{n+2}\|_2\le C(n+1)(n+2)\|P_n\|_2.}
\tag{15}
$$



It is enough to establish, on the even subsequence,



$$
\Lambda_n\le L,\quad |\bar\gamma|\le G,\quad
|\bar\delta|\le D(n+1),
$$




$$
\|\bar V_0\|_\infty+
\sum_{k=1}^{6}\|\bar V_k\|_\infty/k!\le V(n+1)^2.
\tag{16}
$$



Then (15) holds with $C=L(G+D/2+V)$. The optimized constant-shift bound of the one-degree note can also replace the separate $|\bar\gamma|N+\|\bar V_0\|$ terms; its proof is unchanged.

Iterating (15) over even indices yields



$$
\boxed{\|P_{2m}\|_2\le(2m)!\exp(O(m)),\qquad
\|P_{2m}\|_1\le(2m)!\exp(O(m)).}
\tag{17}
$$



These are conditional on (14), or the stronger convenient bounds (16). The factorial comes from the exact product of the consecutive pairs $(n+1)(n+2)$, not from multiplying unproved one-degree estimates.

For the **actual** high-orthogonal inputs, the previously proved broad-band concentration and (13) give an optional relaxation: $\| (\mathscr L-N)P_n\|=O(n^2/\log n)\|P_n\|$. Thus one may replace $\bar\gamma=O(1)$ by $\bar\gamma=O(\log n)$, provided $\bar\delta=O(n)$, the combined $\bar W_0$ and Volterra terms are $O(n^2)$, and $\Lambda_n=O(1)$. This relaxation applies to the selected high-orthogonal family and is not a bound on every degree-n polynomial.

## 6. The two highest coefficients as direct leading-minor quotients

The leading-minor formulas of `raw_transfer_leading_minor_criterion.md` extend directly to this two-degree transfer. Write



$$
a=A_{n,n},\ a_1=A_{n,n-1},\ c=C_{n,n},\ c_1=C_{n,n-1},
\quad b=B_{n,n},\quad \beta=B_{n,n-1}/b,
$$




$$
d=A_{n+2,n+2},\ d_1=A_{n+2,n+1},\
f=C_{n+2,n+2},\ f_1=C_{n+2,n+1},
$$



where these coefficient letters are local to this section. Define



$$
\Xi=ac_1-a_1c+c^2,\qquad m_0=af-cd,
\quad m_1=af_1+a_1f-cd_1-c_1d.
$$



Then



$$
\boxed{\bar\gamma=\frac{m_0}{\Xi},\qquad
\bar\delta=\frac{m_1+\beta m_0}{\Xi}.}
\tag{18}
$$



To check the signs and degree difference, use at infinity
$H=A+C(\arctan-F_\infty)$, whose first two coefficients are
$a,a_1-c$. The numerator of the last entry in the first transfer row, before multiplying by $D^2$ and removing its origin factor, is



$$
(B+B')(H C_{n+2}-C H_{n+2})
-B(H'C_{n+2}-C'H_{n+2})
-B_{n+2}(HC'-H'C).
$$



Its top two coefficients are $bm_0$ and $bm_1+B_{n,n-1}m_0$: the $n b m_0$ contribution from $B'$ cancels the second displayed term. The last term starts two degrees below the leading degree and does not affect these coefficients. The factor $D^2$ has no relative $z^{-1}$ term. Dividing by $Q_3=b\Xi$ proves (18), with exactly the current and degree-$n+2$ canonical normalizations.

Thus the first two convenient bounds in (16) are precisely the direct even-minor conditions



$$
|m_0|\le G|\Xi|,\qquad
|m_1+\beta m_0|\le D(n+1)|\Xi|.
\tag{19}
$$



No intermediate odd triple occurs in these identities. The all-even nonvanishing of $\Xi$ justifies the quotients, but does not bound them in absolute value.

## 7. Verification and scope

`check_raw_direct_two_degree_transfer.py` verifies the complete operator identity symbolically on $t^r$ with arbitrary symbolic $n,r$, after imposing exactly (8) and $c_0=0$. It also checks the centered identity. As a separate normalization control, it reads only the already saved exact degree-two and degree-four triples, normalizes them by their saved $B(1)$, and verifies the direct matrix identity, degree bounds, determinant identity, all infinity cancellations, and the actual reflected-polynomial equation (11). No new canonical degree is solved and no coefficient fit is performed. Results are saved in `raw_direct_two_degree_transfer_checks.json`.

The direct even update removes every need for an intermediate odd cubic. Its denominator, Volterra inverse, and coefficient criterion depend only on the actual current even $Q_n$ and the direct transfer row. The outstanding work is to prove bounds such as (14) along that actual even orbit. Even if those bounds hold, a further estimate for the whole remainder's signed cancellation and its primitive arithmetic normalization is still required.
