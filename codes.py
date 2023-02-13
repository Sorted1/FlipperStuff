# Generates All Possible Phone Passcodes
import random, math, os

def comb(L):
      
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    
                    # check if the indexes are not
                    # same
                    if (i!=j and j!=k and i!=k):
                        print(L[i], L[j], L[k], L[l])
                      
# Driver Code
comb([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
