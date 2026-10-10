> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the spectral amplitude theorem

Date: 2026-09-13. Reviewed raw_spectral_amplitude_factorial_theorem.md.
The exact formula, explicit bounds, and asymptotic statements pass.

The principal determinant uses precisely the parity indices below l,
so every denominator eigenvalue is separated from xi_l. The determinant
recurrence and eigenvector recurrence give the stated ratio without
truncating the eigenvector. The odd amplitude is one half of the phi_1
coefficient; this factor is preserved throughout. For l>=2 every
denominator gap is positive, establishing the amplitude's sign in the
chosen positive central-coordinate phase. The cases l0 and l1 follow
directly from that phase choice.

Min-max bounds on both the full operator and the finite compression
give gap errors at most1/4. Reversing the parity index gives exactly
Delta=2s(2l−2s+1), with minimum4l−2. The sum-of-reciprocals bound and
|log(1+u)| estimate yield3H_m/[23(l+1)] as stated. Combining it with
the eigenfunction bound gives the explicit two-sided relative bound.

I checked both finite products, including their empty odd l1 cases.
The product of t_k equals the displayed central-binomial expression;
the unperturbed gap product equals(2l)!(m!)²/[2^epsilon(l!)²]. The odd
factor cancels exactly to give G_l. Stirling gives the linear constant
1−log8. The same-parity ratio and both different adjacent-parity
constants also follow with their stated conventions.

Thus the actual spectral weights have a rigorous relative asymptotic.
The theorem does not bound the growing polynomial factors evaluated at
those nodes, nor any mixed interpolation determinant. No such inference
was used in this review.
