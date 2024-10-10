# Leet Code Problem:
# Search through an array to find 2 numbers that sum to the target. Return the index of these numbers.

x = [1,2,3,4,5,6,7,8,9,10]
target = 15

# Below is my initial attempt based on my intuitive reponse to the problem
# def twoSum(nums, target):
#     i = 0
#     while i < len(nums):
#         for j in range(len(nums)):
#             if j != i:
#                 x = nums[i] + nums[j]
#                 if x == target:
#                     return i, j
#         i += 1

# print(twoSum(x,target))



# Below is the repsonse I learnt and will use to solve the problem because it is more efficient.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {} # Create an empty hashmap (dictionary) to store 'index: value' pairs.
        for i in range(len(nums)): # Iterate through the idexes of the nums list.
            complement = target - nums[i] # This calculates the number that would need to be paired witht the current number to achive the target.
            if complement in hashmap: # This checks if the complement exists in the hashmap. If so the complemnt index and the current cursor index are the solution.
                return [hashmap[complement], i] # returns the index of the 2 numbers that sum to target.
            hashmap[nums[i]] = i

solution = Solution() # Create instance of the solution class.

result = solution.twoSum(x,target) # Solve the current two sum problem.

print(result)