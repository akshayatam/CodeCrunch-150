def maxArea(height: list[int]) -> int:
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
    """
    #length of height
    n=len(height) 

    # starting and last index of array
    l,r=0,n-1 

    # initailly result is zero
    res=0 

    while l<r: 
        #storing max area of water in res for every iteration
        res=max(res,(r-l)*min(height[l],height[r])) 

        #updating the smallest vertical line hoping 
        #there would be a bigger vertical line after updation.
        if height[l]<height[r]: 
            l+=1
        else:
            r-=1
    return res


def main():
    tests: list[list[int]] = [[1,8,6,2,5,4,8,3,7], [1,1]]

    for test in tests:
        print(maxArea(test))

if __name__ == "__main__":
    main()