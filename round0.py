import pandas as pd 

def round0(sub1, sub2):
    arr1 = sub1.split()
    arr2 = sub2.split()
    score1 = sum([(i+1) if arr1[i] > arr2[i] else 0 for i in range(10)])
    score2 = sum([(i+1) if arr2[i] > arr1[i] else 0 for i in range(10)])
    if score1 > score2:
        return (3, 0)
    if score2 > score1:
        return (0, 3)
    return (1, 1)