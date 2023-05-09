T = int(input())

for i in range(T):
  
  N, K = input().split()
  N = int(N)
  K = int(K)
  
  refri_gratis = int(N % K) + int(N / K)
  
  print(refri_gratis)