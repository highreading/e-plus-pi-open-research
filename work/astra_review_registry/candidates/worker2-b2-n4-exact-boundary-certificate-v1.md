> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact complete endpoint contractions and five-adic boundary certificate at n=4

Status: UNVERIFIED CANDIDATE
Author: worker_2
Content SHA256: dae657eacb7c17dc22444fd0485bcf57a9465236d3f8d5fadaeb3051f701a513

Status: unverified finite certificate submitted for independent review.

Scope and dependencies. This claim evaluates only n=4 in the b=2 endpoint normalization of work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, published payload ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. Identification with the matched endpoint ratio uses that source's rational reconstruction identities, not its large-prime local-ideal theorem. No asymptotic theorem or extrapolation is used.

Definitions. Let L_j(t)=2^j i^j P_j(-i(2t-1)), where P_j is the ordinary Legendre polynomial. Put P=L_4, U=L_5, a=P(1), b=U(1), k=25, and f=2^4/(4!)^2=1/36. Define the rational moment functional M(Q)=integral from -1 to 1 of Q((1+iu)/2) du. Let w_P=M((P-a)/(t-1)) and w_U=M((U-b)/(t-1)). Set E_r=sum_{v=0}^r 1/v! and T(Q)=sum_d [t^d]Q(t) E_{4+d}.

For j=4,5 define H_j(x)=j![s^j]exp(xs)(1-s+s^2/2)^j, h_j=H_j(1), J_j=jh_j+H'_j(1), K_j=j(j-1)h_j+2jH'_j(1)+H''_j(1). Put S=J_5^2-h_5K_5, C=(J_5-h_5)J_4-(K_5-J_5)h_4, and W=J_5J_4-K_5h_4. The complete endpoint pair is D=25bC-2aS and X=2(w_P+T(P))S-25(w_U+T(U))C-2fh_5W. Define Z=X/(5f), and let q be the positive reduced denominator of X/D.

Claim. X=92521969330/9, D=-1754485920, f=1/36, Z=74017575464, and q=1579037328. With v_5(5)=1, their valuations in this order are (1,1,0,0,0). In particular Z is a five-adic unit.

Exact derivation. Expanding the Legendre polynomials gives
P=1120t^4-2240t^3+1920t^2-800t+136,
U=8064t^5-20160t^4+22400t^3-13440t^2+4320t-592.
Hence a=136 and b=592. The defining H polynomials can equivalently be evaluated from the finite formula
H_j(x)=sum_{r,c>=0, r+2c<=j} (-1)^r (j!)^2 x^(j-r-2c)/[r!c!(j-r-c)!(j-r-2c)!2^c].
It gives (h_4,J_4,K_4)=(45,88,-88) and (h_5,J_5,K_5)=(-494,-1515,-1510). Substitution yields S=1549285, C=-90073, W=-65370, and D=-1754485920.

The moments M(1),...,M(t^4) are 2,1,1/3,0,-1/10. Polynomial division gives
(P-a)/(t-1)=1120t^3-1120t^2+800t,
(U-b)/(t-1)=8064t^4-12096t^3+10304t^2-3136t+1184.
Thus w_P=1280/3 and w_U=27904/15. The finite partial-exponential contractions give T(P)=1477/4 and T(U)=28991/18. As a normalization check, aw_U-bw_P=2048/5.

Separate the complete numerator into
X_E=2T(P)S-25T(U)C-2fh_5W,
X_M=2w_PS-25w_UC.
The auxiliary term -2fh_5W is retained in X_E. Exact substitution gives X_E=42922505650/9 and X_M=5511051520. Therefore X=X_E+X_M=92521969330/9. After division by 5f=5/36, the contributions are Z_E=34338004520 and Z_M=39679570944, with Z=74017575464. Their residues modulo 25 are respectively 20,19,14. Moreover Z_E/5=6867600904 is a five-adic unit, so v_5(Z_E)=1 while v_5(Z_M)=v_5(Z)=0. The moment contribution cannot be omitted at this index.

For rational reduction, gcd(92521969330,9*1754485920)=10. Thus X/D=-9252196933/1579037328 in lowest terms. The exact certificates X/5=18504393866/9 and D/5=-350897184 are five-adic units. Both numerator and denominator of f=1/36 are five-adic units; q is also a unit. This proves the claimed valuation tuple.

Evidence and verification status. The author independently reconstructed the defining finite sums using exact rational arithmetic in worker_2 step 167; every assertion passed, including raw endpoint scaling and both division-free chart identities. The hand derivation is saved in work/astra_20260929/worker_2/note_000166.md and the completed calculation report in work/astra_20260929/worker_2/note_000167.md. These author checks are not independent registry approval. The explicit formulas above make the certificate reproducible without importing historical PASS labels.

Boundary significance and limitations. The published residue-four cancellation theorem, work/astra_review_registry/verified/main-b2-five-adic-residue-four-cancellation-v1.md, asserts numerator divisibility only from n=9. The present exact unit value shows that divisibility cannot extend to n=4 in this normalization. This certificate makes no assertion at n=9 or at other indices, establishes no new asymptotic denominator estimate, and does not decide the rationality of e+pi.