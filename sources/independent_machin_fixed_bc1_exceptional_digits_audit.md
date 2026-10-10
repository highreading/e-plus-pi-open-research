> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the fixed-$(b,c)=(1,1)$ exceptional-digit branch

Date: 2026-08-26

## Verdict

**ACCEPT, with exactly the pointwise limitation stated in the source.**  The
scaled singular formula, the regular-term separation, the complete
classification for positive odd $N<239^3$, all three next-digit
certificates, and the adjacent-pair denominator theorem rederive correctly.
The recurrence proves an $N-O(\log N)$ exponent for at least one index in
each sufficiently large adjacent odd pair.  It does not prove that bound at
every odd index, and no finite calculation was treated as evidence for such
a pointwise theorem.

Two proof/markup defects found during this audit were corrected before the
final source hash was frozen:

1. The valuation argument for the recurrence originally did not treat
   $F_N=0$.  The final source adopts $v_p(0)=+\infty$, observes that the
   positive numerator of $H_N$ makes $H_N\ne0$, and handles either possible
   zero directly from the recurrence.
2. Displays (17) and (20) originally omitted their closing `\]` delimiters.
   The final source includes both closers; all display and inline delimiters
   are now balanced and correctly ordered.

The accepted, frozen artifacts have SHA-256 hashes

* `sources/machin_fixed_bc1_exceptional_digits.md`:
  `d898766a1873da918a945b2a464de859b668d56ab65973d817217d901558e8d7`;
* `scripts/machin_fixed_bc1_exceptional_digits.py`:
  `b3e2e4d82b9e5ae3ebbb9c528508a73896495cd146fb20fcb4e9e89135587b7b`;
* `results/machin_fixed_bc1_exceptional_digits.json`:
  `e9045ea99af4ab9932851bb8b17e1f108d580bc152f4d8298749a979ae1eac96`.

## 1. Exact singular normalization and regular gap

Put $p=239$, $D_N=N^2+N-1$, and
$s_r=(-1)^{(r-1)/2}$ for positive odd $r$.  In the endpoint-ratio formula
from the parent note, the two copies of the final Machin coefficient have
combined coefficient

$$
-\left(1+\frac1{D_N}\right)
=-\frac{N(N+1)}{D_N}.
$$

Since

$$
g_N=s_N\left(\frac{16}{N5^N}-\frac4{Np^N}\right),
$$

their singular part is exactly

$$
\frac{4s_N(N+1)}{D_Np^N}.
$$

Every earlier odd coefficient contributes $4s_r/(rp^r)$.  Thus, after
suppressing the common $p$-adic unit $4$, the source's decomposition
$R_N=4h_N+Q_N$ has

$$
h_N=\sum_{\substack{1\le r<N\\r\ \mathrm{odd}}}
       \frac{s_r}{rp^r}
     +\frac{s_N(N+1)}{D_Np^N}.
$$

Write

$$
a=v_p(N+1),\qquad d=v_p(D_N),\qquad W_*=N-a+d,
$$

and let $W$ be the maximum of $W_*$ and all
$w(r)=r+v_p(r)$.  If $r=p^{e_r}u_r$, $N+1=p^aU$, and
$D_N=p^dV$, multiplication by $p^W$ gives the exact identity in
$\mathbf Z_{(p)}$

$$
p^Wh_N=
\sum_{\substack{1\le r<N\\r\ \mathrm{odd}}}
s_rp^{W-r-e_r}u_r^{-1}
+s_Np^{W-W_*}UV^{-1}.
$$

This proves both the leading residue and the higher-digit rule.  Modulo
$p^k$, an earlier term is present exactly when $W-w(r)<k$, and the final
term is present exactly when $W-W_*<k$.

The claimed lower bound for the omitted part also checks term by term.
With

$$
L=\lfloor\log_pN\rfloor,\qquad
f=v_p((N+1)!),\qquad b=v_p(N+2),
$$

the earlier $5$-power terms, combined final $5$-power term, exponential
partial sum, and last factorial term have scaled valuations at least

$$
W-L,\qquad W+a-d,\qquad W-f,\qquad W-f-d+b,
$$

respectively.  Therefore their minimum is the stated $\Gamma_N$.  If the
singular calculation has valuation $t<\Gamma_N$, then

$$
v_p(R_N)=-W+t.
$$

When $W-t>0$, reduction of the endpoint ratio to coprime numerator and
denominator consequently gives $v_p(\beta_N)=W-t$.  No unproved statement
about the endpoint gcd is used here; this is the elementary uniqueness of
the $p$-part of a reduced rational denominator.

## 2. Complete classification below $239^3$

For positive odd $N<p^3$, every earlier index has $v_p(r)\le2$, so
$w(r)\le N$.  Also $a\le2$, and $a,d>0$ cannot occur together because
$N\equiv-1\pmod p$ makes $D_N\equiv-1\pmod p$.  This leaves exactly the
four cases used in the source.

* If $d>0$, then $a=0$ and $W_*=N+d>N$, so the final term is uniquely
  dominant.
* If $a=1$, then $W_*=N-1$.  A tying or larger positive-valuation earlier
  term would force $r=N-2$ with $p\mid r$, but
  $r\equiv-3\pmod p$; hence the final term is again unique.
* If $a=2$, write $N=p^2u-1$.  Parity and the range give the 119 even
  values $2\le u\le238$.  The only tie is the unit $r=N-2$, and the two
  leading terms sum, up to $s_{N-2}$, to $u-1/3$.  This vanishes only at
  $u=80$.
* If $a=d=0$, then $W_*=N$.  A tie requires
  $v_p(r)=N-r=2$, hence $N=p^2u+2$ with one of the 119 odd values
  $1\le u\le237$.  Up to $s_{N-2}$ the residue is $1/u-3/5$, which
  vanishes only at $u=161$.

It follows symbolically, without extrapolation, that the only two leading
zeros in this complete range are

$$
N_B=p^2\cdot80-1=4{,}569{,}679,
\qquad
N_A=p^2\cdot161+2=9{,}196{,}483.
$$

As a separate check, I exhaustively enumerated all
$(p^3-1)/2=6{,}825{,}959$ positive odd indices with an independently
written top-candidate calculation.  It found 238 ties, split as 119
unit-plus-final and 119 exact-$v_p=2$-plus-final ties, with maximum leading
multiplicity two and precisely the two residue zeros above.  It also found
the roots of $D_N$ modulo $239$ to be $15$ and $223$, with nonzero
derivatives $31$ and $208$, confirming the simple-root assertions.  This
enumeration corroborates the proof but is not a substitute for it.

## 3. The next-digit certificates

An independent modular implementation retained exactly those terms whose
gap from $W$ is less than two and reproduced the following data modulo
$p^2=57{,}121$:

| index | $W$ | $\Sigma_N\bmod p^2$ | $4\Sigma_N\bmod p^2$ | $\Gamma_N$ | $v_p(\beta_N)$ |
|---|---:|---:|---:|---:|---:|
| $N_B=4{,}569{,}679$ | $N_B-2$ | $19{,}120=80p$ | $19{,}359=81p$ | $4{,}550{,}477$ | $N_B-3=4{,}569{,}676$ |
| $N_A=9{,}196{,}483$ | $N_A$ | $9{,}082=38p$ | $36{,}328=152p$ | $9{,}157{,}843$ | $N_A-1=9{,}196{,}482$ |
| $N_C=923{,}374{,}845{,}407$ | $N_C$ | $2{,}868=12p$ | $11{,}472=48p$ | $919{,}495{,}119{,}166$ | $N_C-1=923{,}374{,}845{,}406$ |

For $N_B$, the next candidate gaps after the two tying terms are
$2,235,57{,}116$; for $N_A$ they are $4,479$.  The exact factorial
valuations are $19{,}200$ and $38{,}640$, producing the displayed regular
gaps.  Since every singular residue has exact valuation one and
$1<\Gamma_N$, the endpoint conclusions follow from the exact separation
lemma, not from numerical approximation.

For the far example, take $e=4$ and $u=283$.  Dividing the two-term leading
residue by $s_{N-e}$ gives

$$
\frac1u+(-1)^{e/2}\frac{e+1}{e^2+e-1},
$$

so cancellation is equivalent to

$$
u\equiv(-1)^{e/2+1}\frac{e^2+e-1}{e+1}\pmod p
$$

when the displayed units exist.  For $e=4$, this is
$u\equiv-19/5\equiv44\pmod{239}$, and $283\equiv44$.  At
$N_C=p^4\cdot283+4$, the exact candidate gaps for valuations
$e=0,1,2,3,4,5$ are

$$
2,\ 481,\ 114{,}244,\ 27{,}303{,}839,\ 0,
\ 143{,}563{,}580{,}203.
$$

There is no $e\ge6$ candidate because $p^6>N_C$.  Thus only the final term
and $r=N_C-4$ are dominant.  The independently recomputed exact values

$$
D_{N_C}=852{,}621{,}105{,}131{,}324{,}523{,}841{,}055,
\qquad v_p((N_C+1)!)=3{,}879{,}726{,}241
$$

give the third row of the table.  The source correctly restricts the
general congruence to a tie calculation: it does not claim that its two
terms are automatically dominant for every admissible $e$.

## 4. Recurrence and the adjacent-pair theorem

With

$$
S_N=\sum_{\substack{1\le r<N\\r\ \mathrm{odd}}}
       \frac{s_rp^{N-r}}r,
\qquad
F_N=S_N+s_N\frac{N+1}{D_N},
$$

one has $h_N=p^{-N}F_N$ and

$$
S_{N+2}=p^2S_N+s_N\frac{p^2}{N}.
$$

Substitution of
$1/N-(N+1)/D_N=-1/(ND_N)$ gives exactly

$$
F_{N+2}=p^2F_N-s_NH_N,
$$

where

$$
H_N=\frac{p^2D_{N+2}+N(N+3)D_N}{ND_ND_{N+2}}.
$$

The numerator expands to the positive integer

$$
P_N=N^4+4N^3+(p^2+2)N^2+(5p^2-3)N+5p^2.
$$

For $B_N=\lfloor\log_pP_N\rfloor$,
$v_p(H_N)\le v_p(P_N)\le B_N$.  If both $F$ values are nonzero and both
$v_p(F_N)+2$ and $v_p(F_{N+2})$ exceeded $B_N$, the recurrence would force
$v_p(H_N)>B_N$.  If one $F$ value is zero, $H_N\ne0$ and the recurrence
makes the other displayed term have valuation exactly $v_p(H_N)$.  Thus in
all cases

$$
\min\{v_p(F_N)+2,v_p(F_{N+2})\}\le B_N.
$$

After scaling by $p^j$, the regular part of the endpoint ratio has valuation
at least

$$
G_j=\min\{j-L_j,j+a_j-d_j,j-f_j,j-f_j-d_j+b_j\}.
$$

Legendre's formula gives $f_j\le(j+1)/(p-1)$, whereas
$a_j,d_j,L_j=O(\log j)$.  Hence both $G_N$ and $G_{N+2}$ eventually exceed
$B_N$.  For the member $j\in\{N,N+2\}$ selected by the recurrence, the
singular term is then strictly dominant and

$$
v_p(R_j)=-j+v_p(F_j),
\qquad
v_p(\beta_j)=j-v_p(F_j)\ge j-B_N.
$$

This validates every normalization step in the adjacent-pair proposition,
including domination of the factorial and $5$-adic regular terms.  It also
pinpoints the unresolved issue: the recurrence allows an isolated $F_N$ to
have arbitrarily high valuation while controlling its neighbors.  Nothing
in this branch rules out such isolated congruences uniformly.

## 5. Artifact and computation validation

I performed the following checks against the frozen hashes above.

* The archived script parses as Python, and its full default run completed.
  It regenerated all $8{,}381$ bytes of the archived JSON byte-for-byte;
  both files have SHA-256
  `e9045ea99af4ab9932851bb8b17e1f108d580bc152f4d8298749a979ae1eac96`.
* The JSON parses strictly with arbitrary-precision integer values and has
  no floating-point tokens.  In particular, the 24-digit value of
  $D_{N_C}$ is preserved exactly.
* A separate exact-`Fraction` implementation checked the recurrence and the
  expanded numerator at 42 odd indices, including 20 independently chosen
  indices beyond the archived script's range.  These finite checks are
  stress evidence only; the symbolic derivation above is the proof.
* The source, script, and result are strict UTF-8, LF-only files with no
  forbidden C0 control bytes or replacement characters.  The source has
  48 ordered display pairs, 176 ordered inline pairs, three matched
  `aligned` environments, and the complete sequential tag list 1 through
  42.  A Pandoc render check exits successfully.

The accepted logical endpoint is therefore exactly the one stated by the
source: full finite-precision control at any specified index, a complete
classification below $239^3$, three rigorous exceptional next digits, and
an unconditional adjacent-pair theorem.  The all-odd pointwise bound
$v_{239}(\beta_N)\ge N-O(\log N)$ remains open.
