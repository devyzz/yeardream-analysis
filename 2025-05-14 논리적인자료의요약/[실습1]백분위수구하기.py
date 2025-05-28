import numpy as np

def calculate_percentile(data, p):
    #1. 데이터 정렬
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    #2. 위치계산 (nxp)
    position = n * p
    
    #3. 백분위수 계산
    if position.is_integer():
        pos = int(position)
        percentile_value = (sorted_data[pos - 1] + sorted_data[pos]) / 2
    else:
        pos = int(np.ceil(position))
        percentile_value = sorted_data [pos-1]
        
    return percentile_value

score = [52,55,58,60,63,65]
percentiles = [0.25 , 0.5, 0.75]
print("🔷백분위수 계산 결과")
for p in percentiles:
    percentile_value = calculate_percentile(score,p)
    print(f"{int(p*100)}백분위값 : {percentile_value}")