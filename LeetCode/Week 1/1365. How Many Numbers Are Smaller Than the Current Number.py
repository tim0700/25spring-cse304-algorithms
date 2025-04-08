'''
1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
'''


def smallerNumbersThanCurrent(nums:list) -> list[int]:
    tempList = nums.copy()
    nums.sort()
    for i in range (len(nums)):
        for j in range (len(nums)):
            if tempList[i] == nums[j]:
                tempList[i] = j
                break
    return tempList

#  시간 복잡도 n^2

def smallerNumbersThanCurrent(nums:list) -> list[int]:
    # 정렬된 배열의 복사본 만들기
    sorted_nums = sorted(nums)
    
    # 각 숫자보다 작은 숫자의 개수를 저장할 딕셔너리
    count_map = {}
    
    # 각 숫자의 첫 등장 위치 찾기 (중복 처리를 위해 중요!)
    for i, num in enumerate(sorted_nums):
        # 딕셔너리에 아직 없는 숫자만 추가 (첫 등장 위치만 기록)
        if num not in count_map:
            count_map[num] = i
    
    # 결과 리스트 생성
    result = [count_map[num] for num in nums]
    
    return result

#  시간 복잡도 nlogn