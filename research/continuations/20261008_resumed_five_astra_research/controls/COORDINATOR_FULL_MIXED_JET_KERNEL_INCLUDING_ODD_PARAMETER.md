> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The full mixed-jet kernel, including the odd auxiliary parameter

Parent derivation, 9 October 2026. This is NEW and UNSENT when written;
DIFFERENT proof review is pending. The original EVEN-d joint kernel
and integer rising divisor independently PASS full A4turn21. The
new complete mixed comparison in A2turn13 and the parent quarter
window are being independently audited in A4turn22. None of those
audits is a final terminal coefficient upper.

Scoped current/prior/Desktop English MD/TEX searches for this all-
higher mixed-jet kernel and its odd-parameter derivative find no
earlier proved statement. The SINGLE first mixed jet S_p(r), the
original even-d joint kernel and all Newton product rules are REUSE.
No new external theorem is imported. This note specializes those
identities to the actual retained mixed Cauchy columns; it does not
replace the original d by a freely chosen research index.

## 1. Actual mixed bottom jets

Keep ORIGINAL d=9^(18+32u)-1 and all exact corrected columns, integer
divisions and physical ranges in full A2turn13/A4turn21. Choose a
set I of e ACTUAL rational Cauchy forcing-column indices, each<d,
and define the exact odd polynomial

    Q_I(i)=product_(b in I)(2(d+i+b)+1).

Here e=|I| is an AUXILIARY mixed-compound column count, not a changed
original index. For an actual weighted return r<d, put

    W_r(i)=eta_r^(d+i).

The mixed Cauchy identity leaves the INTEGER column Q_I(i)W_r(i).
For every admissible physical Newton order j, the full divisor
2^j j! is paid. Its binary normalized coefficient is

    Phi_(j,r)(I)=Delta^j(Q_I W_r)(0)/(2^j j!) mod2.

The exact finite product rule and the original shift independence
eta_s^(m) mod2=eta_s give

    Phi_(j,r)(I)
       =sum_(t=0)^min(e,j) binom(e,t)
                     binom(r+j-t,r) eta_(r+j-t).       (1)

Proof of the Q factor: write Q_I as an integer polynomial in2i.
Its degree-b coefficient has parity binom(e,b), because all e
constant factors are odd. In the normalized tth difference,
terms with b<t vanish and b>t retain an additional factor2.
The b=t term has Delta^t i^t/t!=1. Hence

    Delta^t Q_I(i)/(2^t t!)=binom(e,t) mod2,

independent of i and the actual pole choices. The original weighted
return identity is

    Delta^s W_r(i)/(2^s s!)
       =binom(r+s,r) eta_(r+s) mod2.

In the product rule the binomial coefficient exactly pays the ratio
j!/[t!(j-t)!], yielding(1). All INTEGER odd factors and divisions
are taken before reducing parity. The dependence on I disappears
only at this normalized parity precision.

For j=e+z, z>=0, changing t to e-t evaluates every higher mixed jet:

    Phi_(e+z,r)(I)=U_e(z,r),
    U_e(z,r)=sum_(t=0)^e binom(e,t)
                         binom(r+z+t,r) eta_(r+z+t).    (2)

The already evaluated first mixed scalar is U_e(0,r)=S_e(r).
Equation(2) gives its complete higher-jet array. Its use requires
e+z<=d+1, and with a shifted starting row i also i+e+z<=d+1.
Consequently all original physical source/return indices stay below
3d and the successor moment stays3d+1=3k-2. No factorial beyond
(6k-4)! or return column r>=d is introduced.

## 2. Joint generating law at BOTH parities of e

Let omega^2+omega+1=0 in F4, Tr(a)=a+a^2, and trace coefficientwise
with formal variables fixed. The exact original contact parity is

    eta_n=Tr(omega^(n+2)+(n+1)omega^n).

Put S=X+Y and

    B_e(Y)=((omega^2+omega Y)/(1+omega Y))^e,
    H_e(X,Y)=B_e(Y)/(1+omega S).

Using the classical finite binomial generating identity,

    sum_(z,r>=0) binom(t+z+r,r) X^z Y^r
       =(1-Y)^(-t)/(1-X-Y),

one obtains

    H_e=sum_(t=0)^e binom(e,t) omega^t
                    sum_(z,r>=0) binom(t+z+r,r)
                                    (omega X)^z(omega Y)^r.

Let E=X*d/dX+Y*d/dY. The factor n+1=z+r+t+1 in eta_n means

    F_e:=sum_(z,r>=0) U_e(z,r)X^zY^r
       =Tr((omega^2+1)H_e+E H_e+T_e),                (3)

where

    T_e=(e mod2) omega B_(e-1)(Y)
                             /((1+omega Y)(1+omega S)).

When e=0, T_e is zero and B_(-1) is not used. Unlike the original
even-d specialization, the t-derivative and the Y derivative of
B_e cannot be dropped when e is odd.

Indeed,

    Y B_e'(Y)=(e mod2) omega^2 Y B_(e-1)(Y)
                                              /(1+omega Y)^2.

Combining this term with T_e gives

    Y B_e'+(e mod2) omega B_(e-1)/(1+omega Y)
       =(e mod2) omega B_(e-1)/(1+omega Y)^2.

The remaining denominator derivative in E H_e is
B_e omega S/(1+omega S)^2. Since omega^2+1=omega and
omega+omega^2=1, the full evaluated kernel is therefore

    F_e(X,Y)=Tr[
       B_e(Y)(omega+S)/(1+omega S)^2
       +(e mod2) omega B_(e-1)(Y)
                    /((1+omega Y)^2(1+omega S))].      (4)

Every denominator has unit constant term. For EVEN e the second
term vanishes, and the first is exactly

    Tr[omega^2 B_e(Y)
                    (omega^2+omega S)/(1+omega S)^2],

the independently established original even-d kernel. For ODD e
the second term is indispensable. For example at e=1,z=r=0, the
direct value eta_0+eta_1 is1. The first term alone has trace0,
while the derivative term contributes1. This is a displayed
algebraic check, not a new computational scan or a global rank claim.

## 3. The concrete corrected mixed interface

In an exact mixed term, e=a is the number of retained R_C columns,
not automatically p, the number of R N_d A product columns. They
coincide only when v=0 factorial correction columns are selected.
This distinction remains necessary in all higher mixed compounds.

The top source normalized contact rows are U_d, with d the actual
original even parameter. After paying the mixed Cauchy polynomial
columns, the normalized bottom return jets are U_a, with a possibly
ODD mixed count. Thus full mixed parity couples two evaluated kernels
at DIFFERENT parameters, rather than applying the original even-d
source-unit theorem to both halves. Formula(4) supplies the missing
odd-count derivative exactly.

The integer mixed Cauchy factor, its odd row denominators, the
factorial-adjugate source weights, actual atom correction, both full
affine borders, Cramer scalars and actual final G are NOT replaced
by this binary array. Summing mixed terms at a tied valuation may
cancel. A rank of one auxiliary stack is not automatically the
complete determinant coefficient or their joint upper depth.

The next precise question is to evaluate the rank/leading paid
compound of the actual U_d/U_a coupling when the multiple-return
comparison window closes, retaining atom-in-source and atom-in-W
terms and BOTH terminal borders. In particular an argument that
uses B_a'=0 at odd a would be invalid. The full kernel(4) repairs
that shortcut before any such continuation is attempted.

No joint terminal upper, other odd-prime control, producer retirement
or decision about e+pi is asserted here. The note is an evaluated
all-higher mixed-jet identity and a new input to ongoing A2 research.
It awaits DIFFERENT full proof audit; no computation is indispensable
merely to mirror the finite product rule.
