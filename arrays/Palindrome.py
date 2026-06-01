#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

# Example usage:
solution = Solution()
print(solution.isPalindrome(121))  # True
print(solution.isPalindrome(-121)) # False
print(solution.isPalindrome(10))   # False