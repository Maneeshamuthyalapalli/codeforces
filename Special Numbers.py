def find_kth_special_number(n, k):
    MOD = 10**9 + 7
    result = 0
    power = 1
    while k > 0:
        if k % 2 == 1:
            result = (result + power) % MOD
        power = (power * n) % MOD
        k //= 2
    return result
import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
results = []
for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    index += 2
    results.append(find_kth_special_number(n, k))
for result in results:
    print(result)
