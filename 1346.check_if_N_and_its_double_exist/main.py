class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for idx, _ in enumerate(arr):
            i = 1
            while idx + i < len(arr):
                if arr[idx] == arr[idx + i] * 2 or arr[idx] == arr[idx + i] / 2:
                    return True
                i += 1
        return False
