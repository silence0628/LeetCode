# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:58:20 2018

@author: Administrator
"""
import time
#%%
"""这是网络上别人的"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for index,value in enumerate(nums):
            print('x'*80)
            sub = target - value
            if sub in dic:
                print(dic[sub],index)
                return [dic[sub],index]
            else:
                print(index)
                dic[value] = index
        

num=[3,2,4,6,4,11,2]
targets = 8

start = time.clock()

Solution().twoSum(nums=num,target=targets)
end = time.clock()
print(end-start)
#%%
"""这是我自己写的，时间复杂度差不多，但是感觉没有上面的具有规范性"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = len(nums)
        
        for i in range(k):
            err = target-nums[i]
            if err in nums:
                return [i,nums.index(err)]
            
            
            
            
#            for j in range(l,k):
#                total = nums[i]+nums[j]
#                if total==target:
#                    return [i,j]
num=[3,2,4,6,4,11,2]
targets = 8
start = time.clock()
a =Solution().twoSum(nums=num,target=targets)
end = time.clock()
print(end-start)