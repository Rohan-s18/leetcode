"""
author: rohan singh
code for string greatest common divisor probelm stated in stringGCD.md
"""


# solution for the problem
class Solution:

    # function for the solution
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str2) > len(str1):
            str1, str2 = str2, str1

        gcd = ""

        for i in range(1, len(str2)+1, 1):

            if self.isDivisor(str1, str2[0:i]) and self.isDivisor(str2, str2[0:i]):
                gcd = str2[0:i]


        return gcd
    
    
    # function that checks if str2 divides str1
    def isDivisor(self, str1: str, str2: str) -> bool:

        if len(str1)%len(str2) != 0:
            return False
        
        for j in range(0, len(str1), len(str2)):
            if str1[j:j+len(str2)] != str2:
                return False
        
        return True





# main function for testing
def main():
    
    demo = Solution()

    # test 1
    str1 = "ABCABC"
    str2 = "ABC"
    if demo.gcdOfStrings(str1=str1, str2=str2) == "ABC":
        print("test 1 passed :)")
    else:
        print("test 1 failed :(")
        print(demo.gcdOfStrings(str1=str1, str2=str2))

    # test 2
    str1 = "ABABAB"
    str2 = "ABAB"
    if demo.gcdOfStrings(str1=str1, str2=str2) == "AB":
        print("test 2 passed :)")
    else:
        print("test 2 failed :(")


    # test 3
    str1 = "LEET"
    str2 = "CODE"
    if demo.gcdOfStrings(str1=str1, str2=str2) == "":
        print("test 3 passed :)")
    else:
        print("test 3 failed :(")





if __name__ == "__main__":
    main()


