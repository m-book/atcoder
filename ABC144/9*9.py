nums = list(map(int, input().split(" ")))

num_range = range(1, 10)

if nums[0] in num_range and nums[1] in num_range:
    print(nums[0] * nums[1])
else:
    print(-1)