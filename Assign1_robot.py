# GEO1000 - Assignment 1
# Authors: Yitong Xia & Fengyan Zhang
# Studentnumbers: xxxxxxx(Yitong Xia) 5462150(Fengyan Zhang)


def wiggle(start,end,moves):
    result = 0 # for every start and end, result need to be set as 0 first
 
    # if the recursion hits the base case
    if moves==0:
        if start==end:
            return 1 # a possible path is found
        else:
            return 0

    # recursion
    result += wiggle(start-1,end,moves-1)
    result += wiggle(start+1,end,moves-1)
    return result

if __name__ == "__main__":

    print("runningrobot.pydirectly")
    print(wiggle (1, 4, 5))
    print(wiggle (4, 1, 5))
    print(wiggle (1, 4, 2))
