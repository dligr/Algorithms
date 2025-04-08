from searches import fibSearch

num = int(input())

A = list(map(lambda x: int(x), input().split(' ')))

fibSearch(A, num)