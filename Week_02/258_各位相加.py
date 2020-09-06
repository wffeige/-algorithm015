class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        new_num = 0
        for i in str(num):
            new_num += int(i)

        if new_num >= 10:
            return self.addDigits(new_num)
        else:
            return new_num