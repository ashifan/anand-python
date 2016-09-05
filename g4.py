def remove_adjacent(nums):
  result = []
  for num in nums:
    if len(result) == 0 or num != result[-1]:
      result.append(num)
  return result
nums = [1,2,2,3]
print remove_adjacent(nums)