> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit: cubic Smith reduction and Cartier infinity resonance

Date: 2026-08-28

## Cubic Smith reduction (staged item 157)

The algebraic reduction in `mixed_cubic_cube_smith_reduction.md` is
correct as stated.

- The coefficient definitions and the multiplication matrix agree.
- The twenty maximal minors have the twelve listed forms, with the stated
  signs in the certificate.
- The DVR argument, including the nonprimitive common-content case, proves
  (G_q\mid\Delta_3(q)) away from (2,3).
- The Smith chain gives
  (G_q\mid\Delta_3(q)=d_1d_2d_3\mid d_3^3).
- The exclusion of a compatible prime is explicitly conditional on the
  still-unproved assertion (d_3(q)\mid P_q).

The theorem/evidence boundary is clean: (d_3(q)\mid P_q), and hence
(G_q\mid P_q^3), is exact finite evidence for admissible (q\le1001),
not a uniform theorem.  The original JSON and replay are byte-identical.

Audited SHA-256 values:

```text
b44cc15d1a846d5298d61b9e53539116b31bbab0338dbc6e320fb0a875b0d0a0  mixed_cubic_cube_smith_reduction.md
4ebb2d8747afed65bdd9af720ff39aa5d01d4db5a15d6134a7ed8961e85a9149  mixed_cubic_cube_smith_certificate.py
0366edc49654f250c5d7b0933d8994b69659acc571699ea8256342c3eec02196  mixed_cubic_cube_smith_certificate_q1001.json
0366edc49654f250c5d7b0933d8994b69659acc571699ea8256342c3eec02196  mixed_cubic_cube_smith_certificate_q1001.replay.json
```

## Cartier/Hermite bounded-primitive proposal

The reduction to a Cartier-zero, hence exact, differential is valid, but
the proposed bound $\deg V\le1$ is not.  For



$$
D_A(V)=QuV'+\frac A3uQ'V-(q-1)Qu'V,
$$



one has the exact monomial formula



$$
D_A(z^d)=(d-q+1)z^d+\frac{5q-6}{3}
 (z^{d+1}+z^{d+2}+z^{d+3})+(1-d)z^{d+4}.
$$



Global Hermite reduction gives $\deg V\le2p$.  Therefore a nonzero
primitive with cubic output can have degree (1) or (p+1).  The second
case is a genuine infinity resonance, not a removable formal gauge.  The
certificate constructs exact witnesses at



$$
(p,q)=(11,5),(31,13),(97,13),
$$



including witnesses whose numerator ratio is the actual fixed-gap residue
ratio.  None has (B_0=B_1=0), so this is a counterexample only to the
bounded-primitive proof step, not to fresh-prime nonvanishing.

This is a genuinely distinct archived barrier from item 153: item 153
records the corrected moving-ray equivalence and the failure of a generic
three-term propagation certificate, whereas this package identifies a
global characteristic-(p) infinity mode in the Cartier/Hermite route.

The certificate replayed byte-for-byte.  Audited SHA-256 values:

```text
28ed1ebbca1e04b4b8fb82777e8635b86e3d9a130ecf3788eb97b9878c9b3c8c  mixed_cubic_cartier_infinity_resonance_barrier.md
687ede47178f8bfa232f932e56b8b486577052f685edbe176b40feafc0aabf21  mixed_cubic_cartier_infinity_resonance_certificate.py
5b6a142bb5f98cebefa81ec3ee3333ab5da6d73e98fc4c0b300bd5d4cad68d01  mixed_cubic_cartier_infinity_resonance_certificate.json
```

All audited files are free of unexpected control bytes.
