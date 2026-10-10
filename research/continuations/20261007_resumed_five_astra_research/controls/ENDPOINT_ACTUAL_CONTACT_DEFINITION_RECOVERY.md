> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Recovered actual finite contacts for the seeded endpoint task

A3 turn1's source packet lacked the old explicit contact entries. They are
recoverable, so that missing input is not a reason to stop the contact target.
The following exact definitions are retained from O=A3 turn8 (5 October)
and P=A3 turn1/turn11 (6 October); their original excerpts accompany the
next packet. This recovery does not introduce a new producer or normalization.

Set c_k=[z^k]e^z q(z)^n, q=1-z+z^2/2, and a=c_(n-2), b=c_(n-1),
c=c_n, d=c_(n+1), e*=c_(n+2). The actual finite row-factorial matrix is

  T = [[c,b,a],[d,c,b],[e*,d,c]],
  C = diag(n!,(n+1)!,(n+2)!) T.

The endpoint rows are ell0=(-1,n,-n(n+1)), ell3=(0,0,1), and
Rj=ellj adj(T). Its actual primitive integer contact row rj is obtained by
the least denominator of the three rational coordinates of Rj followed by
the gcd of those three integer coordinates, with a recorded sign convention.
This contact coordinate content is distinct from the later whole-column
eight-entry clearer and the later all-prime row contents.

Put m=n+1,N=n+2, v'=(2N,N,m), w'=(0,N,2n+3), e2=(0,0,1).
Actual moment-state contact coordinates are

  cj=(rj v', rj w', rj e2).

The supplied retained relation is cj dot(P,Q,F)=0, with
P=nX+Y, Q=nZ+2X-Y, F=2m(Y-2X-(n-1)Z). The paid reference is
Rhatj=cj dot(L tau_n,L tau_(n+1),0).
These cj need not have coordinate content1 over every prime; the retained
large-prime content payment must be kept. Do not substitute arbitrary
syzygy rows for these actual rows or omit the exterior+1.

The complete finite force formula is also included in the original excerpt,
with its actual maximum index2n+2. Full reconstruction and the least eight-entry
clearer remain exactly those in the current A3 turn1 report.

New parent certificate: the degree<=6, denominator n(n+1)(n+2) gauge class
has exact ranks42 and43 and a rational left-null inconsistency witness. Twenty-one
small auxiliary seeded recurrence checks pass. This excludes only that specified
class and does not settle unrestricted rational gauges or original gcd growth.
