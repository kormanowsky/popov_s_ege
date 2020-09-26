N = int(input())
H = int(input())
M = int(input())
A_min = 24
B_min = 24
for i in range(N):
    A = int(input())
    B = int(input())
    if A > H or (A == H and B >= M):
        if A < A_min:
            A_min = A
            B_min = B
        elif A == A_min:
            if B < B_min:
                B_min = B

answer = (A_min - (H + 1)) * 60 + B_min + 60 - M
print(answer)