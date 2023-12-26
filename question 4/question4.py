def search(nums, target):
  left, right=0, len(nums)-1
  while left<=right:
    mid = left + (right - left) //2

    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return left

nums = [1, 3, 5, 6]
target = 7
result = search(nums, target)
print(result)