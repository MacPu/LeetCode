__author__ = 'MacPu'

#思路就是计算有多少个1，有多少个10，多少个100，以此类推

import  time

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        count, multiplier,left = 0,1,n
        while left > 0 :
            center = left % 10
            right = n % multiplier

            count += (left / 10 + (1 < center)) * multiplier

            if center == 1 :
                count += right + 1

            left /= 10
            multiplier *= 10

        return count



if __name__ == '__main__':
    time1 = time.time();
    print "return %d " % Solution().countDigitOne(101)
    print(time.time() - time1)



