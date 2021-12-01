arr = [1,2,3,2,3]

def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] = j-i
            elif prices[i] > prices[j]:
                answer[i] = j-i 
                break
    return answer


print(solution(arr))