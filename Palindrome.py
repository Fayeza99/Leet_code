class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        tmp = x
        reversed_num = 0

        while tmp > 0:
            digit = tmp % 10
            reversed_num = reversed_num * 10 + digit
            tmp = tmp // 10
        return x == reversed_num

def main():
    solution = Solution()
    test_numbers = [121, -121, 12321, 123, 10, 0, 1221, 1234321, -101]
    
    for num in test_numbers:
        result = solution.isPalindrome(num)
        print(f"{num} is palindrome: {result}")

if __name__ == "__main__":
    main()
