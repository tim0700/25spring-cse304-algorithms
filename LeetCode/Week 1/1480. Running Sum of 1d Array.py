'''
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/description/
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #your code
        result = [0]*(len(nums))
        for i in range (len(nums)):
            for k in range (i+1):
                result[i] += nums[k]
        return result
    

    # 더 좋은 방법 많음, 리팩토링 ㄱㄱㄱ