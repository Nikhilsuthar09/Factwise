def robber(nums):
  if not nums:
    return 0 
  if len(nums)==1:
    return nums[0]
  
  def simpleRob(nums):
    prev, curr = 0, 0
    for num in nums:
      prev, curr = curr, max(prev+ num, curr)
    return curr
  
  case1 = simpleRob(nums[:-1])
  case2 = simpleRob(nums[1:])
  return max(case1, case2)

nums = [1,2,3]
result = robber(nums)
print(result)