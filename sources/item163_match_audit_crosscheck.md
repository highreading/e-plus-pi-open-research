> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 163 main matching package: independent cross-audit

Date: 2026-08-29 (Beijing time)

## Verdict

**FINAL PASS.** The exact primewise ledger, both divisibility theorems, the
subcritical-index no-go, the clearing-reservoir ceiling, all finite counts and
rates, replay determinism, and every manifest hash verify independently. The
two scope corrections and two packaging cleanups found in the initial audit
are present in the final package. None of the findings settles $e+\pi$.

## Package hashes audited

| file | SHA-256 |
|---|---|
| `sequential_matching_primewise_audit.py` | `d8f0523c9d4aaaef7e114b294785a988215e7cadeb50085b175841abdd489c35` |
| `sequential_matching_primewise_audit_m100_N6m.json` | `ab22c075132c72d9aa80206ef009220d93bc03907bf5b95faf6fb5db730daff9` |
| `sequential_matching_context_audit.py` | `b65ee0623c1529f9ef3e8abc27da233872ca2e8f90451a06d47adb532e32546c` |
| `sequential_matching_context_audit.json` | `3652db9285b7827c5fcf15b5828de96292bdf25055f954c7870daf6caef76de5` |
| `sequential_matching_mass_audit.md` | `81fc0b40b03f3953ecdcd4b350772223bb1eb587218c32f03f5caebbdda5d08f` |
| `item163_sequential_matching_audit_hashes.sha256` | `c1c4a0467919f0e2efa25935b24634f88d3d348e14a2d50db9a5cb05864fec1a` |

Every entry in the manifest matches. Fresh replays to separate temporary
outputs were byte-identical to the staged JSON files, with hashes
`ab22c075...` and `3652db92...` above.

## Algebra verified

Writing



$$
\kappa_p=\min\{v_p(U),v_p(V)\},\qquad
 \beta_p=v_p(V)-\kappa_p=v_p(b),\qquad t_p=v_p(q_N),
$$



gives



$$
d_p=v_p(\Delta)=\min\{\beta_p,t_p\}.
$$



If $0<t_p<\beta_p$, the normalized $b_0p_N$ term in $P^*$ is a
multiple of $p$, while $q_0a$ is a unit. If
$0<\beta_p<t_p$, the roles reverse, using
$\gcd(p_N,q_N)=1$. Thus $P^*$ is a unit whenever the two positive
valuations are unequal. On the equal diagonal,



$$
\gamma_p=v_p(g)=\min\{\beta_p,v_p(P^*)\}.
$$



Therefore the claimed exact ledger



$$
v_p(c\Delta g)=\kappa_p+d_p+\gamma_p
$$



is correct. Since $g\mid\Delta$, $\Delta\mid q_N$, and
$|V|=cb$,



$$
\Delta g\mid q_N^2,
 \qquad
 c\Delta g\mid |V|q_N.
$$



The recurrence bound $q_N<4^{N-1}N!\le(4N)^N$ for $N\ge2$ then gives



$$
\frac{\log(\Delta g)}{6m}
 \le\frac{N\log(4N)}{3m},
$$



so $N_m=o(m/\log m)$ has zero matching rate.

## Clearing-reservoir theorem verified

Let $K^{(0)}=K/\gcd(K,G)$ and
$D=K^{(0)}/\gcd(K^{(0)},c)$. Primewise, the exact relation
$V=K\widehat B/G\in\mathbb Z$ gives



$$
K^{(0)}\mid V,
 \qquad D\mid b.
$$



If $k=v_p(K^{(0)})$, $\kappa=v_p(c)$,
$\beta=v_p(b)$, and $t=v_p(q_N)$, then
$k\le\kappa+\beta$ and



$$
\min(k,\kappa+t)
 \le\kappa+\min(\beta,t).
$$



This proves $\gcd(K^{(0)},cq_N)\mid c\Delta$. In fact the same
case split proves the sharper exact equality



$$
\gcd(K^{(0)},cq_N)=\gcd(K^{(0)},c\Delta).
$$



For the scoped source accounting, put
$r=\max\{k-\kappa,0\}$. At most $\min(k,\kappa)$ reservoir digits
occur in $c$; at most $r$ residual digits can be forced into each of
$\Delta$ and $g$. Hence



$$
\min(k,\kappa)+2r\le2k.
$$



Because $K^{(0)}\le K$ and
$\log K/(6m)\to1/2$, the doubled reservoir ceiling is one. Adding the
rank-one rate, even with overlap deliberately overcounted, gives



$$
1+0.13651416829481281845\ldots
 =1.13651416829481281845\ldots
 <1.15614715196424461233\ldots,
$$



with gap $0.01963298366943179388\ldots$. This is a valid no-go only for
certificates whose booked sources are the rank-one radical and the
$K^{(0)}$-traceable reservoir; it is not an upper bound for actual
$c\Delta g$. The report states this scope correctly.

The lower estimate



$$
\liminf\frac{\log K^{(0)}}{6m}
 \ge\frac{3-(-4\log2+\pi/\sqrt3+3\log3)}6
 =0.1104920820002057\ldots
$$



also follows from $K^{(0)}\ge K/G$ and the frozen rates.

## Independent finite replay

An implementation independent of the package scripts reproduced:

- 15,150 candidates, 10,190 with $\Delta>1$, and 234 with $g>1$;
- 18 stored content maximizers with $g>1$;
- largest $g=1133$ at $(m,N,\Delta)=(91,455,12463)$;
- canonical transcript SHA-256
  `9ef61a6d4ebea6652466edd7208ddc43748acbf84a7afb3d4aa6007cbb013f35`;
- selected-index counts
  $41:19,312:13,138:12,37:10,121:8,4:7,234:6,59:5$;
- all five unrestricted-window block means, including the last-block rates
  $0.1845733550,0.0320234811,0.2165968361$;
- last-block reservoir means
  $0.4626258611,0.3398082625,0.1389485879$;
- complete support of every finite $c_m$ on primes $p\le6m$;
- the recovery divisibility and equal-valuation law on every candidate, not
  only the two stored distinguished candidates.

Independent reads of the pinned saddle scans reproduce both displayed rows
of means, their maxima, the 13/100 and 5/20 full-versus-saddle counts, and
the primitive-$b$ missing-prime lists and cofactor rates.

## Corrections verified as resolved

The final report now scopes the positive-rate statement to
$K^{(0)}\mid cb=|V|$, explicitly says that no positive asymptotic lower
bound is known for $D\mid b$, separates first-level singular-root abundance
from deeper all-lift behavior, and uses one-line PowerShell-compatible replay
commands. The two temporary `root_replay_*.json` copies were removed; the
directory now contains exactly the five manifested artifacts plus the
manifest itself.

## Formatting

The report has 96 balanced inline delimiters, 36 balanced display delimiters,
balanced code fences, sequential equation tags, valid UTF-8, and no forbidden
control bytes. The scripts, JSON files, and manifest also contain no forbidden
control bytes.
