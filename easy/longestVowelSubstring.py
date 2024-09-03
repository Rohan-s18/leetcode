"""
author: rohan singh
code for the longest vowel substring problem stated in longestVowelSubstring.md
"""



# solution class
class Solution:

    def longestSubstring(self, s:str) -> int:

        vowels = ['a','e','i','o','u']
        max_len = 0
        curr_len = 0

        for char in s:
            
            if char in vowels:
                curr_len += 1
            else:
                curr_len = 0
            
            max_len = max(curr_len, max_len)

        return max_len





# main function for testing
def main():

    demo = Solution()

    s =""
    if demo.longestSubstring(s) == "":
        print("Test case 1 passed :)")
    else:
        print("Test case 1 failed :(")