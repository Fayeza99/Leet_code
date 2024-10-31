class Solution(object):
    def merge(self, nums1, m, nums2, n):
        last1, last2 = m - 1, n - 1
        fill_index = m + n - 1
        
        while last1 >= 0 and last2 >= 0:
            if nums1[last1] > nums2[last2]:
                nums1[fill_index] = nums1[last1]
                last1 -= 1
            else:
                nums1[fill_index] = nums2[last2]
                last2 -= 1
            fill_index -= 1
        
        while last2 >= 0:
            nums1[fill_index] = nums2[last2]
            fill_index -= 1
            last2 -= 1

# def main():
#     # Create instances of arrays and their respective sizes
#     nums1 = [1, 2, 3, 0, 0, 0]
#     m = 3
#     nums2 = [2, 5, 6]
#     n = 3

#     # Instantiate the Solution class
#     solution = Solution()
    
#     # Before merging, print the original nums1
#     print("Before merge:")
#     print("nums1:", nums1[:m])  # Print only the initialized part of nums1

#     # Call the merge method
#     solution.merge(nums1, m, nums2, n)
    
#     # After merging, print the modified nums1
#     print("After merge:")
#     print("nums1:", nums1)

# if __name__ == "__main__":
#     main()
