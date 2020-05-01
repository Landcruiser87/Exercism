# nums = [2,7,11,15]
# target = 9

# # class Solution:
# #     def twoSum(self, nums: list[int], target: int) -> list[int]:
#%%
nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
	for i, num in enumerate(nums):
		for j in range(i+1, len(nums)):
			if num + nums[j] == target:
				return [i, j]

answer = twoSum(nums,target)
# for idx, x in enumerate(nums):
# 	# print(nums[idx])
#     if nums[idx] + nums[idx+1] == target:
#         answer = [nums[idx], nums[idx+1]]

print(answer)
# answer = twoSum(nums, target)



# %%
