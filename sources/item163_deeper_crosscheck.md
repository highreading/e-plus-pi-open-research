> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 163 deeper-digit package: independent cross-audit

Date: 2026-08-29

## Verdict

No mathematical, normalization, precision, census, replay, hash, or
formatting defect was found in the staged item-163 deeper-digit package.
The exact two-minor gate and its all-depth generalization are correct.  The
784-row experiment and all displayed layer counts reproduce independently.

One non-mathematical wording clarification is advisable.  Only (4.1) is a
differential Bockstein identity.  The higher recurrence (4.4)--(4.6) is the
generic base-$p$ convolution-and-carry expansion of a determinant, supplied with new
coordinate digits by the Hasse recurrence.  Calling the whole tower an
"iterated determinant-Bockstein" may suggest the formal iteration that
Section 5 correctly says is unavailable.  "Determinant digit/carry tower
seeded by the first Bockstein" would be more precise.  This does not change
any formula, certificate, or conclusion.

## 1. Independent normalization and all-depth gate

Write



$$
D_m^\sharp=p^e d,\qquad G_m=p^\delta g,\qquad
 D=1+\delta,
$$



where $d,g\in\mathbb Z_p^\times$, and put



$$
\mathscr A=q_pA_m,\qquad \mathscr B=8B_m.
$$



The frozen primitive coordinates give directly



$$
U_m={d\over g}{\mathscr A\over p^\delta},\qquad
 V_m={d\over8g}p^{e-\delta}\mathscr B.
$$



The archived forced-Cartier theorem gives
$p^D\mid\mathscr A,\mathscr B$.  Therefore, if



$$
\mathscr A/p^D=\sum_{j\ge0}a_jp^j,\qquad
 \mathscr B/p^D=\sum_{j\ge0}b_jp^j,
$$



then exactly



$$
v_p(U_m)=1+v_p(\mathscr A/p^D),\qquad
 v_p(V_m)=e+1+v_p(\mathscr B/p^D).
$$



Consequently, for every $r\ge2$,



$$
p^r\mid c_m
 \Longleftrightarrow
 a_0=\cdots=a_{r-2}=0
 \quad\hbox{and}\quad
 b_0=\cdots=b_{r-e-2}=0,
$$



with the second string empty for $r\le e+1$.  Setting $e=1$
reproduces all four gates through $p^5$, including the entry of $b_0$
at the $p^3$ layer.  No Cartier scalar or period coordinate is assumed
nonzero.

## 2. Precision and recurrence audit

For $F=A^{6m}/B^{K_s}$, coefficient comparison in



$$
(AB)F'=(6mA'B-K_sAB')F
$$



shows that the step producing $C_{n+1}$ loses exactly
$v_p(n+1)$ digits: the constant coefficient of $AB$ is a unit for
every odd forced prime.  Starting $C_0$ at precision



$$
M+v_p((K_s-1)!)
$$



leaves the last requested coefficient at exactly precision $M$.  The
implementation tracks this decreasing precision coefficient by coefficient
and checks every division by a power of $p$ for exactness.

For the $e=1$ rows, $4m+1<p^2$, hence every endpoint index has
valuation at most one and the only Hasse bands are $h=0,1$.  Coordinates
modulo $p^7$ suffice uniformly: in the worst branch $\delta=1$,
division of $\mathscr A$ by the normalization factor $p^\delta$ still
leaves six digits, while the $p^5$ gate itself needs only four normalized
$A$-digits and three normalized $B$-digits.

As an independent recurrence check, the fast coefficients were compared
modulo $p^7$ with the archived direct truncated-series evaluator for both
$s=0,1$ at



$$
(m,p)=(4,7),(9,13),(36,19),(89,19),(100,23),(100,167).
$$



All $(L_s,pR_s,E_s)$ triples agreed.  These rows cover rank one,
rank zero, new rank-two support, both normalization branches,
representative $p^3$ survivors, and the upper census boundary.  A separate
6,400-case randomized integer test of the carry recurrence, including
negative carries, also had zero failures.

## 3. Census and deterministic replay

Reconstructing the support independently from the archived definitions,
rather than reading the item-163 output rows, gives



$$
738=453+285
$$



rank-one $e=1$ rows split by $\delta=0,1$, plus 46 new rank-two-zero
rows, all with $\delta=0$.  There are 784 unique pairs and no duplicates.
Recomputing $v_p(c_m)=\min(v_p(U_m),v_p(V_m))$ from the complete frozen
integers gives



$$
\begin{array}{c|rrrrr}
\text{source}&p^1&p^2&p^3&p^4&p^5\\ \hline
\text{rank one, }\delta=0&453&35&4&0&0\\
\text{rank one, }\delta=1&285&15&1&0&0\\
\text{rank-two zero, }\delta=0&46&8&0&0&0\\ \hline
\text{all}&784&58&5&0&0.
\end{array}
$$



The five valuations at least three are exactly



$$
(36,19),(67,17),(74,19),(89,19),(100,23),
$$



and each valuation is exactly three.  A fresh canonical execution of the
certificate completed with zero assertion failures and produced 443,700
bytes byte-for-byte identical to both staged JSON files.

The support-capacity arithmetic was also recomputed from the exact formulas



$$
r_1={-4\log2+6\log3-3\over6},\qquad
 C_2=6-{\pi\over\sqrt3}-3\log3.
$$



It gives



$$
r_1+C_2/6=0.284908129921721664320454827882119\ldots,
$$



so four layers give
$1.13963251968688665728181931152847\ldots<T$, with gap
$0.0165146322773579550489109123284\ldots$.  Five layers are only the
first count not excluded by this optimistic support ceiling, exactly as the
note states.

## 4. Formatting and provenance

The Markdown decodes as strict UTF-8.  It has no decoded control or format
characters, NULs, replacement characters, or malformed math delimiters.
The 93 inline and 41 display math delimiters are paired, and every checked
math region has balanced braces.  Both JSON files parse and are
byte-identical.

Audited SHA-256 values:

```text
f2e7f97f54f101c6809a2bac882bd9cf3e5c9b637f9a51a6ec59c2f9fa3c57bc  item163_deeper_digits.md
e8e22e997d4b998d2e38454a5f9bef43f3a4d4995ec0bace8e211f0a7b1dfde5  item163_deeper_digits_certificate.py
c3234900f80abb0ff2ee4c96e82d8c19fd5734b58135d16c5090e397dcebc9d1  item163_deeper_digits_certificate.json
c3234900f80abb0ff2ee4c96e82d8c19fd5734b58135d16c5090e397dcebc9d1  item163_deeper_digits_certificate_replay.json
32c711487a5989753e8f47095f6fd337d318d3b7488085809d53711cd00490a6  item163_deeper_digits_hashes.sha256
```

The four input hashes embedded in the JSON also match their current
archived files exactly.  The final classification remains: exact gate and
evaluator proved; finite counts experimental; positive-mass simultaneous
digit vanishing open; no consequence here decides $e+\pi$.
