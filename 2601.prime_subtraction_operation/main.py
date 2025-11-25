import math


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Bruce-force solution
        def is_prime(num):
            if num < 2:
                return False

            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False

            return True

        def is_sorted(nums):
            # If it not strictly increasing sorted.
            # return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
            return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))

        # The "prev_num" variable should be "0"
        # so that there is no error when checking the first number.
        prev_num = 0
        for idx in range(len(nums)):
            if is_sorted(nums):
                return True

            max_prime_range = nums[idx] - prev_num
            current_largest_prime = 0

            # The "current_largest_prime" variable should be "0"
            # to avoid the case that the first number is less than 2.
            for i in reversed(range(2, max_prime_range)):
                if is_prime(i):
                    current_largest_prime = i
                    break

            if nums[idx] - current_largest_prime <= prev_num:
                print(nums, current_largest_prime, idx)
                return False

            prev_num = nums[idx] - current_largest_prime
            nums[idx] = prev_num

        return True
