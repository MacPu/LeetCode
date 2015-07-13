__author__ = 'MacPu'

# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#思路：如果有一个新的数字，先判断他是否在字典result里面，如果在就将他删除，如果不在就保存在这个字典里面，这样的话最后剩下的一个就是答案了。


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        result = {}
        for i,num in enumerate(nums):
            if(num in result):
                result.pop(num)
            else :
                result[num] = i;

        for key in result.keys():
            return key


if __name__ == '__main__':
    print "answer = %d" % Solution().singleNumber([1,1,3,4,4,3,6,7,7])
