class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for x in range(n):
            for y in range(x+1,n):
                if(nums[x] == nums[y]):
                    if (x * y) % k == 0:
                        count +=1
                else:
                    continue
        return count
        