"""
author: rohan singh
code for the problem stated in mergeStrings.md
"""


# solution for problem
class Solution:

    # function for alternate merge
    def mergeAlternately(self, word1: str, word2: str) -> str:

        idx = 0
        mergedWord = ""
        
        while (idx < len(word1) and idx < len(word2)):
            mergedWord += word1[idx]
            mergedWord += word2[idx]
            idx += 1
        
        
        while idx < len(word1):
            mergedWord += word1[idx]
            idx += 1


        while idx < len(word2):
            mergedWord += word2[idx]
            idx += 1
        
    
        return mergedWord



# main function for testing
def main():

    demo = Solution()

    # test1
    word1 = "abc"
    word2 = "pqr"
    if demo.mergeAlternately(word1=word1, word2=word2) == "apbqcr":
        print("test 1 passed :)")
    else:
        print("test 1 failed :(")


    # test2
    word1 = "ab"
    word2 = "pqrs"    
    if demo.mergeAlternately(word1=word1, word2=word2) == "apbqrs":
        print("test 2 passed :)")
    else:
        print("test 3 failed :(")


    # test 3
    word1 = "abcd"
    word2 = "pq"
    if demo.mergeAlternately(word1=word1, word2=word2) == "apbqcd":
        print("test 1 passed :)")
    else:
        print("test 1 failed :(")



if __name__ == "__main__":
    main()


