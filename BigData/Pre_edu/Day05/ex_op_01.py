# ------------------------------------------------------------
#
# 비교연산자
#  : < > <= >= == !=
# ------------------------------------------------------------
n1=44
n2=7

#비교 후 결과 출력
print('%d > %d : %s' %(n1, n2, n1>n2))
print('%d < %d : %s' %(n1, n2, n1<n2))

print('%d >= %d : %s' %(n1, n2, n1>=n2))
print('%d <= %d : %s' %(n1, n2, n1<=n2))

print('%d == %d : %s' %(n1, n2, n1==n2))
print('%d != %d : %s' %(n1, n2, n1!=n2))

n2 = 44.0
print('%d == %f : %s' %(n1, n2, n1==n2))
print('%d != %f : %s' %(n1, n2, n1!=n2))