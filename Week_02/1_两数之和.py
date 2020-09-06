# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表
#  👍 8962 👎 0


class Solution(object):

    def twoSum(self, nums, target):
        hashmap = dict()
        for index, value in enumerate(nums):
            hashmap[value] = index

        for i in range(len(nums)):
            j = target - nums[i]
            if j in hashmap.keys():
                if i != hashmap[j]:
                    return i, hashmap[j]

    def twoSum2(self, nums, target):
        hashmap = dict()
        for i, value in enumerate(nums):
            j = target - nums[i]
            if j in hashmap.keys():
                if i != hashmap[j]:
                    return i, hashmap[j]
            else:
                hashmap[value] = i

    def twoSum3(self, nums, target):
        for index in range(len(nums)):
            if target - nums[index] in nums:
                index1 = nums.index(target - nums[index])
                if index1 != index:
                    return [index, index1]


def main():
    nums = [2,7,11,15]
    target = 9

    # nums = [3,3]
    # target = 6
    print(Solution().twoSum(nums, target))


if __name__ == "__main__":
    main()
