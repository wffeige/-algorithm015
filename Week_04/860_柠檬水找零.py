


class Solution(object):
    """
    在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

    顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

    每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

    注意，一开始你手头没有任何零钱。

    如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/lemonade-change
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def lemonadeChange(self, bills):
        """
        思路
            - 遍历账单
            - 计算每次的收入和支出
                - 通过记录5 美元、10美元的张数 判断是否能完成本次的交易
        :param bills:
        :return:
        """
        five_amounts = ten_amounts = 0

        for bil in bills:
            if bil == 5:
                five_amounts += 1

            elif bil == 10:
                if five_amounts >= 1:
                    five_amounts -= 1
                    ten_amounts += 1
                else:
                    return False
            else:
                if five_amounts >= 1 and ten_amounts >= 1:
                    five_amounts -= 1
                    ten_amounts -= 1
                elif five_amounts >= 3:
                    five_amounts -= 3

                else:
                    return False

        return True


data = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]
print(Solution().lemonadeChange(data))















        #
        # five = ten = 0
        #
        # for bill in bills:
        #
        #     if bill == 5:
        #         five += 1
        #     elif bill == 10:
        #         if not five:
        #             return False
        #         five -= 1
        #         ten += 1
        #     else:
        #         if ten and five:
        #             ten -= 1
        #             five -= 1
        #         elif five >= 3:
        #             five -= 3
        #         else:
        #             return False
        # return True

