"""
Theatre Square
"""

import math

def theatre_square(n, m, a):
     to_the_right = math.ceil(n / a)
     to_the_left = math.ceil(m / a)

     return (to_the_right * to_the_left)

#m, n, a = list(map(int, input().split()))

#print(theatre_square(m, n, a))


print(theatre_square(6, 9, 2))