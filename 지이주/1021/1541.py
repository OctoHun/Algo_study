s = list(input().split('-'))
res = 0
nums = []
for i in s:
  num = i.split("+")
  x = 0
  for j in num:
    x += int(j)
  nums.append(x)
res = nums[0]
for i in range(1,len(nums)):
  res -= nums[i]

print(res)
