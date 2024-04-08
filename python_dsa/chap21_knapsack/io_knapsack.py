def knapsack(values, weights, capacity):
    # 물건의 개수
    n = len(values)
    # DP 테이블 초기화
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # DP를 이용하여 해결
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # 현재 물건을 넣을 수 있다면, 넣는 경우와 넣지 않는 경우 중 최대 가치를 선택
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                # 현재 물건을 넣을 수 없다면, 이전 물건까지의 가치를 상속
                dp[i][w] = dp[i-1][w]

    # 최대 가치 반환
    return dp[n][capacity]

# 예시 입력
values = [60, 100, 120] # 각 물건의 가치
weights = [10, 20, 30] # 각 물건의 무게
capacity = 50 # 배낭의 최대 용량

# 함수 실행
max_value = knapsack(values, weights, capacity)
print(f"Maximum value in knapsack = {max_value}")
