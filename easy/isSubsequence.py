"""
author: rohan singh
code for Is Subsequence problem stated in isSubsequence.md
"""



# solution class
class Solution:

    # function to solve the problem
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        if len(t) <= len(s):
            return t == s
        
        while(j < len(t)):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i += 1
            j+=1
        
        return i == len(s)
    


# main function for testing
def main():
    
    demo = Solution()


    # test case 1
    s = "abc"
    t = "ahbgdc"
    if demo.isSubsequence(s,t) is True:
        print("passed test case 1 :)")
    else:
        print("failed test case 1 :(")


    # test case 2
    s = "axc"
    t = "ahbgdc"
    if demo.isSubsequence(s,t) is False:
        print("passed test case 2 :)")
    else:
        print("failed test case 2 :(")




if __name__ == "__main__":
    main()