"""Exact equilibrium phase algebra; no actual finite-center samples."""
import sympy as S
import json

c=S.symbols('c',positive=True)
s=S.sqrt(2); M=1+s; B=M*M+1; E=M*M+(c+1)**2
simp=lambda f:S.factor(S.cancel(f,extension=s),extension=s)
A2=M*M*c*(c+2)/E
zp=2/(2+c); zm=2*M/(2*M-c)
qp=s+zp; qm=s-zm
Tp=M*M*(2*s+c)/(2*s*M+c)
Tm=M*M*(2*s-c)/(2*s*M+c)
Pp=c*c+(s+3)*c+B
Pm=c*c+(1-s)*c+B

def Gprime(T,P):
    Croot=M*B*P/(c*(2*s*M+c))
    return -T*((c+1)/(c*(1-T*T))+1/(c*(M*M+T*T)))+Croot/((1-T*T)*(M*M+T*T))

Jp=(-1+(Tp-1)*Gprime(Tp,Pp))/(1-qp)
Jm=(-1+(Tm+1)*Gprime(Tm,Pm))/(1-qm)
g=lambda z:1+s/2*(z+1/z)
h=lambda z:s/2*(z+1/z)-1
plus_stationary=simp(s/2*(1-1/zp**2)/g(zp)+c*Jp)
minus_stationary=simp(s/2*(1-1/zm**2)/h(zm)-c*Jm)

kp=M*(2*s+c)/Pp; km=M*(2*s-c)/Pm
k1p=(c+1)*kp; k1m=(c+1)*km
aa=(qp-1)/(1-qm)
bb=(Tp*Tp-1)/(Tm*Tm-1)
cc=(M*M+Tp*Tp)/(M*M+Tm*Tm)
dd=((k1p+1)/(k1p-1))/((k1m+1)/(k1m-1))
ee=((1+kp)/(1-kp))/((1+km)/(1-km))
linear_factor=simp(aa**2*bb*dd)
constant_factor=simp((g(zp)/h(zm))**2*bb*dd/(cc*ee))
result={
 "scope":"exact auxiliary equilibrium saddle algebra only; center-rate theorem separate",
 "zeta_plus":str(zp),"zeta_minus":str(zm),
 "plus_stationary_residual":str(plus_stationary),
 "minus_stationary_residual":str(minus_stationary),
 "linear_log_factor":str(linear_factor),
 "linear_log_factor_minus_M_squared":str(simp(linear_factor-M*M)),
 "constant_log_factor":str(constant_factor),
 "constant_log_factor_minus_M_fourth":str(simp(constant_factor-M**4)),
 "radical_square_plus_residual":str(simp((Tp*Tp+A2)*E*(2*s*M+c)**2/M**2-B*Pp**2)),
 "radical_square_minus_residual":str(simp((Tm*Tm+A2)*E*(2*s*M+c)**2/M**2-B*Pm**2))
}
print(json.dumps(result,indent=2))
