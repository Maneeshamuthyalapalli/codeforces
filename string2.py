sum_str = input().split('+')
summands = [int(num) for num in sum_str]
summands.sort()
new_sum = '+'.join(map(str, summands))
print(new_sum)
