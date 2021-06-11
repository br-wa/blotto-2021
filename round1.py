def round1(sub1, sub2):
    arr1 = [int(x) for x in sub1.split()]
    arr2 = [int(x) for x in sub2.split()]
    score1 = sum([1 if arr1[i] > arr2[i] and arr1[i] + arr2[i] <= 5 * (i+1) else 0 for i in range(10)])
    score2 = sum([1 if arr2[i] > arr1[i] and arr1[i] + arr2[i] <= 5 * (i+1) else 0 for i in range(10)])
    if score1 > score2:
        return (3, 0)
    if score2 > score1:
        return (0, 3)
    return (1, 1)