# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:56:31 2021

@author: Ameer Hamza
"""

# text = input("Enter a string: ")
# print(to_ascii(text))

import sys
sys.path.insert(4, "/var/www/html/api_orio/.local/lib/python3.8/site-packages")
from numpy import ones,vstack, float128
from numpy.linalg import lstsq
import gmpy2


args=sys.argv
img_hash= str(args[1])

def to_ascii(text):
    res=""
    for character in text:
        res= (res+str(ord(character)))
    return int(res)

def toDec(hexa):
    return int(hexa, 16)

x1= toDec("fff542b6b1ced2cf8a8f6ca4fd3b8bc9") #ID: 682
y1= toDec("238b1699a9de8052738f2d73532bd460") #ID:551
x2= toDec("c6351be3d6218046128d09334b514bab")
y2= toDec("e9f0214184931d19c67a5ad951a9d7de")
img_hash_dec= gmpy2.mpfr(toDec(img_hash))

gmpy2.get_context().precision=1000
points = [(gmpy2.mpfr(x1),
           gmpy2.mpfr(y1)),
          (gmpy2.mpfr(x2),
           gmpy2.mpfr(y2))]
#print(points)
#x_coords, y_coords = zip(*points)
#A = vstack([x_coords,ones(len(x_coords))]).T
#m, c = lstsq(A, y_coords)[0]
#print("Line Solution is y = {m}x + {c}".format(m=m,c=c))


m = (points[1][1] - points[0][1])/(points[1][0] - points[0][0])
c= points[0][1]-(m*points[0][0])

print(hex(round((m*img_hash_dec)+c)).split('x')[-1])
