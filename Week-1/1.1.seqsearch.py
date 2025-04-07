from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int: 
    location = 0

    # Complete the code here
    location = -1
    for i in range (n):
        if x == S[i]:
            location = i
            break
        
    return location