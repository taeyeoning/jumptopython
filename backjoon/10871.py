N, X = input().split()
N = int(N)
X = int(X)

A = list(map(int, input().split()))

for i in range(len(A)) :
    if A[i] < X :
        print(A[i], end = " ")