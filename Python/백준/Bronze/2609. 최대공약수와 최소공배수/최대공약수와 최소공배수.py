# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 
# 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

(a, b) = map(int, input().split())

temp = -1
for i in range(min(a, b), 0, -1):
    if (a % i == 0 and b % i ==0):
        temp = i
        print(temp)
        break
        
print(int(a * b / temp))