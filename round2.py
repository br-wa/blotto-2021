triples = [
    (0, 1, 2), 
    (3, 4, 5), 
    (6, 7, 8), 
    (0, 3, 6),
    (1, 4, 7), 
    (2, 5, 8), 
    (0, 4, 8), 
]

def round2(sub1, sub2):
    arr1 = [int(x) for x in sub1.split()]
    arr2 = [int(x) for x in sub2.split()]
    sites1 = [1 if arr1[i] > arr2[i] else 0 for i in range(10)]
    sites2 = [1 if arr2[i] > arr1[i] else 0 for i in range(10)]
    score1 = sum(sites1)
    score2 = sum(sites2)
    for triple in triples:
        if sum([sites1[i] for i in triple]) == 3:
            score1 += 2
        if sum([sites2[i] for i in triple]) == 3:
            score2 += 2
            
    if score1 > score2:
        return (3, 0)
    if score2 > score1:
        return (0, 3)
    return (1, 1)