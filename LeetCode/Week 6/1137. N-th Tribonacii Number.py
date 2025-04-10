'''
1137. N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/description/
'''

def tribonacci(n: int) -> int:
    T_n = [0] * (n + 1)
    T_n[0] = 0
    T_n[1] = 1
    T_n[2] = 1

    if n == 0 or n == None:
        return T_n[0]
    elif n == 1 or n == 2:
        return T_n[n]
    else:
        for i in range (3, n+1):
            T_n[i] = T_n[i-1] + T_n[i-2] + T_n[i-3]
    return T_n, T_n[n]

print (tribonacci(1)) # 44