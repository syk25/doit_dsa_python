def fractional_knapsack(value, weight, capacity):
    # 단위 무게 당 가치에 따라 항목을 정렬
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    
    max_value = 0
    fractions = [0] * len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1  # 전체 물건을 넣을 수 있으면 1로 설정
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]  # 배낭에 남은 용량만큼만 물건을 넣음
            max_value += value[i] * (capacity / weight[i])
            break

    return max_value, fractions

# 예시 입력
values = [60, 100, 120]  # 각 물건의 가치
weights = [10, 20, 30]  # 각 물건의 무게
capacity = 50  # 배낭의 최대 용량

# 함수 실행
max_value, fractions = fractional_knapsack(values, weights, capacity)
print(f"Maximum value in knapsack = {max_value}")
print(f"Fractions of items taken: {fractions}")
