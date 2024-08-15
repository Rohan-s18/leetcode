"""
author: rohan singh
solution for the Greatest Number of Candies Problem defined in greatestNumCandies.md
"""



# imports
from typing import List



# solution
class Solution:

    # function for the solution
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandies = max(candies)

        result = []

        for idx in range(0, len(candies), 1):
            if candies[idx] + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)

        return result



# main function for testing the code
def main():
    
    demo = Solution()

    # test 1
    candies = [2,3,5,1,3]
    extraCandies = 3
    if demo.kidsWithCandies(candies=candies, extraCandies=extraCandies) == [True,True,True,False,True]:
        print("Test 1 passed :)")
    else:
        print("Test 1 failed :(")

    # test 2
    candies = [4,2,1,1,2]
    extraCandies = 1
    if demo.kidsWithCandies(candies=candies, extraCandies=extraCandies) == [True,False,False,False,False] :
        print("Test 2 passed :)")
    else:
        print("Test 2 failed :(")

    # test 3
    candies = [12,1,12]
    extraCandies = 10
    if demo.kidsWithCandies(candies=candies, extraCandies=extraCandies) == [True,False,True]:
        print("Test 3 passed :)")
    else:
        print("Test 3 failed :(")




if __name__ == "__main__":
    main()



