"""
code: rohan singh
code for container with the most water problem stated in the waterContainer.md
"""


# imports
from typing import List



# solution class
class Solution:

    
    # function for the problem solution
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        for i in range(len(height)-1):
            for j in range(i, len(height)):
                temp = (j-i)*min(height[i],height[j])
                area = max(area, temp)

        return area
    


# main function for testing
def main():
    

    demo = Solution()


    # test case 1
    height = [1,8,6,2,5,4,8,3,7]
    if demo.maxArea(height) == 49:
        print("passed test case 1 :)")
    else:
        print("failed test case 1 :(")

    
    # test case 2
    height = [1,1]
    if demo.maxArea(height) == 1:
        print("passed test case 2 :)")
    else:
        print("failed test case 2 :(")




if __name__ == "__main__":
    main()