__author__ = 'MacPu'

#思路是利用字典，将num保存成一个key，sum1 ＋ sum2 ＝ target， => sum2 ＝ target － sum1,最后只需要看字典里是否有这个key即可，

class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num] + 1, i + 1)
            lookup[num] = i

if __name__ == '__main__':
    print "index1=%d, index2=%d" % Solution().twoSum((2, 7, 11, 15), 9)


