# 输出结果
print("整数:", end="")
for item in sorted_frequency:
    print(f"{item[0]}, ", end="")
print("\n频率：", end="")
for item in sorted_frequency:
    print(f"{item[1]}, ", end="")