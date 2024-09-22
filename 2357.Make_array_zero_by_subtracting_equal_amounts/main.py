class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        update_arr = sorted(nums)
        count = 0
        if sum(update_arr) == 0:
            return count

        while(True):
            while(True):
                if update_arr[0] == 0:
                    update_arr.pop(0)
                else:
                    break
            min_update = min(update_arr)
            for idx, num in enumerate(update_arr):
                update_arr[idx] = num - min_update
            count += 1
            if sum(update_arr) == 0:
                break
        return count