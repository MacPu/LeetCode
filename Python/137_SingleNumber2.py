__author__ = 'pudegui'

# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# 思路：还是如SingleNumber的思路是一样的，但是这次出现三次才删除。

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        result = {}
        for i,num in enumerate(nums):
            if(num in result):
                if result[num] == 2:
                    result.pop(num)
                else:
                    result[num] += 1
            else :
                result[num] = 1;

        for key in result.keys():
            return key


if __name__ == '__main__':
    print "answer = %d" % Solution().singleNumber([1,1,3,4,4,3,6,7,7,1,3,4,7])