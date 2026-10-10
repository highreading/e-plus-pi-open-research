> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Route 1 literature update — 2026-08-31

## Scope

This note records a targeted primary-source check for work published after
the earlier archive triage.  It is a literature-status note, not a proof and
not a capacity booking.

## Directly relevant 2026 preprint

Runlong Yu, *Tail Criteria, No-Go Audits, and Apéry-Type Certificate
Obstructions for the Irrationality of $e+\pi$*, arXiv:2606.17303
(submitted 2026-06-15):

<https://arxiv.org/abs/2606.17303>

The paper explicitly states that the irrationality of $e+\pi$ remains
open.  Its proved results include:

1. exact equivalences between $e+\pi\in\mathbb Q$ and eventual factorial
   tail behavior, including a ceiling recurrence, a factorial-Cantor digit
   condition for $\pi$, and an eventual divisibility condition;
2. the mixed integer-kernel identity
   

$$
\int_0^1\left(P(x)e^x+\frac{4A(P)}{1+x^2}\right)\,dx
   =A(P)(e+\pi)-S_P(0)
$$


   for $P\in\mathbb Z[x]$; and
3. bounded no-go audits for several low-complexity Apéry-type mechanisms.

The paper expressly does **not** prove $e+\pi\notin\mathbb Q$.  Its tail
criteria require an eventual pattern to be disproved infinitely often, and
its computational audits are scoped rather than universal.

## Adjacent 2026 preprint

L. Lerner, *The Irrationality of $e$ and $\pi$*, arXiv:2607.19418
(submitted 2026-07-19):

<https://arxiv.org/abs/2607.19418>

This concerns separate proofs and integral representations for the
irrationality of $e$ and $\pi$.  Separate irrationality or transcendence
does not exclude rational cancellation in $e+\pi$, so it supplies no
Route-1 mass or closure theorem.

## Route-management consequence

Neither preprint supplies:

- weighted zero density for the fixed $j=1$ or $j=2$ cells;
- an actual positive-mass higher-Witt or matching mechanism;
- a global upper bound for fresh or multi-parent matching; or
- a de-overlapped exponent gain.

## Fixed-characteristic frameworks checked for the live zero-density target

Two standard-looking frameworks were also checked against the actual
horizontal quantifiers.

Eric Rowland and Reem Yassawi, *Automatic congruences for diagonals of
rational functions*, arXiv:1310.8635,
<https://arxiv.org/abs/1310.8635>, construct finite automata for diagonal or
algebraic coefficient sequences modulo a **fixed** prime power.  Alan
Adolphson and Steven Sperber, *Hasse invariants and mod $p$ solutions of
$A$-hypergeometric systems*, arXiv:1209.2448,
<https://arxiv.org/abs/1209.2448>, identify Hasse invariants with mod-$p$
hypergeometric solutions in fixed characteristic.  These are relevant
structural languages for the algebraic coefficient and incomplete-beta
periods, but neither abstract theorem controls the diagonal event in which
the characteristic itself is the moving row prime



$$
p=4h+6s+3
$$



or proves a Chebyshev-weighted $o(M)$ zero bound while $p$, $h$, and
$s$ vary together.  Importing fixed-$p$ automaticity or a Hasse-invariant
realization without a new horizontal bridge would therefore be an
applicability error, not a density theorem.

The factorial-tail and mixed-kernel criteria are conceptually transverse and
may inform a future Route 2.  Under the frozen execution rule they are not
imported into Route 1 merely to keep Route 1 open.



$$
\boxed{\text{new Route-1 rate}=0,\qquad
\text{new retained-capacity change}=0.}
$$



The authoritative Route-1 decision therefore remains unchanged pending new
mathematics in the live branches.
