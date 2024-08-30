# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다

N = int(input())

lst = map(int, input().split())
lst = list(lst)
print(min(lst), max(lst))