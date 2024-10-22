class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return nums

def main():
    solution = Solution()
    
    nums = [2]
    result = solution.removeElement(nums, 3)
    
    print(nums)

if __name__ == "__main__":
    main()
