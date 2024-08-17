"""
author: rohan singh
pythond solution for can place flowers problem stated in flowerPlacement.md
"""



# imports
from typing import List



# solution
class Solution:

    # function for problem
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        idx = 1

        # for the first pot
        if flowerbed[0:2] == [0,0] or (len(flowerbed)==1 and flowerbed[0] == 0):
            n-=1
            flowerbed[0] = 1

        while idx < len(flowerbed)-1 and n >= 0:

            if flowerbed[idx-1:idx+2] == [0,0,0]:
                flowerbed[idx] = 1
                n -= 1

            idx += 1
        
        # for the last pot
        if flowerbed[len(flowerbed)-2:] == [0,0]:
            n-=1
        
        return n <= 0




# main function for testing
def main():
    
    demo = Solution()


    # test case 1
    flowerbed = [1,0,0,0,1]
    n = 1
    if demo.canPlaceFlowers(flowerbed=flowerbed,n=n):
        print("passed test case 1 :)")
    else:
        print("failed test case 1 :(")

    
    # test case 1
    flowerbed = [1,0,0,0,1]
    n = 2
    if demo.canPlaceFlowers(flowerbed=flowerbed,n=n) is False:
        print("passed test case 1 :)")
    else:
        print("failed test case 1 :(")




if __name__ == "__main__":
    main()