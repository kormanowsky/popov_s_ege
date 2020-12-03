N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
array = array[::-1]
for i in range(N):
    print(array[i])