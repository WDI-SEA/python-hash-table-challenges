'''
https://leetcode.com/problems/two-sum/
3. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''    

# def two_sum(nums: list, target: int) ->list:
#   for i in range(len(nums)):
#     for j in range(len(nums)):
#       if i == j: continue
#       if nums[i] + nums[j] == target:
#         return [target]

def two_sum(nums:list, target: int) ->list:
  hash_table = {}
  for i in range(len(nums)):
    difference = target - nums[i]
    if difference not in hash_table:
      hash_table[nums[i]] = 1
    else: 
        return [hash_table[difference], i]

print('it should return [0, 1]', two_sum([2,7,11,15], 9))
print('it should return [1, 2]', two_sum([3,2,4], 6))
print('it should return [3, 4]', two_sum([0,1,2,3,3], 6))