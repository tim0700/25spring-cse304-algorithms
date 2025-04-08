'''
136. Single Number
https://leetcode.com/problems/single-number/description/
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

'''
최적 솔루션: XOR 비트 연산 사용
이 문제의 가장 우아한 해결책은 XOR(^) 연산을 활용하는 것입니다! XOR의 세 가지 특성이 핵심이에요:

a ^ 0 = a
a ^ a = 0
a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

즉, 모든 숫자가 자기 자신과 XOR 연산을 하면 0이 되고, 중복되는 모든 숫자는 서로 상쇄됩니다!

---

XOR 연산이란?
XOR(exclusive OR)는 '배타적 논리합'이라고도 하며, 두 비트가 서로 다를 때만 1을 반환하는 비트 연산이에요.
0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0
파이썬에서는 ^ 기호로 표현돼요! 숫자로 예를 들면:
python
            5 ^ 3   = 6
# 이진수로: 101 ^ 011 = 110

XOR의 마법 같은 특성
XOR는 정말 놀라운 특성들을 가지고 있어요:

항등성: a ^ 0 = a
어떤 수와 0을 XOR하면 그 수 자체가 됩니다!


자기 자신과의 소멸: a ^ a = 0
같은 숫자끼리 XOR하면 항상 0이 됩니다!


교환법칙: a ^ b = b ^ a
순서를 바꿔도 결과는 같아요!


결합법칙: (a ^ b) ^ c = a ^ (b ^ c)
그룹화해도 결과는 변하지 않아요!


자기 역원: a ^ b ^ a = b
어떤 값에 동일한 값을 두 번 XOR하면 원래 값이 복원됩니다!
'''