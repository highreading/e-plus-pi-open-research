// Parent-owned isolated Pascal-row regression; no matrix solve.
#define main historical_producer_main
#include "precision_local_producer_diagonal_allocation_repaired.cpp"
#undef main
int main(){
  const int M=4,L=72,H=6*M-1,K=std::max(H,std::max(L,3*M));
  Q=power3(M);
  V nchoose=binomial_row(200,K), endchoose=binomial_row(199,K);
  if(nchoose.size()!=size_t(K+1)||endchoose.size()!=size_t(K+1))return 2;
  std::cout<<"{\"M\":"<<M<<",\"L\":"<<L<<",\"H\":"<<H<<",\"K\":"<<K
           <<",\"binom_200_24_mod81\":"<<nchoose.at(24)
           <<",\"last_nchoose\":"<<nchoose.at(72)
           <<",\"last_reconstruction_entry\":"<<endchoose.at(71)<<",\"nchoose\":";
  vector_json(nchoose);std::cout<<",\"endchoose\":";vector_json(endchoose);
  std::cout<<"}\n";return 0;
}
