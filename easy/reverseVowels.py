"""
author: rohan singh
python solution for the problem stated in reverseVowels.md
"""



# solution
class Solution:

    # function to reverse the vowels
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

        i = -1
        j = len(s)

        while i < j:
            i += 1
            j -= 1
            while i < j and s[i] not in vowels:
                i += 1
            while j > i and s[j] not in vowels:
                j -= 1
            if i >= j:
                return s
            s = self.swap(s,i,j)

        return s

    # helper function to swap the vowels in the string         
    def swap(self, s, i, j):
        s_i = s[i]
        s_j = s[j]
        return s[0:i] + s_j + s[i+1:j] +s_i + s[j+1:]



# main function for testing
def main():
    
    demo = Solution()

    # test case 1
    s = "hello"
    if demo.reverseVowels(s) == "holle":
        print("Test 1 passed :)")
    else:
        print("Test 1 failed :(")

    # test case 2
    s = "leetcode"
    if demo.reverseVowels(s) == "leotcede":
        print("Test 2 passed :)")
    else:
        print("Test 2 failed :(")

    # test case 3
    s = "Live on evasions? No, I save no evil."
    if demo.reverseVowels(s) == "Live on evasIons? No, i save no evil.":
        print("Test 3 passed :)")
    else:
        print("Test 3 failed :(")


    # test case 4
    s = "Sore was I ere I saw Eros."
    if demo.reverseVowels(s) == "SorE was I ere I saw eros.":
        print("Test 4 passed :)")
    else:
        print("Test 4 failed :(")


if __name__ == "__main__":
    main()


