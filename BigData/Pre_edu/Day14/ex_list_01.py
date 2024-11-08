# -------------------------------------------------------
# 리스트 자료형 살펴보기
# -------------------------------------------------------
nums = [1, 3, 5]

# 리스트의 원소/요소 읽기 => 인덱싱
print(nums[0], nums[-1])

nums2 = [1, 3, 5, [11, 33, 55]]
print(nums2[0], nums2[-1])
print(nums2[3], nums2[3][1])

nums3 = [1, 3, 5, [11, 33, ['A', 'B'], 55]]
#       0   1  2  3
#                  0    1       2       3     
#                           0     1

print(nums[3], nums3[3][2], nums[3][2][1])

