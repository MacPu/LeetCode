__author__ = 'MacPu'

# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

#思路：这道题需要用回溯的思想，需要用到递归。usedMap保存的是已经出现过的数字，current数组保存的当前的组合，
#     先遍历一边nums，如果i没有在usedMap里面出现，就说明没有被用过，则将他添加到current数组里面去，并且在usedMap里面标记已经用过了这个数字
#     接下来再继续递归没有用过的那些nums，还是之前的逻辑，当发现current的长度等于 nums的长度，就证明一个组合就已经找出来了，将他保存到result里面
#     然后就是回溯到上一步，将上一步标记用过的数字标记成没有用过，然后再循环到下一个数字，一直到遍历完整个数组，

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        result = []
        self.backtrack(nums,[],result,{})
        # print(result)
        return result

    def backtrack(self,num,current,result,usedMap):
        if len(current) == len(num):
            #这里之所以这么写是因为，我不知道该如何将一个数组里的值赋给另外一个数组，并且地址不一样。python初学Orz....
            c = []
            for i in current:
                c.append(i)
            result.append(c)
            return

        for i in num:
            if i not in usedMap:
                current.append(i)
                usedMap[i] = 1
                self.backtrack(num,current,result,usedMap)
                current.remove(i)
                del(usedMap[i])


if __name__ == '__main__':
    print Solution().permute([1,2,3])
