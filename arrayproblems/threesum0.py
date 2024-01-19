class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      nums.sort()
      result = []
      for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = len(nums) - 1

            while mid < right:
                summ = nums[left] + nums[mid] + nums[right]
                if summ < 0:
                    mid += 1
                elif summ > 0:
                    right -= 1
                else:
                    result.append([nums[left],nums[mid],nums[right]]) 
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid+=1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1

                    mid +=1
                    right -= 1
            return result 
        
        






# Explanation
# left : leftmost index (iterate)
# mid : left + 1
# right: rightmost index (len(nums) - 1)

# The main idea is that we fix left index. Then we find the sum of three values (left, mid, right) where mid is initially left + 1 and right is initially len(nums) - 1.

# If the current sum is less than 0, we move mid to right by one since the nums are sorted in ascending order.
# Else If the current sum is greater than 0, we move right to left by one.

# Else where current sum is equal to 0, we add (left, mid, right) to result. And by moving mid to right by one and right to left by one at the same time, we keep going on finding other combinations.

# Dealing with Duplicates
# if left > 0 and nums[left] == nums[left-1]: continue
# Since we fix left and find combinations by only moving mid and right, if current left value is equal to the previous one, the combinations would be the same.

# while mid < right and nums[mid] == nums[mid+1]: mid+=1
# while mid < right and nums[right] == nums[right-1]: right -= 1

# For example, if nums = [-1,0,0,1,1,1,1], the first combination we can find is [-1,0,1] where "-1" is 0th index, "0" is 1st index and "1" is 3rd index. Another combination [-1,0,1] can be found if we take left and mid the same but right 4th index. However, since we do not want duplicates, we can skip all the same values of mid and right by using the code above.