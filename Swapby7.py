num = [3,21,5,6,14,8,14,3]
l = len(num)
i = 0
while i < l:
    if num[i] % 7 == 0:
        num[i],num[i + 1] = num[i + 1 ],num[i]
        i = i + 2
    else:
        i = i + 1
print(num)
