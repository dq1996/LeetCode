# 给定一个整数数组 nums 和一个整数目标值 target
# 在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
#
# 限制：
# 返回的下标不相同，下标返回顺序不作要求
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案
#
# 示例：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

from typing import List


# 执行用时3008s
# 内存消耗15.2MB
# 时间复杂度O(n2)
# 空间复杂度O(1)
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == '__main__':
    print(Solution().twoSum([3, 3], 6))
