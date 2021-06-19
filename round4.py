def round4(sub1, sub2):
    arr1 = [int(x) for x in sub1.split()]
    arr2 = [int(x) for x in sub2.split()]
    if sum(arr1) != 100 and min(arr1 < 0):
        print(f"ERROR: SUBMISSION {sub1} NOT LEGAL")
    if sum(arr2) != 100 and min(arr2 < 0):
        print(f"ERROR: SUBMISSION {sub2} NOT LEGAL")
    score1 = sum([(i+1) if arr1[i] > arr2[i] and arr1[i] + arr2[i] + 5*i <= 70 else 0 for i in range(10)])
    score2 = sum([(i+1) if arr2[i] > arr1[i] and arr1[i] + arr2[i] + 5*i <= 70 else 0 for i in range(10)])
    if score1 > score2:
        return (3, 0)
    if score2 > score1:
        return (0, 3)
    return (1, 1)