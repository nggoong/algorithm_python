N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0



arr.sort(reverse=True)

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if arr[i] + arr[j] + arr[k] == M:
                answer = arr[i] + arr[j] + arr[k]
                break
            elif arr[i] + arr[j] + arr[k] < M and arr[i] + arr[j] + arr[k] > answer :
                answer = arr[i] + arr[j] + arr[k]

            elif arr[i] + arr[j] + arr[k] > M:
                continue

print(answer)



