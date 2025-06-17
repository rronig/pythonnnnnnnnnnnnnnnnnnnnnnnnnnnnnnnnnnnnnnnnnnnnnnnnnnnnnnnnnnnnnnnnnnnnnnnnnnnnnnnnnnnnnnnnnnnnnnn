count=1
while count <= 5:
    print("Iteration:",count)
    count += 1
nums = [1,2,3,4,5,6,7,8,9]
target=4
for num in nums:
    print(num)
    if num == target:
        print("Found it!")
        break
for num in nums:
    if num > 5:
        continue
    else:
        print(num)