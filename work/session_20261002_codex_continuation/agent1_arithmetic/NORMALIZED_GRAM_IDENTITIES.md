> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact normalized b=3 Gram identities

New author derivation for local and global-content research, 2026-10-02. No independent review is asserted. All identities refer to the same b=3,m_w=1 factorial B-only Gram center with its endpoint correction.

Put q0(t)=1-t+t²/2, a_s=[t^s]q0(t)^n, F=(n!)² and d=(n+1)(n+2). Define

H_n(x)=n! [t^n]e^(xt)q0(t)^n,
h=H_n(1), u=H'_n(1), v=H''_n(1).

(The symbol h here is a scalar jet; the historical metric determinant should be denoted h_met to avoid collision.) Let

a=h+(n−1)u/2+v/2,
b=((n²−n+2)h+(3n−1)u)/2+v.

Then M=2^n N, exactly, with

N=[[h,u,v], [a,(n+1)h,(n+1)u], [b,(n+2)a,d h]].

Proof: if f_k=[t^k]e^t q0(t)^n, logarithmic differentiation gives
(k+1)f_(k+1)=(k+1−n)f_k+(n−(k+1)/2)f_(k−1)+f_(k−2)/2.
The k=n and k=n+1 cases give (n+1)! f_(n+1)=a and (n+2)! f_(n+2)=b. Negative-shift entries are the derivatives u,v. This establishes every entry without inverting n+1 or n+2.

The exact reconstruction matrix is

K=[[-1,n,−n(n+1)], [1,−n−1,n(n+3)], [0,1,−2n−1], [0,0,1]].

Put Omega=diag(1,(n+2)²,d²,(dn)²) and H=K^T Omega K.

Define the exponential vector with no d prefactors by

A_i=sum_(s=0)^min(2n,n+i) a_s (n+i)_s Dcal_(2n+i−s), i=0,1,2,
Dcal_0=1, Dcal_k=k Dcal_(k−1)+1.

Then Ecal=2^n diag(d,n+2,1) A. This is a rational identity; A belongs to Z[1/2]^3 and is integral at every odd prime.

Put D0=diag(1,n+1,d), J=(P_n,P_n/2+P_(n+1)/4,P_(n+2)/8)^T, Y=adj(N)D0J and

D=Y^T H Y,
V=Y^T H adj(N)A+det(N)(K Y)_0.

The canonical contractions satisfy

Dg=2^(4n)D,
S=Acal+d Delta x_0=d 2^(5n)V.

In particular the complete center is exactly

c=2^n V/(F D)+beta,
beta=calL((K_z−Dg)/(t−1))/Dg.

This cancels d over Q before reducing at an odd prime. It retains the complete endpoint correction through the second term in V. The final rational denominator still depends on cancellation against beta; D or V alone is not q.

A useful two-coordinate endpoint representation removes the n+2 denominator:

D0J=[j0,(n+1)j1,(n+1)((2n+3)j1−(n+2)j0/2)]^T,
j0=P_n, j1=P_n/2+P_(n+1)/4.

It follows by substituting (n+2)P_(n+2)=2(2n+3)P_(n+1)+4(n+1)P_n. It is exact over Q even when n+2 is a local nonunit.
