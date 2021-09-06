# GEO1000 - Assignment 1
# Authors:Yitong Xia & Fengyan Zhang
# Studentnumbers:xxxxxxx(Yitong Xia) 5462150(Fengyan Zhang)

import math


def distance(x1, y1, x2, y2):
    '''Calculate the Cartesian distance between 2 points.(fruitful function)'''   
    return math.sqrt((x1-x2)**2+(y1-y2)**2) # not necessary to consider exceptions here
   

def angle(a, b, c):
    '''Calculate the angle (in radians) given by three sides of a triangle.(in radians)'''
    try:
        division = 2*a*b # divided into parts because of exception considering
        result = (a**2+b**2-c**2)/division
        final = math.acos(result)
        return final
    except ZeroDivisionError as e: # division shouldn't be 0
        print("angle function:",e)
    except ValueError as e: # domain of acos() is:(-1,1)
        print("angle function:",e)
 

def cot(x):
    '''Calculate the cot(), x is in radians'''
    try:
        return 1/math.tan(x)
    except ZeroDivisionError as e: 
        print("cot function:",e)
    except ValueError as e: # domain of cot() is:≠K*math.pi
        print("cot function:",e)


def k(angle_corner, angle_interior):
    '''Calculate the parameter k'''
    try:
        division = cot(angle_corner)-cot(angle_interior)
        return 1/division
    except ZeroDivisionError as e: 
        print("k function:",e)
    except TypeError as e: # check whether the two return values of cot() function are legal
        print("k function:",e)


def tienstra(ax, ay, bx, by, cx, cy, alpha, beta):
    '''Calculate unknown point coordinates'''
    try:
        # Transform the given interior angles (α and β) from degrees to radians
        r_alpha = math.radians(alpha)
        r_beta = math.radians(beta)

        # Calculate the angle γ
        gamma = 360-alpha-beta
        r_gamma = math.radians(gamma)

        # Calculate the length of AB,BC,CA
        dist_AB = distance(ax,ay,bx,by) # AB
        dist_BC = distance(bx,by,cx,cy) # BC
        dist_AC = distance(ax,ay,cx,cy) # AC

        # Calculate the angel A,B,C
        angle_A = angle(dist_AB,dist_AC,dist_BC) # ∠A
        angle_B = angle(dist_AB,dist_BC,dist_AC) # ∠B
        angle_C = angle(dist_AC,dist_BC,dist_AB) # ∠C

        # Calculate k1,k2,k3
        k1 = 1/(cot(angle_A)-cot(r_alpha))
        k2 = 1/(cot(angle_B)-cot(r_beta))
        k3 = 1/(cot(angle_C)-cot(r_gamma))

        # Calculate px,py(coordinates of unknown points)
        px = (k1*ax+k2*bx+k3*cx)/(k1+k2+k3)
        py = (k1*ay+k2*by+k3*cy)/(k1+k2+k3)

        # return the xy coordinates
        return (px,py)
    except ZeroDivisionError as e:
        print("tienstra function:",e)
    except TypeError as e: 
        print("tienstra function:",e)
    

tienstra(
    1000.0, 5300.0,
    2200.0, 6300.0,
    3100.0, 5000.0,
    115.052, 109.3045)

if __name__ == "__main__":
    
    result = tienstra(1000.0, 5300.0,
    2200.0, 6300.0,
    3100.0, 5000.0,
    115.052, 109.3045)
    print(result)

    test_result = tienstra(0, 0,
    2, 0,
    1, 1.732,
    120, 120)
    print(test_result)

    