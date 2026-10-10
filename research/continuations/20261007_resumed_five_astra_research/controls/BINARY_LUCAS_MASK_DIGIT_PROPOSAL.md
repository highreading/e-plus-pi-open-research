> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Parent proposal: complete mod4 mask decision by a two-mask addition

Status: coordinator derivation awaiting independent review. The whole source
mod4 is independently proved in A4turn8. Finite receipts alone do not establish
the identities below for all original indices.

Keep b=9^(18+32u), n=4002b, h=n/2. Thus b=17mod64, n=2mod64. The mod4 force
is (2,1,3,1,0,...), and lambda and inverse symbol both equal (1,2,0,2,2).
At L2 the finite Schur completion has m=d=4. All entries of K,G,D_f use
binomial lower indices<=7, or the force's lower indices<=3. Binomial residues
at such indices are periodic modulo16 in their upper argument, by Vandermonde
and v2 binom(16,a)>=2 for1<=a<=7. Hence the finite Schur data are fixed by
n=2mod16,b=1mod16. The parent finite calculation gives

 S=S^-1=[[1,0,0,2],[0,1,0,0],[0,0,1,2],[0,0,0,1]],
 zeta=(2,1,3,2)^T, eta=U_n K zeta=0 modulo4.

The claim that this residue argument proves eta=0 on EVERY original index
requires review. It retains the actual return rather than omitting it.

Insert the four force residues and eta=0 into the accepted complete head
profile (6.2). At an odd-weight row W_j=binom(n+2,j), Lucas forces
j=0 or4 modulo64. The coefficient index in binom(j,a) never exceeds7.
The proposed simplifications are

 zf_j=0mod4                          when j=0mod64,
 zf_j=2 binom(2n+b+3-j,b+3-j) mod4    when j=4mod64.

For the first class, every positive inverse-symbol term carries2 and can be
reduced by Lucas: only a=0 survives. At s4,r4,i=q0 it contributes
2 binom(2n+b+3-j,b-1-j); this cancels the s0,i0 term
2 binom(2n+b-1-j,b-1-j), since their binomial parities agree (top low words20
and24, bottom low word16, no carry to the higher word). The i1 and i3 terms
vanish from their short binomial factors; the i2 term also has an even long
binomial. For the second class, positive-symbol terms can have a=0 or4 modulo2.
The only nonzero case is s4,r0,i=q0,a4, yielding the displayed expression.
All s0 terms vanish modulo4 from the short coefficients and low-word carry
counts; s1 and s3 have even small binomial factors. This branchwise argument
needs an independent coefficient check before promotion to theorem.

Put d=(b-1)/4 and H0=(h+1)/2. For j=4k odd weight means k is a binary submask
of H0. The second class has k odd, and the long binomial is odd exactly when

  ell=d+1-k has ell & h=0.

Thus the proposed exact criterion is

 a=0 iff exists k,ell with k+ell=d+1,
          k odd, ell>0, k & H0=k, ell & h=0.

The condition ell>0 gives k<=d and thus j<b. It is essential: the extraneous
ell0 solution would place the contact outside its finite endpoint.

A binary addition automaton with carry0/1 and a flag for ell>0 decides this
complete mask in O(log b) steps with at most4 states per position. It reads
the entire actual words of d+1,H0,h. This is not a free-suffix experiment and
does not enumerate or construct the original-size contact matrix. An accepting
path gives a concrete actual a=0 witness. A rejecting path proves a>=1 at the
finite original index only, CONDITIONAL on the head-profile simplification.
An infinite original theorem still requires analysis of the actual power word.
