def round3(sub1, sub2):
    arr1 = [int(x) for x in sub1.split()]
    arr2 = [int(x) for x in sub2.split()]
    if sum(arr1) != 100: 
        print(f"ERROR: SUBMISSION {sub1} NOT LEGAL")
    if sum(arr2) != 100: 
        print(f"ERROR: SUBMISSION {sub2} NOT LEGAL")
    score = sum([(i+1) if abs(arr1[i] - arr2[i]) >= 7 else 0 for i in range(10)])
    return (score, score)