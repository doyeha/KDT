# ------------------------------------------------------- 
# range() 내장함수
# - 수의 범위를 생성하는 함수
# - range 객체 결과 반환
# - 형식
#   range(시작, 끝+1, 간격)
#   range(끝+1)  : 0 <= ~ < 끝+1  간격 1 
#   range(10)  : 0 <= ~ < 10  간격 1 : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#   range(11)  : 0 <= ~ < 11  간격 1 : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# ------------------------------------------------------- 

nums = range(11)
print(f"nums => {nums}")
print(f"nums 타입 => {type(nums)}")
print(f"nums 개수 => {len(nums)}")
print(f"nums 원소 => {nums[0]}, {nums[-3]}")
print(f"nums 슬라이싱 => {nums[0:-4]}")

#[실습] 1부터 100까지 정수 숫자 데이터에서 3의 배수만 출력하세요.
# nums=[1,2,3,4,5,6 ...., 100]
nums = range(1, 101)
for n in nums:
    if n%3==0:
        print(n)
for n in nums:
    if not n%3:
        print(n)


nums2 = range(3,101,3)
for n in nums2: print(n, end=" ")

# range ==> list 형변환
nums3 = list(nums2)
print(nums2, nums3, sep="\n")

