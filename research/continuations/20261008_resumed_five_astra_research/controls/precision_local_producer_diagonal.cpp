// Parent-authored bounded arithmetic. No network, filesystem or external code.
// Entry generation by literal small Pascal transforms and PROVED diagonal
// Newton polynomials, independent of the initial multinomial implementation.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using U=uint64_t;
using V=std::vector<U>;
using Mat=std::vector<V>;
using Wide=__uint128_t;
using Signed=__int128_t;
static U Q;
static U mul(U a,U b){return U(Wide(a)*b%Q);}
static U sub(U a,U b){return a>=b?a-b:a+Q-b;}
static U powm(U a,U b,U mod){U s=1;while(b){if(b&1)s=U(Wide(s)*a%mod);a=U(Wide(a)*a%mod);b>>=1;}return s;}
static U power3(int n){U s=1;for(int i=0;i<n;i++){if(s>UINT64_MAX/3)throw std::runtime_error("power bound");s*=3;}return s;}
static U inverse(U a,U mod){Signed x=1,y=0;U r=a,s=mod;while(s){U q=r/s,t=r%s;r=s;s=t;Signed z=x-Signed(q)*y;x=y;y=z;}if(r!=1)throw std::runtime_error("nonunit inverse");x%=Signed(mod);if(x<0)x+=mod;return U(x);}
static V binomial_row(U a,int top){
  V v(top+1);v[0]=1;U unit=1;int depth=0;
  for(int s=1;s<=top;s++){
    if(U(s)>a){v[s]=0;continue;}
    U num=a-U(s)+1,den=s;
    while(num%3==0){num/=3;depth++;}
    while(den%3==0){den/=3;depth--;}
    if(depth<0)throw std::runtime_error("negative binomial depth");
    unit=mul(mul(unit,num%Q),inverse(den,Q));
    v[s]=depth>=33?0:mul(unit,power3(depth)%Q);
  }
  return v;
}
static V digit_solve(const Mat&a,const V&f,int M){
  int n=int(a.size());V x(n);U step=1;
  for(int r=0;r<M;r++){
    V rem(n),d(n);
    for(int i=0;i<n;i++){
      Wide sum=0;for(int j=std::max(0,i-(6*M-1));j<=std::min(n-1,i+6*M-1);j++)sum+=Wide(a[i][j])*x[j];
      U z=sub(f[i],U(sum%Q));if(z%step)throw std::runtime_error("unpaid digit division");rem[i]=(z/step)%3;
    }
    for(int i=0;i<n;i+=3){
      if(n-i>=3){U u=rem[i],v=rem[i+1],w=rem[i+2];d[i]=2*v%3;d[i+1]=(2*u+v+w)%3;d[i+2]=(v+2*w)%3;}
      else if(n-i==2){d[i]=2*rem[i+1]%3;d[i+1]=(2*rem[i]+2*rem[i+1])%3;}
      else d[i]=rem[i];
    }
    for(int i=0;i<n;i++)x[i]+=step*d[i];step*=3;
  }
  for(int i=0;i<n;i++){Wide sum=0;for(int j=0;j<n;j++)sum+=Wide(a[i][j])*x[j];if(sub(f[i],U(sum%Q)))throw std::runtime_error("final residual");}
  return x;
}
static void vector_json(const V&v){std::cout<<'[';for(size_t i=0;i<v.size();i++){if(i)std::cout<<',';std::cout<<v[i];}std::cout<<']';}
int main(int argc,char**argv){try{
  if(argc!=4)throw std::runtime_error("arguments M,n-residue,L required");
  int M=std::stoi(argv[1]),L=std::stoi(argv[3]);U nr=std::stoull(argv[2]);
  if(M<4||M>33||L<1||L>72||nr%3!=2)throw std::runtime_error("bounded input domain");
  Q=power3(M);int R=std::max(L,6*M)+13*(M-1)+4;R+=(int(nr%3)-R%3+3)%3;
  int lg=0;for(U z=3;z<=U(R);z*=3)lg++;int E=M+lg+1;U period=power3(E);
  if(nr>=period||R>622)throw std::runtime_error("residue/window guard");
  int H=6*M-1,rows=H+1,cols=2*H+1,endpoint=3*H;
  Mat choose(endpoint+1,V(endpoint+1));choose[0][0]=1;
  for(int n=1;n<=endpoint;n++){choose[n][0]=choose[n][n]=1;for(int k=1;k<n;k++)choose[n][k]=(choose[n-1][k-1]+choose[n-1][k])%Q;}
  V gamma(endpoint+1);gamma[0]=1;gamma[1]=0;
  for(int n=1;n<endpoint;n++)gamma[n+1]=(mul((4*U(n)+2)%Q,gamma[n])+mul(4,gamma[n-1]))%Q;
  Mat raw(rows,V(cols)),left(rows,V(cols)),hat(rows,V(cols));
  for(int a=0;a<rows;a++)for(int b=0;b<cols;b++)raw[a][b]=mul(choose[a+b][a],gamma[a+b]);
  for(int a=0;a<rows;a++)for(int b=0;b<cols;b++){
    Wide pos=0,neg=0;for(int r=0;r<=a;r++){Wide t=Wide(choose[a][r])*raw[r][b];if((a-r)&1)neg+=t;else pos+=t;}left[a][b]=sub(U(pos%Q),U(neg%Q));
  }
  for(int a=0;a<rows;a++)for(int b=0;b<cols;b++){
    Wide pos=0,neg=0;for(int s=0;s<=b;s++){Wide t=Wide(choose[b][s])*left[a][s];if((b-s)&1)neg+=t;else pos+=t;}hat[a][b]=sub(U(pos%Q),U(neg%Q));
  }
  Mat newton(2*H+1,V(rows));
  for(int delta=-H;delta<=H;delta++){
    V v(rows);for(int a=0;a<rows;a++){int b=a-delta;v[a]=(b<0?0:hat[a][b]);}
    for(int s=0;s<rows;s++){newton[delta+H][s]=v[0];for(int i=0;i<rows-s-1;i++)v[i]=sub(v[i+1],v[i]);}
  }
  Mat endchoose(R,V(rows));for(int i=0;i<R;i++)endchoose[i]=binomial_row((nr+period-U(R-i))%period,H);
  auto entry=[&](int row,int delta)->U{
    if(delta<-H||delta>H)return 0;Wide sum=0;for(int s=0;s<rows;s++)sum+=Wide(newton[delta+H][s])*endchoose[row][s];return U(sum%Q);
  };
  Mat a(R,V(R));V kh(R);
  for(int i=0;i<R;i++){for(int j=std::max(0,i-H);j<=std::min(R-1,i+H);j++)a[i][j]=entry(i,i-j);kh[i]=entry(i,i-R);}
  const int base[3][3]={{1,2,2},{2,0,0},{2,0,2}};
  for(int i=0;i<R;i++)for(int j=0;j<R;j++){
    if(a[i][j]!=a[j][i])throw std::runtime_error("literal symmetry");
    int expected=i/3==j/3?base[i%3][j%3]:0;
    if(a[i][j]%3!=U(expected))throw std::runtime_error("actual block type");
  }
  int top=std::max(L,3*M);V u(R),uh(R),ratios(R);U factor=1,exponent_period=power3(M-1);
  for(int r=1;r<=3*M;r++){
    int i=R-r;if(r>1)factor=mul(factor,(nr+period-U(r-1))%period%Q);
    ratios[i]=factor;U ar=(nr+period-U(r))%period;u[i]=mul(factor,powm(Q-2,ar%exponent_period,Q));
  }
  for(int b=R-3*M;b<R;b++){
    Wide pos=0,neg=0;for(int i=R-3*M;i<=b;i++){Wide t=Wide(endchoose[b][b-i])*u[i];if((b-i)&1)neg+=t;else pos+=t;}uh[b]=sub(U(pos%Q),U(neg%Q));
  }
  V vh=digit_solve(a,uh,M),hh=digit_solve(a,kh,M),vtop(top),htop(top);
  V nchoose=binomial_row(nr,H);
  for(int r=1;r<=top;r++){
    int i=R-r;Wide pv=0,nv=0,ph=0,nh=0;
    for(int b=i;b<R;b++){Wide tv=Wide(endchoose[b][b-i])*vh[b],th=Wide(endchoose[b][b-i])*hh[b];if((b-i)&1){nv+=tv;nh+=th;}else{pv+=tv;ph+=th;}}
    vtop[top-r]=sub(U(pv%Q),U(nv%Q));U known=nchoose[r];if((r-1)&1)known=known?Q-known:0;htop[top-r]=(known+sub(U(ph%Q),U(nh%Q)))%Q;
  }
  Wide ee=0,ss=0;for(int i=R-3*M;i<R;i++)ee+=Wide(uh[i])*vh[i];
  U eta=U(ee%Q);eta=eta?Q-eta:0;
  for(int r=1;r<=3*M;r++)ss+=Wide(u[R-r])*htop[top-r];
  U chi=(mul((3*(nr%Q))%Q,U(ss%Q))+mul(6,u[R-1]))%Q;
  if(eta%9!=3||chi%9!=3)throw std::runtime_error("reused scalar law");
  U target=Q/3,xi=U(Wide(chi/3)*inverse(eta/3,target)%target);
  U bc=(target-((nr%target+66)%target))%target;
  U inv_n1=inverse((nr+period-1)%period%target,target);
  V q(L),v70(L>1?L-1:0);int min_depth=M-1;std::vector<int> depths(L);
  for(int r=1;r<=L;r++){
    U force=U(Wide((3*(nr%target))%target)*(htop[top-r]%target)%target);
    if(r==1)force=(force+bc+6)%target;
    if(r==2)force=(force+U(Wide(2)*bc*inv_n1%target))%target;
    force=(force+U(Wide(xi)*(vtop[top-r]%target)%target))%target;
    U val=U(Wide(ratios[R-r]%target)*force%target);q[L-r]=val?target-val:0;
    U z=q[L-r];int d=M-1;if(z){d=0;while(z%3==0){z/=3;d++;}}depths[L-r]=d;min_depth=std::min(min_depth,d);
  }
  U endpoint_value=0,pow_neg2=1;
  for(int i=0;i<L;i++){endpoint_value=(endpoint_value+U(Wide(q[i])*pow_neg2%target))%target;pow_neg2=U(Wide(pow_neg2)*(target-2)%target);}
  for(int b=0;b<L-1;b++){U p=1;Wide sum=0;for(int r=b+1;r<L;r++){sum+=Wide(p)*q[r];p=U(Wide(p)*(target-2)%target);}v70[b]=U(sum%target);}
  std::cout<<"{\"status\":\"PASS\",\"M\":"<<M<<",\"target_precision\":"<<M-1<<",\"L\":"<<L<<",\"window\":"<<R<<",\"entry_polynomial_degree_bound\":"<<H<<",\"small_raw_moment_endpoint\":"<<endpoint<<",\"input_period_exponent\":"<<E<<",\"n_residue\":\""<<nr<<"\",\"Xi_mod_input\":"<<eta<<",\"chi_mod_input\":"<<chi<<",\"xi_mod_target\":"<<xi<<",\"minimum_top_q_depth_at_capped_precision\":"<<min_depth<<",\"top_polynomial_at_minus2\":"<<endpoint_value<<",\"q_top\":";
  vector_json(q);std::cout<<",\"V_coefficients\":";vector_json(v70);std::cout<<",\"q_depths_capped\":[";for(int i=0;i<L;i++){if(i)std::cout<<',';std::cout<<depths[i];}std::cout<<"]}\n";
  return 0;
}catch(const std::exception&e){std::cerr<<"BOUNDED_CHECK_FAILURE: "<<e.what()<<'\n';return 1;}}
